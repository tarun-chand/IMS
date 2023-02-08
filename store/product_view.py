from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProductCategoryMaster,ProductDetails
from django.contrib import messages

def productCatRedirect(request):
    list_all_pc = ProductCategoryMaster.objects.all()
    return render(request,"master/product/productCategory.html",{'flag':'NEW','list_all_pc':list_all_pc})

def productCatSubmit(request):
    pcm = ProductCategoryMaster()
    producttype = request.POST.get('producttype')
    productcatname = request.POST.get('productcategory')
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
    list_all_pd = ProductDetails.objects.all()
    return render(request,"master/product/productDetails.html",{'list_all_pd':list_all_pd})

def productCategoryFilter(request):
    list_all_protype = ProductCategoryMaster.objects.filter(product_type=request.GET.get('protype'))
    return render(request,"master/product/productCatListAJX.html",{'list_all_protype':list_all_protype})

def productDetailsSubmit(request):
    pd = ProductDetails()
    productcat = ProductCategoryMaster.objects.get(product_cat_id=request.POST.get('productcat'))
    productname = request.POST.get('productname')
    modelname = request.POST.get('modelname')
    serialno = request.POST.get('serialno')
    quantity = request.POST.get('quantity')
    toner = request.POST.get('toner')
    remarks = request.POST.get('remarks')

    is_exists = ProductDetails.objects.filter(product_cat_id=productcat,product_name=productname,product_model=modelname,product_serialno=serialno,initial_quantity=quantity,cartridge_toner=toner,remarks=remarks).exists()
    if is_exists:
        messages.info(request, 'Product Detail with Given Details is already exists.!!')
        print("RETURN FROM EXIXST")
        return redirect('/productDetails')
        
    pd.product_cat_id = productcat
    pd.product_name = productname
    pd.product_model = modelname
    pd.product_serialno = serialno
    pd.initial_quantity = quantity
    pd.cartridge_toner = toner
    pd.remarks = remarks
    pd.save()
    messages.success(request, 'Product Detail SAVED Successfully...!!')
    return redirect('/productDetails')