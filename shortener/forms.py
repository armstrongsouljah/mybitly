from django import forms
from .models import MyBitlyUrl
from .validators import validate_url, validate_dot_com
class ShortenUrl(forms.ModelForm):
    url = forms.CharField(label="", validators=[validate_url ],
           widget=forms.TextInput(attrs={
                   'placeholder':'some long url',
                   'class':'form-control',
          })
)


    # def clean_url(self):
        # url = self.cleaned_data['url']
        # url_validator = URLValidator()
        
        # try:
        #    url_validator(url)
        # except:
            # raise forms.ValidationError("Invalid url, use something like http://www.example.com")
        # return url
    
    class Meta:
        model = MyBitlyUrl
        fields = ['url','active']
