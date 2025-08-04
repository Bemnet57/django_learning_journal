from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values() #Creates a mymembers object with all the values of the Member model.
  template = loader.get_template('all_members.html')#Loads the all_members.html template.
  context = {                 #Creates an object containing the mymembers object.
    'mymembers': mymembers,   #Sends the object to the template.
  }
  return HttpResponse(template.render(context, request)) #Outputs the HTML that is rendered by the template.
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")