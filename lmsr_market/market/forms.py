from django import forms
from django.contrib.auth.models import User
from .models import Prediction


NATURAL_CAUSES = 'He will die of Natural causes (Too old)'

class BuySharesForm(forms.Form):
    outcome = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No'), (NATURAL_CAUSES, NATURAL_CAUSES)])
    shares = forms.FloatField(min_value=0.01)

class SellSharesForm(forms.Form):
    outcome = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No'), (NATURAL_CAUSES, NATURAL_CAUSES)])
    shares = forms.FloatField(min_value=0.01)
    

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['stock', 'shares']