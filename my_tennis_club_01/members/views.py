from django.http import HttpResponse
from django.template import loader
from .models import Member #here we imported the model to send it to the template to be displayed

def members(request):
  mymembers = Member.objects.all().values() #Creates a mymembers object with all the values of the Member model.
  template = loader.get_template('all_members.html')#Loads the all_members.html template.
  context = {                 #Creates an object containing the mymembers object.
    'mymembers': mymembers,   #Sends the object to the template.
  }
  return HttpResponse(template.render(context, request)) #Outputs the HTML that is rendered by the template.

def details(request, id): #takes id as an argument & locate the record in the Member table
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html') #loads details.html template
  context = { 
    'mymember': mymember, #creates an object that contains the member 
  }
  return HttpResponse(template.render(context, request)) #sends the object to the template & outputs the html rendered by the template

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")