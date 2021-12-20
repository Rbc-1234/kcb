# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Brand,Size,BrandColor,Category,Master_Page
from django.views import View
from .forms import BrandForm,SizeForm,ColorForm,CategoryForm,MasterForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
import os
from django.db.models import Q
from django.views.generic import DetailView
from django.http import JsonResponse
from django.core.mail import send_mail




class Brand_Details(View):
    def get(self,request):
        kc=Brand.objects.all().order_by('-id')
        paginator= Paginator(kc,6 )
        page_number=request.GET.get('page')
        pre = paginator.get_page(page_number)
        return render(request,'home/brand-name.html',{'rk':pre})

class Brand_Add(View):
    def get(self,request):
        cr=BrandForm()
        return render(request,'home/brand-add.html',{'pr':cr})
        
    def post(self,request):
        kr=BrandForm(request.POST, request.FILES)
        if request.method =="POST":
            status=request.POST.get('status')
            searchst=Brand.objects.filter(status=status)
        if kr.is_valid():
            kr.save()
            return redirect('/brand-name')
        else:
            brandname = request.POST['brandname']
            status=request.POST['status']
            obj = Brand(brandname=brandname)
            py=BrandForm(request.POST,request.FILES)
            return render(request,'home/brand-add.html',{'nr':py, 'qr':obj})
            
class Brand_Edit(View):
    def get(self,request,id):
        pr=Brand.objects.get(id=id)
        py=BrandForm(instance=pr)
        return render(request, 'home/brand-edit.html',{'rr':pr})
    def post(self,request,id):
        pr=Brand.objects.get(id=id)
        if len(request.FILES) !=0:
            if len(pr.logo)>0:
                os.remove(pr.logo.path)
                pr.logo=request.FILES['logo']
        py=BrandForm(request.POST,instance=pr)
        if py.is_valid():
            py.save()
            return redirect('/brand-name')
        else:
            return render(request, 'home/brand-edit.html',{'kk':py, 'rr':pr})
    

class Size_Home(View):
    def get(self,request):
        rc=Size.objects.all()
        return render(request,'home/size-home.html',{'kp':rc})


class Size_Edit(View):

   
    def get(self,request,id):
       
        if(id==0):
            rp=SizeForm()
            return render(request,'home/size-edit.html')
        else:
            pt=Size.objects.get(id=id)
            cp=SizeForm(instance=pt)
            return render(request,'home/size-edit.html',{'kc':pt,'rt':cp})

    def post(self,request,id):
        if(id==0):
            rp=SizeForm(request.POST)
            if rp.is_valid():
                rp.save()
                return redirect('/size-home')
            else:
                return render(request,'home/size-edit.html',{'rc':rp})
        else:
            pt=Size.objects.get(id=id)
            cp=SizeForm(request.POST,instance=pt)
            if cp.is_valid():
                cp.save()
                return redirect('/size-home')
            else:
                return render(request,'home/size-edit.html',{'rt':cp})

    

class Color_Home(View):
    def get(self,request):
        tc=BrandColor.objects.all()
        return render(request,'home/color-home.html',{'tk':tc})

class Color_Add(View):
    def get(self,request):
        rp=ColorForm()
        return render(request,'home/color-add.html')
    
    def post(self,request):
        rp=ColorForm(request.POST)
        if rp.is_valid():
            rp.save()
            return redirect('/color-home')
        else:
            return render(request,'home/color-add.html',{'rc':rp})

class Color_Edit(View):
    def get(self,request,id):
        pt=BrandColor.objects.get(id=id)
        cp=ColorForm(instance=pt)
        return render(request,'home/color-edit.html',{'kc':pt,'rt':cp})
        
    def post(self,request,id):
        pt=BrandColor.objects.get(id=id)
        cp=ColorForm(request.POST,instance=pt)
        if cp.is_valid():
            cp.save()
            return redirect('/color-home')
        else:
            return render(request,'home/color-edit.html',{'rt':cp})

class Category_Home(View):
    def get(self,request):
        tc=Category.objects.all()
        return render(request,'home/category-home.html',{'tk':tc})

class Category_Add(View):
    def get(self,request):
        rp=CategoryForm()
        return render(request,'home/category-add.html')
    
    def post(self,request):
        rp=CategoryForm(request.POST)
        if rp.is_valid():
            rp.save()
            return redirect('/category-home')
        else:
            return render(request,'home/category-add.html',{'rc':rp})

class Category_Edit(View):
    def get(self,request,id):
        pt=Category.objects.get(id=id)
        cp=CategoryForm(instance=pt)
        return render(request,'home/category-edit.html',{'kc':pt,'rt':cp})
        
    def post(self,request,id):
        pt=Category.objects.get(id=id)
        cp=CategoryForm(request.POST,instance=pt)
        if cp.is_valid():
            cp.save()
            return redirect('/category-home')
        else:
            return render(request,'home/category-edit.html',{'rt':cp})

class Master_Home(View):
    def get(self,request):
        pre=Master_Page.objects.all().order_by('-masterid')
        ap=Brand.objects.all()
        st=''
        rt=''
        if request.GET.get('searchname'):
            st=request.GET.get('searchname')
        if request.GET.get('searchh'):
            rt=request.GET.get('searchh')
            rt=int(rt)
            
        if ((rt!='')and(st!='')):
            pre=Master_Page.objects.filter(name__icontains=st,brandname=rt)
            paginator= Paginator(pre,4 )
            page_number=request.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(request,'home/master-home.html',{'rk':pre,'pa':ap,'st':st,'rt':rt})
        elif rt!='':
            pre=Master_Page.objects.filter(brandname=rt)
            paginator= Paginator(pre,4 )
            page_number=request.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(request,'home/master-home.html',{'rk':pre,'pa':ap,'st':st,'rt':rt})
        elif st!='':
                pre=Master_Page.objects.filter(name__icontains=st)
                paginator= Paginator(pre,4 )
                page_number=request.GET.get('page')
                pre = paginator.get_page(page_number)
                return render(request,'home/master-home.html',{'rk':pre,'pa':ap,'st':st,'rt':rt})
        else:
            pre=Master_Page.objects.all()
            ap=Brand.objects.all()
            paginator= Paginator(pre,4 )
            page_number=request.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(request,'home/master-home.html',{'rk':pre,'pa':ap,'st':st,'rt':rt})
    

# class PictureView()
#         # rt=request.GET.get('searchh')
#         # st=request.GET.get('searchname')

        
#         # ap=Brand.objects.all()

#         # if((st !='' and st is not None) and (rt !='' and rt is not None)):
        #     pre=Master_Page.objects.filter(name__icontains=st,brandname=rt).order_by('-masterid')
           

        # elif st !='' and st is not None:
        #     pre=Master_Page.objects.filter(name__icontains=st).order_by('-masterid')
            
        # elif rt !='' and rt is not None:
        #     pre=Master_Page.objects.filter(brandname=rt).order_by('-masterid')
           
        # else:
        #     pre=Master_Page.objects.all().order_by('-masterid')
            
            
        # ap=Brand.objects.all()
        # paginator= Paginator(pre,2 )
        # page_number=request.GET.get('page')
        # pre = paginator.get_page(page_number)
        # return render(request,'home/master-home.html',{'rk':pre,'pa':ap}) 

class Master_Add(View):
    def get(self,request):
        rp=MasterForm()
        kc=Size.objects.all()
        rt=Brand.objects.all()
        kw=Category.objects.all()
        return render(request,'home/master-add.html',{'rr':kc,'cr':rt,'ir':kw})
        
    
    def post(self,request):
        rp=MasterForm(request.POST,request.FILES)
        if request.method =="POST":
            masterstatus=request.POST.get('masterstatus')
            searchst=Master_Page.objects.filter(masterstatus=masterstatus)
        if rp.is_valid():
            rp.save()
            return redirect('/master-home')
        else:
            name = request.POST['name']
            discription=request.POST['discription']
            price=request.POST['price']
            brandsize=request.POST['brandsize']
            brandname=request.POST['brandname']
            brandcategory=request.POST['brandcategory']
            obj = Master_Page(name=name,discription=discription,price=price)
            py=MasterForm(request.POST,request.FILES)
            return render(request,'home/master-add.html',{'rc':rp, 'ar':obj})

class Master_Edit(View):
    def get(self,request,masterid):
        jr=Master_Page.objects.get(masterid=masterid)
        pq=MasterForm(instance=jr)
        kc=Size.objects.all()
        rt=Brand.objects.all()
        kw=Category.objects.all()
        return render(request,'home/master-edit.html',{'rr':kc,'cr':rt,'ir':kw,'ii':pq,'xr':jr})
        
    def post(self,request,masterid):
        rt=Master_Page.objects.get(masterid=masterid)
        if len(request.FILES) !=0:
            if len(rt.document)>0:
                os.remove(rt.document.path)
                rt.document=request.FILES['document']
        kc=MasterForm(request.POST,instance=rt)
        if kc.is_valid():
            kc.save()
            return redirect('/master-home')
        else:
            return render(request,'home/master-edit.html',{'pr':kc})

class Autosuggest(View):
    def get(self,request):
        query_original=request.GET.get('term')
        queryset=Master_Page.objects.filter(name__icontains=query_original)
        mylist=[]
        mylist +=[x.name for x in queryset]
        return JsonResponse(mylist, safe=False)
    

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lastname']= 'sharma'
    return render(request,'home/newses.html')

def getsession(request):
    # name= request.session['name']
    name=request.session.get('name')
    lastname=request.session.get('lastname')
    return render(request,'home/getsess.html',{'name':name,'lastname':lastname})

def dellsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'home/dellses.html')


# class Email_Fun(View):
#     def post(self,request):
#         if request.method=="POST":
#             email=request.POST['email']
#             message=request.POST['message']
#             print('email')
#             send_mail('test',message,settings.EMAIL_HOST_USER,[email],fail_silently=False,)
#         return render(request,'home/email.html')




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
