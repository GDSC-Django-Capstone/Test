from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import EmailInput, PasswordInput, CharField
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class LoginUserForm(AuthenticationForm):
    # email = CharField(widget=EmailInput())
    # password = CharField(widget=PasswordInput())
   
    class Meta:
        model = CustomUser
        fields = ('email','password')
