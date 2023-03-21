from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import ProductCategoryMaster,ProductDetails,UserDetails,ProductDetails,UserDetails,TransactionDetails,HealthStatusDetails,LocationDetails,ProductTransactionDetails
from django.contrib import messages
from django.core.serializers import serialize
import json
from django.db.models import Count
# Create your views here.

def home(request):
    return render(request,"home.html")


def issueRedirect(request):
    list_of_prod = ProductDetails.objects.all()
    list_of_loc = LocationDetails.objects.all()
    # list_of_cat = ProductDetails.objects.select_related('product_cat_id').distinct('product_cat_id')
    list_of_cat = ProductCategoryMaster.objects.all()
    print("list_of_cat---",list_of_cat.query)
    return render(request,"issue/page-issue.html",{'list_of_prod':list_of_prod,'list_of_cat':list_of_cat,'list_of_loc':list_of_loc})

def issueProductCategoryFilter(request):
    list_all_protype = ProductCategoryMaster.objects.filter(product_type=request.GET.get('protype'))
    print("list_all_protype----",list_all_protype)
    return render(request,"ajaxpage/productAJX.html",{'flag':'productCategoryList','list_all_protype':list_all_protype})

def issueProductModelFilter(request):
    list_all_mod = ProductDetails.objects.filter(product_cat_id=request.GET.get('productcat')).exclude(current_quantity=0)
    print("list_all_protype----",list_all_mod)
    return render(request,"ajaxpage/productAJX.html",{'flag':'ProductModelList','list_all_mod':list_all_mod})

def issueOtherProductDetailsFilter(request):
    prod_det = ProductDetails.objects.filter(product_id=request.GET.get('productdet'))
    list_data =[]
    for prod_det in prod_det:
        data_small={
                    "current_quantity":str(prod_det.current_quantity),                
                    "remarks":str(prod_det.remarks)}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),
                        content_type="application/json", safe=False)
    

def issueUserDetailsFilter(request):
    list_all_usr = UserDetails.objects.select_related('usr_des_id').filter(usr_des_id_id__usr_des_type=request.GET.get('issueto'))
    print(list_all_usr.query)
    print("list_all_protype----",list_all_usr)
    return render(request,"ajaxpage/productAJX.html",{'flag':'UserDetailList','list_all_usr':list_all_usr})


def IssueDetailsSubmit(request):
    trn = TransactionDetails()
    trn.trans_type = 'Issued'
    trn.trans_date = request.POST.get('dateIssue')
    received_status=request.POST.get('receiving')
    status=''
    if received_status == 'on':
        status = 'YES'
    else:
        status = 'NO'
    trn.received_status = status
    trn.save()

    total_item = len(request.POST.getlist('proId'))
    proId = request.POST.getlist('proId')
    remarks = request.POST.getlist('proRem')
    no_of_item=request.POST.getlist('proQun')
   
    for t in range(total_item):
        pro_trn = ProductTransactionDetails()
        trans_id=(TransactionDetails.objects.last()).trans_id  
        usr_id=UserDetails.objects.get(usr_id=request.POST.get('receiverName'))
        loc_id=LocationDetails.objects.get(location_id=request.POST.get('postedAt'))
        product_id=ProductDetails.objects.get(product_id=proId[t]) 
        pro_trn.trans_id = TransactionDetails.objects.get(trans_id=trans_id) 
        pro_trn.usr_id = usr_id
        pro_trn.location_id = loc_id
        pro_trn.product_id = product_id
        pro_trn.no_of_item = no_of_item[t]
        pro_trn.remarks = remarks[t]
        pro_trn.save()

        # Updating the current Quantity 
        product_id.current_quantity=str(int(product_id.current_quantity) - int(no_of_item[t]))
        product_id.save()
    messages.success(request, 'Issue Details SAVED Successfully...!!')
    return redirect('/issueRedirect')


def listAllIssueDetails(request):
    
    return render(request,"issue/page-list-issue.html")

def receiptPage(request):
    
    return render(request,"issue/issue_receipt.html")
    

def returnRedirect(request):
    return render(request,"return/page-return.html",{'flag':'Redirect','user_name':''})

def returnGetIssueStuff(request):
    user_name=''
    trn_det_list = TransactionDetails.objects.filter(usr_id=request.POST.get('userdetail'),return_flag=0)
    for a in trn_det_list:
        user_name = a.usr_id.usr_name + " ("+a.usr_id.usr_des_id.usr_des_name +")"
    print("USER_-----------",user_name)
    return render(request,"return/page-return.html",{'trn_det_list':trn_det_list,'user_name':user_name,'flag':'DATA'})

def returnDetailsSubmit(request):
    trn = TransactionDetails()
    trn_no = request.POST.getlist('trn_no')  
    print("trn_no---",trn_no)

    holder = request.POST.getlist('holder')
    product_id = request.POST.getlist('product_id')
    usr_id = request.POST.getlist('usr_id')
    Rquantity = request.POST.getlist('Rquantity')

    productstatus = request.POST.getlist('productstatus')
    producthealth = request.POST.getlist('producthealth')
    print("productstatus----",productstatus,"producthealth---",producthealth)
    remarks = request.POST.getlist('remarks')

    returnDate = request.POST.get('returnDate')
    received_status=request.POST.get('receiving')
    for idx, x in enumerate(holder):
        print("HOLDER DATA -- ",x)
        if x =='on':            
            product=ProductDetails.objects.get(product_id=product_id[idx])
            usr=UserDetails.objects.get(usr_id=usr_id[idx])         
            status=''
            if received_status == 'on':
                    status = 'YES'
            else:
                    status = 'NO'
            trn.product_id = product
            trn.usr_id = usr
            trn.trans_type = 'At Computer Section'
            trn.return_flag = 2
            trn.trans_date = returnDate
            trn.no_of_item = Rquantity[idx]
            trn.remarks = remarks[idx]
            trn.received_status = status
            trn.save()
            # Updating the Return Flag 
            print("trn_no[idx]---",trn_no[idx])
            trn_up = TransactionDetails.objects.get(trans_id=trn_no[idx])
            trn_up.return_flag = 1
            trn_up.save()
            # Updating the current Quantity 
            product.current_quantity=str(int(product.current_quantity) + int(Rquantity[idx]))
            product.save()
            # Inserting Data in Health Table
            health = HealthStatusDetails()
            health.product_id = product_id[idx]
            health.product_healthy = producthealth[idx]
            health.health_remarks = remarks[idx]
            health.product_status = productstatus[idx]
            health.status_date = returnDate
            health.save()                        
    return render(request,"return/page-return.html",{'flag':'Redirect','user_name':''})


def listAllReturnDetails(request):
    return render(request,"return/page-list-return.html")


def healthDetailsRedirect(request):
    return render(request,"reports/health.html")