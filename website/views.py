from django.shortcuts import render

# Create your views here.


def index_view(request):
    
     return render(request, 'website/index.html')
 
def about_view(request):
    
     return render(request, 'website/about.html')
 
def contact_view(request):
    
     return render(request, 'website/contact.html')
 
def education_view(request):
    
     return render(request, 'website/education.html')
 
def experiences_view(request):
    
     return render(request, 'website/experiences.html')
 
def languages_view(request):
    
     return render(request, 'website/languages.html')
 
def skills_view(request):
    
     return render(request, 'website/skills.html')
 
 
