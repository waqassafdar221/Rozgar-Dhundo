
from django import forms
from uploadapp.models import Uploads


class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Uploads
        fields = "__all__"
