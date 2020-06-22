from django import forms
from .models import Order


# --------------------------------------------------------- ORDER FORM
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # --- Custom __init__ method
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True   # Sets autofocus to full name field
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:                         # If field is required...
                    placeholder = f'{placeholders[field]} *'            # ... adds a star to placeholder
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder    # Sets placeholder values to dict above
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'    # Adds CSS class for styling
            self.fields[field].label = False                                # Removes field labels
