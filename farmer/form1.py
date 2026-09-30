from .models import ExpertForm
from django import forms

class User(forms.ModelForm):
    class Meta:
        model = ExpertForm
        fields = ['name','phoneno','village','taluka','district','problem']
        labels = {'name':'Enter Name','phoneno':'Enter Phoneno','village':'Enter Village','taluka':'Enter Taluka','district':'Enter District','problem':'Enter Problem'}
