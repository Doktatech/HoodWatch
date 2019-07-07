from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Business, Notices


# Create your views here.
def landing(request): 
    business=Business.get_business()   
    return render(request, 'landing.html',{"business":business})
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term =request.GET.get("business")
        searched_business = Business.search_by_type(search_term)
        message=f"{search_term}"
        return render(request, 'search.html',{"message":message,"businesses": searched_business})
    else:
        message = "You haven't searched for any Business"
        return render(request, 'search.html',{"message":message})
def business(request,business_id):
    try:
        business= Business.objects.get(id=business_id)
    except DoesNotExist:
        raise Http404()        
    return render(request,"single_business.html",{"business":business})