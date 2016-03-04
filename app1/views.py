from django.shortcuts import render
from django.views import generic
from .models import Directory
from .forms import DirectoryForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response


def IndexView(request):
    model = Directory
    queryset=Directory.objects.all()
    template_name = 'app1/index.html'
    form=DirectoryForm()

    query= request.GET.get("q")
    if query:
    	queryset=queryset.filter(
    		Q(name__icontains=query) | 
    	    Q(number__icontains=query)
    	    )

    context= {
    	"objects_list": queryset,
    	"form": form
    }
    return render(request,"app1/index.html",context)

def submit_search(request):
	numbers = []
	search_text = "" 
	if(request.method == "GET"):
		search_text = request.GET.get("number_search_text", "")
	number_results = []
	if(search_text != ""):
		number_results = Directory.objects.filter(Q(name__icontains=search_text) | Q(number__icontains=search_text))
	context= {
    	"objects_list": number_results,
    	"search_text": search_text
    }
	return  render_to_response("app1/search_results__html_snippet.html",context)

def Directory_Add(request):
	form=DirectoryForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Record successfully added!")
	else:
		form = DirectoryForm()
	return redirect("app1:index")

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


# Create your views here.
