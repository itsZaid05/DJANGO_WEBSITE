from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return render(request,'index.html')
   # return HttpResponse("this is my yard")
def about (request):
    return render(request,'about.html')
    #return HttpResponse("this is my about page")
def services (request):
    return render(request,'services.html')
   # return HttpResponse("this is my services")
def contact (request):
    return render(request,'contact.html')
   # return HttpResponse("this is my contact")