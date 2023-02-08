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

def productCategoryFilter(request):
    list_all_protype = ProductCategoryMaster.objects.filter(product_type=request.GET.get('protype'))
    return render(request,"master/product/productCatListAJX.html",{'list_all_protype':list_all_protype})

def productDetailsSubmit(request):
    pd = ProductCategoryMaster()
    productcat = request.POST['productcat']
    productname = request.POST['productname']
    modelname = request.POST['modelname']
    serialno = request.POST['serialno']
    quantity = request.POST['quantity']
    toner = request.POST['toner']

    
    is_exists = ProductCategoryMaster.objects.filter(product_type=producttype,product_cat_name=productcatname).exists()
    if is_exists:
        messages.info(request, 'Product Category with this Product Type is already exists.!!')
        print("RETURN FROM EXIXST")
        return redirect('/productCatRedirect')
        
    pd.product_type = productcat
    pd.product_cat_name = productname
    pd.product_type = modelname
    pd.product_cat_name = serialno
    pd.product_type = quantity
    pd.product_cat_name = toner
    pd.save()
    messages.success(request, 'Product Category SAVED Successfully...!!')
    return redirect('/productCatRedirect')