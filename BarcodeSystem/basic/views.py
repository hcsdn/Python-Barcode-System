from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
def list_barcodes(request):
    assert(request,HttpRequest)
    test = request.POST.get("test")
    return render(
         request,
         'list_barcodes.html',
         {
             test:test
         }
     )