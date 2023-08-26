from locale import format_string
import django.forms
from Examapp.models import *

class Signup(django.forms.Form):
    fname=django.forms.CharField()
    lname=django.forms.CharField()
    uname=django.forms.EmailField()
    password=django.forms.CharField(widget=django.forms.PasswordInput())
    contact=django.forms.IntegerField()
    
