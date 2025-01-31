from django import forms
import re


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices = [
             ('1', True),
             ('0', False),
         ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices = [
            ('1', True), 
            ('0', False),
            ],
        )
    
    def clean_phone_number(self):
        date = self.cleaned_data.get['phone_number']
        if not date.isdigit():
            raise forms.ValidationError('Телефон должен содержать только цифры')
        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(date):
            raise forms.ValidationError('Телефон должен содержать 10 цифр')    

        return date
    
    
    # firs_name = forms.Charfield(
    #     widge = forms.TextInput(
    #         attrs = {
    #             'class': 'form-control',
    #             'placeholder': 'Введите ваше имя',
    #             }
    #         ),
    # )
    
    # last_name = forms.Charfield(
    #     widge = forms.TextInput(
    #         attrs = {
    #             'class': 'form-control',
    #             'placeholder': 'Введите вашу фамилию',
    #         }
    #     ),
    # )
    
    # phone_number = forms.Charfield(
    #     widge = forms.TextInput(
    #         attrs = {
    #             'class': 'form-control',
    #             'placeholder': 'Введите ваш номер телефона',
    #         }
    #     ),
    # )
    
    # requires_delivery = forms.ChoiseField(
    #     widge = forms.RadioSelect(),
    #     choices = [
    #         ('1', True),
    #         ('0', False),
    #     ],
    #     initial = 0,
    # )
    
    # delivery_address = forms.Charfield(
    #     widge=forms.TextInput(
    #         attrs = {
    #             'class': 'form-control',
    #             'id': 'delivery_address',
    #             'rows': 2,
    #             'placeholder': 'Введите ваш адрес доставки',
    #         }   
    #     ),
    #     required = False,
    # )
    
    # payment_on_get = forms.ChoiseField(
    #     widget = forms.RadioSelect(),
    #     choices = [
    #         ('1', True),
    #         ('0', False),
    #     ],
    #     initial = 'card',
    # ) 
    