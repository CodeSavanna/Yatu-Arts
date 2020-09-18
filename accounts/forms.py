from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Username or password incorrect")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Username or password incorrect")
        elif user is None:
            pass
        else:
            return password


class RegistrationForm(forms.ModelForm):
    first_name      = forms.CharField()
    last_name       = forms.CharField()
    email           = forms.EmailField(label="Email")
    password        = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2       = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Password does not match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("email already in use")
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user