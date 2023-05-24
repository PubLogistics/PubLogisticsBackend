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