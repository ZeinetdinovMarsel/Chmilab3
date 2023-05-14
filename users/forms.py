from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Емайл',
            
        }


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio','profile_pic']
        labels = {
            'bio': 'Информация',
            'profile_pic': 'Фото профиля',
            
        }
