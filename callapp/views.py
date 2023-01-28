from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def calculator(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    op_type=request.GET["op"]
    if op_type=="add":
        z=x+y
    elif op_type=="sub":
        z=x-y
    elif op_type=="mul":
        z=x*y
    else:
        op_type=="div"
        z=x/y
    return HttpResponse("the"+op_type+"is:"+str[z])
