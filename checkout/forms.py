from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {                            # Adds placeholders to input fields
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True   # Sets autofocus on full_name field
        for field in self.fields:                                   # Iterates through all fields
            if self.fields[field].required:                         # If field is required...
                placeholder = f'{placeholders[field]} *'            # ... it adds * to the placeholder
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder    # Sets all placeholder attrs to their values
            self.fields[field].widget.attrs['class'] = 'stripe-style-input' # Adds CSS class
            self.fields[field].label = False                        # Removes form field labels
