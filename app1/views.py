from django.shortcuts import render
from django.views import generic
from .models import Directory
from .forms import DirectoryForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q


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


def Directory_Add(request):
	form=DirectoryForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Record successfully added!")
	else:
		form = DirectoryForm()
	return redirect("app1:index")


# Create your views here.
