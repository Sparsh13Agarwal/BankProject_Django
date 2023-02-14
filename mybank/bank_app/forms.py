from django import forms


class Signup(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    middle_name = forms.CharField(label='Middle name', max_length=20,required=False)
    last_name = forms.CharField(label='Last name', max_length=20)
    resident_addr = forms.CharField(label='Resident Address',max_length=100)
    office_addr = forms.CharField(label='Office Add',max_length=100)
    phone_no = forms.IntegerField(label='Phone No')
    email = forms.EmailField(label="Email",widget=forms.EmailInput)
    password = forms.CharField(label='Password',min_length=8,max_length=20,widget=forms.PasswordInput)
    repassword = forms.CharField(label='Repassword',min_length=8,max_length=20,widget=forms.PasswordInput)  
    def clean(self):
        cleaned_data = super().clean()
        password_val = cleaned_data['password']
        repassword_val = cleaned_data['repassword']
        phoneno = cleaned_data['phone_no']

        if password_val!= repassword_val:
            if len(str(phoneno))!=10:
                raise forms.ValidationError(' Password Not Matched & Phone number must be of 10 digits')
            raise forms.ValidationError('Password and Repassword not Matched')

             
        if len(str(phoneno))!=10:
            if password_val!= repassword_val:
                raise forms.ValidationError('Phone number must be of 10 digits Password Not Matched')
            raise forms.ValidationError('Phone number must be of 10 digits')

    # changing balance to integer field from charfield
    Balance = forms.IntegerField(label='Balance',max_value=10000000,min_value=0)

class Transfor(forms.Form):
    transfer_to = forms.CharField(label="Account Number")
    amount = forms.CharField(label='Amount')
 
class Login_form(forms.Form):
    cust_id = forms.CharField(label='Customer Id')
    password = forms.CharField(label='Password',min_length=8,max_length=20,widget=forms.PasswordInput)

class Customer_Contactus(forms.Form):
    name = forms.CharField(label='Name',max_length=20,widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}))
    email = forms.EmailField(label='Email',widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}))
    message = forms.CharField(label='Message',max_length=250,widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}))


