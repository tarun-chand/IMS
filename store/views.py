from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html")

def productCatRedirect(request):
    return render(request,"master/product/productCategory.html")

def productCatSubmit(request):
    producttype=request.GET.get('producttype')
    productcategory=request.GET.get('productcategory')

    return render(request,"master/product/productCategory.html")

def productDetails(request):
    return render(request,"master/product/productDetails.html")

def userDesignationRedirect(request):
    return render(request,"master/users/userDesignation.html")

def userDetails(request):
    return render(request,"master/users/userDetails.html")

def buildingDetails(request):
    return render(request,"master/location/buildingDetails.html")

def sectionRedirect(request):
    return render(request,"master/location/sectionDetails.html")

def locationRedirect(request):
    return render(request,"master/location/locationDetails.html")
    

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