from django.shortcuts import render

# Create your views here.
def profile(request):
    """ view fro profile page"""    
    template = "profile/profile.html"
    context = {}

    return render(request, template, context)