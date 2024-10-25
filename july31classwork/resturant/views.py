from django.shortcuts import render
from resturant.models import menu
# Create your views here.
def func2(request): 
    result=menu.objects.all()  
    return render(request,'index.html',{'res':result})
def insert_data(request):
    result=menu.objects.all()
    if request.method=="POST":
        dish=request.POST.get("food")
        cost=request.POST.get("food_price")
        obj=menu(itemName=dish,price=cost)
        obj.save()
        result=menu.objects.all()   
        return render(request,'form.html',{'res':result})
    return render(request,'form.html',{'res':result})    

