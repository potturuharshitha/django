from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bus1(request):
    d={'routes':[{'id':'bus1','area':'ananthapur'},
    {'id':'bus2','area':'bks'},
    {'id':'bus3','area':'darmavaram'},
    {'id':'bus4','area':'tadipatri'},
    {'id':'bus5','area':'pamidi'}
    ]}
    return render(request,'busesfile.html',d)