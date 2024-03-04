from django.shortcuts import render

# Create your views here.


def index_view(request):
    
     return render(request, 'website/index.html')





cont={'tel':'+971 56 808 7789', 'city':'Dubai, UAE', 'email':'bagheri.payam@gmail.com', 'job':'BI Developer &amp;  SQL Server Expert'} 
def about_view(request):
    
     return render(request, 'website/about.html', cont)
 
 
 
context ={'email':'bagheri.payam@gmail.com', 'tel':'+971 56 808 7789', 'location':'Corniche, Dubai, UAE'}
def contact_view(request):
    
     return render(request, 'website/contact.html', context)
 
def education_view(request):
    
     return render(request, 'website/education.html')
 
def experiences_view(request):
    
     return render(request, 'website/experiences.html')
 
def languages_view(request):
    
     return render(request, 'website/languages.html')
 
def skills_view(request):
    
     return render(request, 'website/skills.html')
 
 
