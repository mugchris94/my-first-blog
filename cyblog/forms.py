from. import models
from django import forms
from django.contrib.auth import (
    
    authenticate,
    login,
    logout,
    get_user_model
)

user= get_user_model()

class UserLoginForm(forms.Form):
    username= forms.CharField(widget= forms.TextInput(

    attrs={
    'class':'form-control',
    'placeholder':'Enter username'
    }
    ))
    password= forms.CharField(widget= forms.PasswordInput(

    attrs={

    'class':'form-control',
    'placeholder':'Enter password'
    }
    ))
    def clean(self):
        username= self.cleaned_data.get('username')
        password= self.cleaned_data.get('password')

        if username and password:
            user= authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("the user is not in database")
            if not user.check_password(password):
                raise forms.ValidationError("the password is not correct")
            if not user.is_active:
                raise forms.ValidationError("the user is not active")
        return super(UserLoginForm,self).clean()
  

class Create_Post(forms.ModelForm):
    title= forms.CharField(required= False,widget= forms.TextInput(
    attrs=
    {
    'class':'form-input'
    }
))
    text= forms.CharField(widget=forms.Textarea(
    attrs= {
        'class':'form-text'

    }
    ))
    class Meta:
        model = models.Post
        fields = ['title','text']

class SearchForm(forms.Form):
        title = forms.CharField(label='', widget= forms.TextInput(
                attrs=
                {

                'class' : 'form-control',
                'placeholder': 'search'
                }
        ))

        def clean_title(self):
            title= self.cleaned_data.get('title')

            db_title= Post.objects.filter(title__icontains = title)
            if not db_title:
                raise forms.ValidationError('i am not seeing it bruhh!')
            else:
                raise forms.ValidationError('u got it man')
            return title

class Create_User(forms.ModelForm):

        username= forms.CharField(widget= forms.TextInput(
            attrs={

                'class':'form-control'
            }


        ))
        email= forms.EmailField(widget= forms.EmailInput(

        attrs={
        'class': 'form-control',
        'placeholder': 'email'

        } ))
        password= forms.CharField( widget= forms.PasswordInput(
        attrs={

        'class':'form-control',
        'placeholder':'password'
        }
        ))
        password_confirm= forms.CharField( widget= forms.PasswordInput(
        attrs={

        'class':'form-control',
        'placeholder':'password_confirm'
        }))


        def clean_username(self):
            username= self.cleaned_data.get('username')
            user_results= User.objects.filter(username_icontains='username')
            len_user=len(username)
            if len_user < 9:
                raise forms.ValidationError("your username is short")

            if user_results.exists():
                raise forms.ValidationError("this user already exists brother")

            return username

            
        def clean_email(self):
            email= self.cleaned_data.get('email')
            if not email.endswith(".@gmail.com"):
                raise forms.ValidationError("this email doesn't apply")
            return email

        def clean_password(self):
            password = self.cleaned_data.get('password')
            pass_char= len(password)
            if pass_char > 7:
                raise forms.ValidationError('too many digits')
            elif pass_char < 7:
                raise forms.ValidationError('less digits')
            return passwd

        def clean_password_confirm(self):
            password_confirm= self.cleaned_data.get('password_confirm')
            password= self.cleaned_data.get('password')
            if password_confirm != password:
                raise forms.ValidationError('Your password is not identical to the previous one')
            return password_confirm
