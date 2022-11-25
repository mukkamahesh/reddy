from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':200,'b':100,'c':50}
    return render (request,'a2_first.html',context=d)
def a2_second(request):
    d={'name':'mahesh'}
    return render (request,'a2_second.html',context=d)

