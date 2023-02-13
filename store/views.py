from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import ProductCategoryMaster,ProductDetails
from django.contrib import messages
from django.core import serializers
# Create your views here.

def home(request):
    return render(request,"home.html")


def issueRedirect(request):
    list_of_prod = ProductDetails.objects.all()
    return render(request,"issue/page-issue.html",{'list_of_prod':list_of_prod})

def issueProductCategoryFilter(request):
    list_all_protype = ProductCategoryMaster.objects.filter(product_type=request.GET.get('protype'))
    print("list_all_protype----",list_all_protype)
    return render(request,"ajaxpage/productAJX.html",{'flag':'productCategoryList','list_all_protype':list_all_protype})

def issueProductFilter(request):
    list_all_prod = ProductDetails.objects.filter(product_cat_id=request.GET.get('productcat'))
    print("list_all_protype----",list_all_prod)
    return render(request,"ajaxpage/productAJX.html",{'flag':'productList','list_all_prod':list_all_prod})

def issueProductDetailsFilter(request):
    prod_det = ProductDetails.objects.filter(product_cat_id=request.GET.get('productdet'))
    data = serializers.serialize('json', prod_det)
    
    return HttpResponse(data, content_type="application/json")
    # return JsonResponse({'prod_det':prod_det})
    # return render(request,"ajaxpage/productAJX.html",{'flag':'productList','prod_det':prod_det})



def listAllIssueDetails(request):
    
    return render(request,"issue/page-list-issue.html")

def returnRedirect(request):
    return render(request,"return/page-return.html")

def listAllReturnDetails(request):
    return render(request,"return/page-list-return.html")


def healthDetailsRedirect(request):
    return render(request,"reports/health.html")