from django import forms

class uploadform(forms.Form):
    iname=forms.CharField(max_length=20)
    iprice=forms.IntegerField()
    file=forms.ImageField()
# Create your models here.
class itembillform(forms.Form):
    iname=forms.CharField(max_length=20)
    iprice=forms.IntegerField()
    qty=forms.IntegerField()