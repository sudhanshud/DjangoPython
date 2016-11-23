from django import forms
import utils

class CompanyRating(forms.Form):
    """

    """
    def __init__(self, *args, **kwargs):
        super(CompanyRating, self).__init__(*args, **kwargs)
        self.fields['Company_name'] = forms.ChoiceField(
            choices=utils.get_com_names(), widget=forms.Select(attrs={'class' : 'form-control'}) )
        self.fields['Month'] = forms.ChoiceField(
            choices=utils.get_months(), widget=forms.Select(attrs={'class' : 'form-control'}) )

class CrsData(forms.Form):
    """

    """
    def __init__(self, *args, **kwargs):
        super(CrsData, self).__init__(*args, **kwargs)
        self.fields['Company_name'] = forms.ChoiceField(
            choices=utils.get_com_names(), widget=forms.Select(attrs={'class' : 'form-control'}) )