from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from . import views


urlpatterns=[
    url('^$',views.landing,name='Landing'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^business/(\d+)',views.business,name ='business'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'^new/hood$', views.new_hood, name='new-hood'),
    url(r'^hoods/new/notice/(\d+)$', views.notice_new, name='new-notice'),
    # url(r'^map$', views.maps, name='maps'),
    # url(r'^hoods/new/business/(\d+)$',views.post_business, name='new-business'),
    # url(r'^hoods/(\d+)',views.hoods,name='hoods'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)