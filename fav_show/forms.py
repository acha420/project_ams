from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Shows


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15, required=True)
    name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'mobile', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # use email as username
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['mobile']
            )

            return user
    
    
class ShowForm(forms.ModelForm):
        class Meta:
            model = Shows
            fields = ['title', 'description', 'image', 'watch_link']