from django import forms

from .models import NewslatterUser, Newslatter


class NewslatterUserSingUpForm(forms.ModelForm):
    class Meta:
        model = NewslatterUser
        fields = ['email']

class NewslatterCreateForm(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = ['name','subject','body','email']