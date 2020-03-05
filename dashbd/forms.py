from django import forms


class NewCustomer(forms.Form):
    name = forms.CharField(label="Enter Customer Name", max_length=50)
    email = forms.EmailField(label="E-Mail")
    phone = forms.IntegerField(label="Phone Number")


class PipedriveKey(forms.Form):
    key = forms.CharField(label="Enter Pipedrive API Key", max_length=50)