from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import BuildingMaster,SectionDetails,LocationDetails
from django.contrib import messages
from django.core import serializers
import json


# Building Data Collection START ===============================================

def buildingDetailsRedirect(request):
    list_all_bm = BuildingMaster.objects.all()
    return render(request,"master/location/buildingDetails.html",{'flag':'NEW','list_all_bm':list_all_bm})

def buildingDetailsSubmit(request):
    bm = BuildingMaster()
    buildingname = request.POST.get('buildingname')
    is_exists = BuildingMaster.objects.filter(building_name=buildingname).exists()
    if is_exists:
        messages.info(request, 'Building Name is already exists.!!')
        print("RETURN FROM EXIXST")
        return redirect('/buildingDetailsRedirect')
        # return render(request,"master/product/buildingname.html",{'list_all_bm':list_all_bm})
    bm.building_name = buildingname
    bm.save()
    messages.success(request, 'Building Name Saved Successfully...!!')
    return redirect('/buildingDetailsRedirect')
    # return render(request,"master/product/buildingname.html",{'list_all_bm':list_all_bm})

def buildingDetailsUpdateRedirect(request):
    bmid = request.GET.get('bmid')
    bmdata = BuildingMaster.objects.filter(building_id=bmid)
    list_all_bm = BuildingMaster.objects.all()
    return render(request,"master/location/buildingDetails.html",{'flag':'UPDATE','bmdata':bmdata,'list_all_bm':list_all_bm})


def buildingDetailsUpdate(request):
    bmdata = BuildingMaster.objects.get(building_id=request.POST.get('bmid'))
    bmdata.building_name=request.POST.get('buildingname')
    bmdata.save()
    messages.success(request, 'Building Name UPDATED Successfully...!!')
    return redirect('/buildingDetailsRedirect')

# Building Data Collection END ===============================================

# Section Data Collection Start ===============================================

def sectionRedirect(request):
    list_all_bm = BuildingMaster.objects.all()
    list_all_sc = SectionDetails.objects.all()
    return render(request,"master/location/sectionDetails.html",{'list_all_bm':list_all_bm,'list_all_sc':list_all_sc})

def sectionDetailsSubmit(request):
    sd = SectionDetails()
    building_obj = BuildingMaster.objects.get(building_id=request.POST.get('buildingname'))
    sectiontype = request.POST.get('sectiontype')
    sectionname = request.POST.get('sectionname')
    is_exists = SectionDetails.objects.filter(building_name=building_obj,section_type=sectiontype,section_name=sectionname).exists()
    if is_exists:
        messages.info(request, 'Section Detail with this Building Name and Section Type is already exists.!!')
        return redirect('/sectionRedirect')
        
    sd.building_name = building_obj
    sd.section_type = sectiontype
    sd.section_name = sectionname
    sd.save()
    messages.success(request, 'Section Detail SAVED Successfully...!!')
    return redirect('/sectionRedirect')
    

def sectionDetailsUpdateRedirect(request):
    scid = request.GET.get('scid')
    scdata = SectionDetails.objects.filter(section_id=scid)
    list_all_sc = SectionDetails.objects.all()
    list_all_bm = BuildingMaster.objects.all()
    return render(request,"master/location/sectionDetails.html",{'flag':'UPDATE','scdata':scdata,'list_all_bm':list_all_bm,'list_all_sc':list_all_sc})


def sectionDetailsUpdate(request):
    scdata = SectionDetails.objects.get(section_id=request.POST.get('scid'))
    scdata.building_name=BuildingMaster.objects.get(building_id=request.POST.get('buildingname'))
    scdata.section_type=request.POST.get('sectiontype')
    scdata.section_name=request.POST.get('sectionname')
    scdata.save()
    messages.success(request, 'Product Category UPDATED Successfully...!!')
    return redirect('/sectionRedirect')




# Section Data Collection END ===============================================

# Location Data Collection Start ===============================================

def locationRedirect(request):
    list_all_loc = LocationDetails.objects.select_related('section_id')
    return render(request,"master/location/locationDetails.html",{'list_all_loc':list_all_loc})
    
def locationSectionFilter(request):
    sectype = request.GET.get('sectype')
    list_all_sc = SectionDetails.objects.filter(section_type=sectype)
    return render(request,"master/location/sectionList.html",{'list_all_sc':list_all_sc})

def locationDetailsSubmit(request):
    loc = LocationDetails()
    # sectiontype_obj = SectionDetails.objects.get(section_id=request.POST.get('sectionname')).section_type
    section_obj = SectionDetails.objects.get(section_id=request.POST.get('sectionname'))
    floor = request.POST.get('floor')
    room = request.POST.get('room')
    landmark = request.POST.get('landmark')
    is_exists = LocationDetails.objects.filter(section_id=section_obj,floor = floor,roomno=room,landmark=landmark).exists()
    if is_exists:
        messages.info(request, 'Location Detail with given Details is already exists.!!')
        return redirect('/locationRedirect')
    loc.section_id = section_obj
    loc.floor = floor
    loc.roomno = room
    loc.landmark = landmark
    loc.save()
    messages.success(request, 'Location Detail SAVED Successfully...!!')
    return redirect('/locationRedirect')

        
def locationDetailsUpdateRedirect(request):
    locid = request.GET.get('locid')
    locdata = LocationDetails.objects.filter(location_id=locid)
    list_all_loc = LocationDetails.objects.select_related('section_id')
    return render(request,"master/location/locationDetails.html",{'flag':'UPDATE','locdata':locdata,'list_all_loc':list_all_loc})


def locationDetailsUpdate(request):
    locdata = LocationDetails.objects.get(location_id=request.POST.get('locid'))
    locdata.section_id=SectionDetails.objects.get(section_id=request.POST.get('sectionname'))
    locdata.floor=request.POST.get('floor')
    locdata.roomno=request.POST.get('room')
    locdata.landmark=request.POST.get('landmark')
    locdata.save()
    messages.success(request, 'Location Detail UPDATED Successfully...!!')
    return redirect('/locationRedirect')
    
    
    

    
# Location Data Collection END ===============================================

