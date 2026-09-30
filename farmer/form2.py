from .models import FarmerTraining
from django import forms

class User1(forms.ModelForm):
    class Meta:
        model = FarmerTraining
        fields = ['name','age','contact','taluka','village','district','cropdetails']
        labels = {'name':'Enter Name','age':'Enter age','contact':'Enter Contact','taluka':'Enter Taluka','village':'Enter Village','district':'Enter District','cropdetails':'Enter Cropdetails'}
