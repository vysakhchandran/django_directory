from django import forms
from .models import Directory

class DirectoryForm(forms.ModelForm):
    class Meta:
    	model=Directory
    	fields=['name','number']


    def clean_number(self):
        data = self.cleaned_data['number']
        print data
        if len(data) <10:
            raise forms.ValidationError("Invalid phone number ")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
       