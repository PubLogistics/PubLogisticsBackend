from django import forms
from .models import Company
class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields=('name','abbreviation')
# class CompanyQueryForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields=("id","name","abbreviation")
class CompanyModifyForm(forms.Form):
    name=forms.CharField(max_length=255,required=False)
    abbreviation=forms.CharField(max_length=50,required=False)