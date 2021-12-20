# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import Brand_Details,Brand_Add,Brand_Edit,Size_Home,Size_Edit,Color_Home,Color_Add,Color_Edit,Category_Home,Category_Add,Category_Edit,Master_Home,Master_Add,Master_Edit,Autosuggest
from . import views
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('brand-name',Brand_Details.as_view(),name="brand-name"),
    path('brand-add',Brand_Add.as_view(),name="brand-add"),
    path('brand-edit/<int:id>',Brand_Edit.as_view(),name="brand-edit"),
    path('size-home',Size_Home.as_view(),name="size-home"),
    # path('size-add',Size_Add.as_view(),name="size-add"),
    path('size-edit/<int:id>/',Size_Edit.as_view(),name="size-edit"),
    path('color-home',Color_Home.as_view(),name="color-home"),
    path('color-add',Color_Add.as_view(),name="color-add"),
    path('color-edit/<int:id>/',Color_Edit.as_view(),name="color-edit"),
    path('category-home',Category_Home.as_view(),name="category-home"),
    path('category-add',Category_Add.as_view(),name="category-add"),
    path('category-edit/<int:id>/',Category_Edit.as_view(),name="category-edit"),
    path('master-home',Master_Home.as_view(),name="master-home"),
    # path('new',Master_Home.as_view(),name="new"),
    path('master-add',Master_Add.as_view(),name="master-add"),
    path('master-edit/<int:masterid>/',Master_Edit.as_view(),name="master-edit"),
    path('autosuggest/',Autosuggest.as_view(), name="autosuggest"),
    # path('email',Email_Fun.as_view(),name="email"),
    # path('master-home/<int:masterid>/',Master_Filter.as_view(),name="master-home"),
    path('newses',views.setsession, name="newses"),
    path('getsess',views.getsession, name="getsess"),
    path('dellses',views.dellsession, name="dellses"),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
