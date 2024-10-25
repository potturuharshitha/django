from django.shortcuts import render

# Create your views here.
def usearch(request,pid):
    customers=[{'id':1,'name':'likitha','address':'kldroad','phoneno':9732},
         {'id':2,'name':'tarun','address':'3ndroad','phoneno':45847},
         {'id':3,'name':'parnika','address':'2ndroad','phoneno':7847},
         {'id':4,'name':'lahari','address':'4ndroad','phoneno':23847}]
    result=None
    for item in customers:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>laptopname:{result.get('name')}<br>cost:{result.get('address')}<br>phoneno:{result.get('phoneno')}</p>")
    else:
        return HttpResponse("Sorry not matched")