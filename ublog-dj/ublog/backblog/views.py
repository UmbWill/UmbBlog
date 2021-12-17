from django.shortcuts import render

# Create your views here.
def post_list(request):
    return resnder(request,'backblog/templates/post_list.html',{})