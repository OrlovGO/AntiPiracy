from django import forms


class CodeForm(forms.Form):
    code_field = forms.CharField(widget=forms.Textarea)

# class CodeOutput(forms.Form):
#    code_field_out = forms.CharField(widget=forms.Textarea)
