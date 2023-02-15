from django import forms
from .models import Blog

banned_email_list = ['test@hotmail.com','berkcan_karabulut@hotmail.com']

#Normal Form
class IletisimForm(forms.Form):
    isim = forms.CharField(max_length=50, label='İsim', required=False)
    soyisim = forms.CharField(max_length=50, label='Soyisim', required=False)
    email = forms.EmailField(max_length=50, label='Email', required=True)
    email2 = forms.EmailField(max_length=50, label='Email Kontrol', required=True)
    icerik = forms.CharField(widget=forms.Textarea({'class':'form-control','style':'height:200px;'}), max_length=1000, label='İçerik')

    #Kalıtım aldığı constructor class ı
    def __init__(self, *args,**kwargs):
        super(IletisimForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field != 'icerik':
                self.fields[field].widget.attrs={'class':'form-control'}
        #self.fields['icerik'].widget = forms.Textarea(attrs={'class':'form-control'})

    def clean_isim(self):
        isim = self.cleaned_data.get('isim')
        if isim == 'berkcan':
            raise forms.ValidationError('Lütfen berkcan dışında bir kullanıcı giriniz.')
        return isim
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('Lütfen banlanmamış bir email adresi giriniz.')
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            self.add_error('email','Emailler eşleşmedi') #Belirtilen alanda hata gösterilir
            self.add_error('email2','Emailler eşleşmedi')
            raise forms.ValidationError('Emailler eşleşmedi') #Form için hata yazdırmaya yarar

#Model Form
class BlogForm(forms.ModelForm):
    class Meta: #Meta class ı form ile alakalı ayarlar için (settings gibi..)
        model = Blog
        fields = ['title','icerik','kategoriler']
    
    def __init__(self, *args,**kwargs):
        super(BlogForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['icerik'].widget.attrs[r'rows']=10
