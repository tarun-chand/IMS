from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProductCategoryMaster
from django.contrib import messages

def productCatRedirect(request):
    list_all_pc = ProductCategoryMaster.objects.all()
    return render(request,"master/product/productCategory.html",{'flag':'NEW','list_all_pc':list_all_pc})

def productCatSubmit(request):
    pcm = ProductCategoryMaster()
    producttype = request.POST['producttype']
    productcatname = request.POST['productcategory']
    is_exists = ProductCategoryMaster.objects.filter(product_type=producttype,product_cat_name=productcatname).exists()
    if is_exists:
        messages.info(request, 'Product Category with this Product Type is already exists.!!')
        print("RETURN FROM EXIXST")
        return redirect('/productCatRedirect')
        
    pcm.product_type = producttype
    pcm.product_cat_name = productcatname
    pcm.save()
    messages.success(request, 'Product Category SAVED Successfully...!!')
    return redirect('/productCatRedirect')
    

def productCatUpdateRedirect(request):
    pcid = request.GET.get('pcid')
    pcdata = ProductCategoryMaster.objects.filter(product_cat_id=pcid)
    list_all_pc = ProductCategoryMaster.objects.all()
    return render(request,"master/product/productCategory.html",{'flag':'UPDATE','pcdata':pcdata,'list_all_pc':list_all_pc})


def productCatUpdate(request):
    pcdata = ProductCategoryMaster.objects.get(product_cat_id=request.POST.get('pcid'))
    pcdata.product_type=request.POST.get('producttype')
    pcdata.product_cat_name=request.POST.get('productcategory')
    pcdata.save()
    messages.success(request, 'Product Category UPDATED Successfully...!!')
    return redirect('/productCatRedirect')


def productDetails(request):
    return render(request,"master/product/productDetails.html")