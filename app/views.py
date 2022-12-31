from django.shortcuts import render

# Create your views here.
def hai(requset):
    return render (requset,'hai.html')
    
    
def hello(request):
    return  render (request,'hello.html')
