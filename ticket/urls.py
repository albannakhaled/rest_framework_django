from django.contrib import admin
from django.urls import path , include
from ticket import views

urlpatterns = [
    path('wayOne/',views.no_rest_no_model,name='jsonresponse'),#api without rest frame work without model
    path('wayTwo/',views.no_rest_with_model,name=''),# with model without rest 
    path('FBV_List/',views.FBV_List,name=''),
    path('CBV_List/',views.CBV_List.as_view(),name=''),
    path('CBV_PK<int:pk>/', views.CBV_PK.as_view(), name='mymodel-detail'),

]