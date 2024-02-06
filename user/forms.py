from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    avatar = forms.ImageField(required=True)
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)


class VeryfyForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)
