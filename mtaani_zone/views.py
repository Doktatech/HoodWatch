from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Business, Notices, Profile


# Create your views here.
def landing(request): 
    hoods = Neighborhood.objects.all()     
    return render(request, 'landing.html',{"hoods":hoods})
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
def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    hoods = Neighbourhood.objects.all()
    return render(request, 'profile/profile.html', {"date": date, "profile":profile,"hoods":hoods})
def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})
