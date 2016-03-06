from django.shortcuts import render
from django.views import generic
from .models import Directory
from .forms import DirectoryForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def IndexView(request):
    model = Directory
    queryset=Directory.objects.all()
    template_name = 'app1/index.html'
    form=DirectoryForm()
    if request.method == "POST":
    	form=DirectoryForm(request.POST or None)
    	if form.is_valid():
		    instance=form.save(commit=False)
		    instance.save()
		    messages.success(request,"Record successfully added!")
		    form=DirectoryForm()



    query= request.GET.get("q")
    if query:
    	queryset=queryset.filter(
    		Q(name__icontains=query) | 
    	    Q(number__icontains=query)
    	    )
    
    context= {
    	"objects_list": queryset,
    	"form": form,
    	"success": True
    }
    return render(request,"app1/index.html",context)

@login_required(login_url='/app1/login/')
def Directory_Add(request):
	form=DirectoryForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Record successfully added!")
	else:
		
		context= { 
		"form": form
		}
	return render(request,"app1/index.html",context)

@login_required(login_url='/app1/login/')
def Directory_Detail(request,slug=None):
	instance=get_object_or_404(Directory,slug=slug)
	form=DirectoryForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Record Updated!")
		return redirect("app1:index")

	context= {
	"instance":instance,
	"form":form,
	}
	return render(request,"app1/Directory_Detail.html",context)
def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'app1/login.html')


# @login_required(login_url='/')
# def home(request):
#     return render_to_response('app1/home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')

# Create your views here.
