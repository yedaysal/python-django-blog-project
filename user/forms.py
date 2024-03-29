from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "Kullanıcı Adı")
    password = forms.CharField(max_length = 20, label = "Parola", widget = forms.PasswordInput)
    confirm_pass = forms.CharField(max_length = 20, label = "Parolayı Doğrulayın", widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_pass")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor!")

        else:
            values = {
                "username" : username,
                "password" : password,
            }

            return values


class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola", widget = forms.PasswordInput)