from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .forms import *
from .models import Business, Notices, Profile, Neighborhood
from django.contrib.auth.models import User


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
def new_hood(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.profile = profile
            hood.save()
        return redirect('Landing')
    else:
        form = HoodForm()
    return render(request, 'new_hood.html', {"form": form})
def notice_new(request,id):
    date = dt.date.today()
    hood=Neighborhood.objects.get(id=id)
    notice= Notices.objects.filter(neighborhood=hood)
    form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.user = request.user.profile
            notice.profile = profile
            notice.neighborhood = hood
            notice.save()
            return redirect('Landing')
    else:
        form = NoticeForm()
        return render(request,'new_notice.html',{"form":form,"notice":notice,"hood":hood,  "date":date})
def hoods(request,id):
    date = dt.date.today()
    post=Neighborhood.objects.get(id=id)
    brushs = Notices.objects.filter(neighborhood=post) 
    business = Business.objects.filter(neighborhood=post)
    return render(request,'each_hood.html',{"post":post,"date":date, "brushs":brushs,"business":business})
def post_business(request,id):
    date = dt.date.today()
    hood=Neighborhood.objects.get(id=id)
    business = Business.objects.filter(neighborhood=hood)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.neighborhood = hood
            business.save()
            return redirect('Landing')
    else:
        form = BusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"hood":hood,  "date":date})
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Awards account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('Landing')
#         return HttpResponse('Thank you for your email confirmation. Now you can now <a href="/accounts/login/">Login</a> your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')