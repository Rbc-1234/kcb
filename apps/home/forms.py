from .models import Brand,Size,BrandColor,Category,Master_Page
from django import forms
from django import forms


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('brandname','logo','status')
       

class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ('brandsize',)

class ColorForm(forms.ModelForm):

    class Meta:
        model = BrandColor
        fields = ('color',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('brandcategory',)

class MasterForm(forms.ModelForm):

    class Meta:
        model = Master_Page
        fields = ('name','discription','document','brandsize','brandname','brandcategory','price','masterstatus')
        


class ContactForm(forms.Form):                
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
