from django.contrib import admin
from django.urls import path , include
from ticket import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    #path('wayOne/',views.no_rest_no_model,name='jsonresponse'),#api without rest frame work without model
    path('wayTwo/',views.no_rest_with_model,name=''),# with model without rest 
    path('wayThree/',views.FBV_List,name=''),#function based view (put , post)
    path('wayFour/',views.CBV_List.as_view(),name=''),#class based view
    path('wayFive/<int:pk>/', views.CBV_PK.as_view(), name='mymodel-detail'),#function based views with pk
    path('waySix/', views.GuestList.as_view(), name='mymodel-detail'),# mixin
    path('waySeven/<int:pk>', views.MixinDetail.as_view(), name='mymodel-detail'),#mixin with pk
    path('wayEight/', views.Generic_list.as_view(), name='mymodel-detail'),# generic
    path('wayNine/<int:pk>/', views.Generic_details.as_view(), name='mymodel-detail'),# generic with pk

    # token authentication
    # path('api-token/',views.obtain_auth_token)
    path('api-token-auth/', obtain_auth_token)
]