from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('productCatRedirect', views.productCatRedirect, name='productCatRedirect'),
    path('productCatSubmit', views.productCatSubmit, name='productCatSubmit'),

    path('productDetails', views.productDetails, name='productDetails'),

    path('userDesignationRedirect', views.userDesignationRedirect, name='userDesignationRedirect'),
    path('userDetails', views.userDetails, name='userDetails'),

    path('buildingDetails', views.buildingDetails, name='buildingDetails'),
    path('sectionRedirect', views.sectionRedirect, name='sectionRedirect'),
    path('locationRedirect', views.locationRedirect, name='locationRedirect'),


    path('issueRedirect', views.issueRedirect, name='issueRedirect'),
    path('listAllIssueDetails', views.listAllIssueDetails, name='listAllIssueDetails'),
    path('returnRedirect', views.returnRedirect, name='returnRedirect'),
    path('listAllReturnDetails', views.listAllReturnDetails, name='listAllReturnDetails'),

    path('healthDetailsRedirect', views.healthDetailsRedirect, name='healthDetailsRedirect'),
]
