from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    response = redirect('/')
    return response

def show(request, my_val):
    return HttpResponse("placeholder to display blog number: "+ str(my_val))

def edit(request, number):
    return HttpResponse("placeholder to edit blog " + str(number))

def destroy(request, my_val):
    response = redirect('/')
    return response