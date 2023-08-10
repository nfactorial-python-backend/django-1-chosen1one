from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Hello, nfactorial school!")

def sum(request, first, second):
    return HttpResponse(f"Sum is: {first + second}")

def uppercase(request, text):
    return HttpResponse(f"{text.upper()}")

def is_palindrome(request, word):
    return HttpResponse(word == word[::-1])

def calculator(request, first, operation, second):
    if operation == "add":
        return HttpResponse(f"{first} + {second} = {first + second}")
    elif operation == "sub":
        return HttpResponse(f"{first} - {second} = {first - second}")
    elif operation == "mult":
        return HttpResponse(f"{first} * {second} = {first * second}")
    else:
        if second == 0:
            return HttpResponseNotFound("can't divide by 0")
        return HttpResponse(f"{first} / {second} = {first / second}")