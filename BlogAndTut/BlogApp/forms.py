from django import forms
from BlogApp.models import *
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']



"""class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField( label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
"""

from BlogApp.models import Comment
class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':50}),
        }



from BlogApp.models import Comment_Related_To_Problem
class Comment_Related_To_ProblemForm(forms.ModelForm):

    class Meta:
        model=Comment_Related_To_Problem
        fields=('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':4, 'cols':50}),
        }
