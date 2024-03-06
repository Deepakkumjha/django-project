from django import forms

class usersForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()

class usersForm2(forms.Form):
    num1=forms.CharField()

class markforms(forms.Form):
    sub_1=forms.CharField()
    sub_2=forms.CharField()
    sub_3=forms.CharField()
    sub_4=forms.CharField()
    sub_5=forms.CharField()
    

