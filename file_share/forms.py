# file_share/forms.py
from django import forms

class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=50)
    ID = forms.CharField(max_length=10)
class ShareFileForm(forms.Form):
    user_to_share_with = forms.CharField(label='User Token', max_length=10)
    file = forms.FileField()
class FileForm(forms.Form):
    file = forms.FileField()
