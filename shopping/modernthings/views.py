from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msearch(request,id):
    mobiles = [{'id':1,'name':'samsung','config':["10gb","24rom"]},
    {'id':2,'name':'vivo','config':["34gb","25rom"]},
    {'id':3,'name':'redmi','config':["280","16rom"]},
    {'id':4,'name':'iphone','config':["180","8rom"]}      
    ]
result=None
for item m mobiles:
    if item.get('id')=id
    result=item
    break
if result is not none:
    return Httpresponse("<p>mobile name:{result.get('name')}<br>config:{result.get('config')}</p>")
else:
    return Httpresponse("not result matched")      

def lsearch(request,id):
    laptops = [{'id':1,'name':'lenovo','config':["64bit","24rom"]},
    {'id':2,'name':'macbook','config':["32bit","25rom"]},
    {'id':3,'name':'thinkpad','config':["64 bit","16rom"]},
    {'id':4,'name':'asus','config':["64 bit","18rom"]}      
    ]
result=None
for item m laptops:
    if item.get('id')=id
    result=item
    break
if result is not none:
    return Httpresponse("<p>laptop name:{result.get('name')}<br>config:{result.get('config')}</p>")
else:
    return Httpresponse("not result matched")  
return HttpResponse


def asearch(request,id):
    airpods = [{'id':1,'name':'apple'},
    {'id':2,'name':'boot'},
    {'id':3,'name':'earnoise'},
    {'id':4,'name':'realme'} ,     
    ]
result=None
for item m airpods:
    if item.get('id')=id
    result=item
    break
if result is not none:
    return Httpresponse("<p>airpods name:{result.get('name')}</p>")
else:
    return Httpresponse("not result matched")        