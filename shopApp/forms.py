from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Утро/день/вечер'}))
    people_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'количество людей'}))
    agree = forms.BooleanField(widget=forms.CheckboxInput(attrs={}))