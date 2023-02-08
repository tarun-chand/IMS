from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDesignationMaster
from django.contrib import messages


def userDesignationRedirect(request):
    list_all_ud = UserDesignationMaster.objects.all()
    return render(request,"master/users/userDesignation.html",{'flag':'NEW','list_all_ud':list_all_ud})

def userDesignationSubmit(request):
    udm = UserDesignationMaster()
    usrdestype = request.POST.get('usrdestype')
    usrdesname = request.POST.get('usrdesname')
    print("-------------------------------DATA----------------------",usrdestype,usrdesname)
    is_exists = UserDesignationMaster.objects.filter(usr_des_type=usrdestype,usr_des_name=usrdesname).exists()
    if is_exists:
        messages.info(request, 'User Designation with this User Type is already exists.!!')
        return redirect('/userDesignationRedirect')
        # return render(request,"master/product/usrdesname.html",{'list_all_ud':list_all_ud})
    udm.usr_des_type = usrdestype
    udm.usr_des_name = usrdesname
    udm.save()
    messages.success(request, 'User Designation Saved Successfully...!!')
    return redirect('/userDesignationRedirect')
    # return render(request,"master/product/usrdesname.html",{'list_all_ud':list_all_ud})

def userDesignationUpdateRedirect(request):
    uddata = UserDesignationMaster.objects.filter(usr_des_id=request.GET.get('udid'))
    list_all_ud = UserDesignationMaster.objects.all()
    return render(request,"master/users/userDesignation.html",{'flag':'UPDATE','uddata':uddata,'list_all_ud':list_all_ud})


def userDesignationUpdate(request):
    uddata = UserDesignationMaster.objects.get(usr_des_id=request.POST.get('udid'))
    uddata.usr_des_type=request.POST.get('usrdestype')
    uddata.usr_des_name=request.POST.get('usrdesname')
    uddata.save()
    messages.success(request, 'User Designation UPDATED Successfully...!!')
    return redirect('/userDesignationRedirect')





def userDetails(request):
    return render(request,"master/users/userDetails.html")