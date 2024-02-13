from .models import img_up,cust_tab,prod
from django import forms

class CustForm(forms.ModelForm):
     class Meta:

        model =cust_tab

        fields =("name","age",'email',"address")

        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }

class ImgForm(forms.ModelForm):
     class Meta:

        model =img_up

        fields =("name","age","email","address","image","approval")

        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
        
class ProdForm(forms.ModelForm):
    class Meta:
        
        model = prod
        
        fields=("name","qty","weight","certification","price")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'}),
            'weight':forms.NumberInput(attrs={'class':'form-control'}),
            'certification':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }
    
class CartForm(forms.ModelForm):
    class Meta:
        
        model = prod
        
        fields=("name","qty","price")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }