from django.shortcuts import render, redirect
from .models import *
from django.views import generic 
from django.contrib import messages


# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status = 1).order_by('-created_on')[:2]
  template_name = 'index.html'
  

class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'


def contact(request):
    if request.method=='POST':
       fullname=request.POST['fullname']
       phone=request.POST['phone']
       message=request.POST['message']
       contact = Contact(fullname=fullname, phone=phone,message=message)
       contact.save()

    return render(request, 'contact.html')

# def News(request):
#    if request.method=='POST':
#       email = request.POST['email']
#       news = Newsletter(email=email)
#       news.save()

def News(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        newsletter_obj = Newsletter(email=email)
        newsletter_obj.save()
        
        return redirect('/') 

    return render(request, '/') 

class AllPost(generic.ListView):
  queryset = Post.objects.filter(status = 1).order_by('-created_on')
  template_name = 'allpost.html'

