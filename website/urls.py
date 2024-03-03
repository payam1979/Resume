from django.urls import path
from website.views import *

app_name='website'

urlpatterns = [
    
   
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('education', education_view, name='education'),
    path('experiences', experiences_view, name='experiences'),
    path('languages', languages_view, name='languages'),
    path('skills', skills_view, name='skills'),
    
   ]
