from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProductCategoryMaster
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")


def issueRedirect(request):
    return render(request,"issue/page-issue.html")

def listAllIssueDetails(request):
    return render(request,"issue/page-list-issue.html")

def returnRedirect(request):
    return render(request,"return/page-return.html")

def listAllReturnDetails(request):
    return render(request,"return/page-list-return.html")


def healthDetailsRedirect(request):
    return render(request,"reports/health.html")