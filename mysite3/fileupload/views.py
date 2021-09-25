from django.shortcuts import render
from .models import FilesUpload

# Create your views here.
def home(request):
	if request.method =="POST":
		file2=request.FILES["file"]
		document=FilesUpload.objects.create(file=file2)
		document.save()


	return render(request,"index.html")

def viewdata(response):
	return render(response, "viewdata.html")
