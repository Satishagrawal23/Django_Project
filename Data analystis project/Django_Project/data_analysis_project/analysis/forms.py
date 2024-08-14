from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV file', widget=forms.FileInput(attrs={'class': 'form-control'}))
