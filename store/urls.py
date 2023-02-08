from django.urls import path

from . import views
from . import product_view
from . import user_view
from . import location_view
import re  as r

urlpatterns = [
    path('', views.home, name='home'),

    path('productCatRedirect', product_view.productCatRedirect, name='productCatRedirect'),
    path('productCatSubmit', product_view.productCatSubmit, name='productCatSubmit'),
    path('productCatUpdateRedirect', product_view.productCatUpdateRedirect, name='productCatUpdateRedirect'),
    path('productCatUpdate', product_view.productCatUpdate, name='productCatUpdate'),
    
    path('productDetails', product_view.productDetails, name='productDetails'),
    path('productCategoryFilter', product_view.productCategoryFilter, name='productCategoryFilter'),
    path('productDetailsSubmit', product_view.productDetailsSubmit, name='productDetailsSubmit'),
    
    path('userDesignationRedirect', user_view.userDesignationRedirect, name='userDesignationRedirect'),
    path('userDesignationSubmit', user_view.userDesignationSubmit, name='userDesignationSubmit'),
    path('userDesignationUpdateRedirect', user_view.userDesignationUpdateRedirect, name='userDesignationUpdateRedirect'),
    path('userDesignationUpdate', user_view.userDesignationUpdate, name='userDesignationUpdate'),

    path('userDetails', user_view.userDetails, name='userDetails'),

    path('buildingDetailsRedirect', location_view.buildingDetailsRedirect, name='buildingDetailsRedirect'),
    path('buildingDetailsSubmit', location_view.buildingDetailsSubmit, name='buildingDetailsSubmit'),
    path('buildingDetailsUpdateRedirect', location_view.buildingDetailsUpdateRedirect, name='buildingDetailsUpdateRedirect'),
    path('buildingDetailsUpdate', location_view.buildingDetailsUpdate, name='buildingDetailsUpdate'),
  
    path('sectionRedirect', location_view.sectionRedirect, name='sectionRedirect'),
    path('sectionDetailsSubmit', location_view.sectionDetailsSubmit, name='sectionDetailsSubmit'),
    path('sectionDetailsUpdateRedirect', location_view.sectionDetailsUpdateRedirect, name='sectionDetailsUpdateRedirect'),
    path('sectionDetailsUpdate', location_view.sectionDetailsUpdate, name='sectionDetailsUpdate'),



    path('locationRedirect', location_view.locationRedirect, name='locationRedirect'),
    path('locationSectionFilter', location_view.locationSectionFilter, name='locationSectionFilter'),
    path('locationDetailsSubmit', location_view.locationDetailsSubmit, name='locationDetailsSubmit'),
    path('locationDetailsUpdateRedirect', location_view.locationDetailsUpdateRedirect, name='locationDetailsUpdateRedirect'),
    path('locationDetailsUpdate', location_view.locationDetailsUpdate, name='locationDetailsUpdate'),


    path('issueRedirect', views.issueRedirect, name='issueRedirect'),
    path('listAllIssueDetails', views.listAllIssueDetails, name='listAllIssueDetails'),
    path('returnRedirect', views.returnRedirect, name='returnRedirect'),
    path('listAllReturnDetails', views.listAllReturnDetails, name='listAllReturnDetails'),
    path('healthDetailsRedirect', views.healthDetailsRedirect, name='healthDetailsRedirect'),
]
