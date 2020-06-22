from django import forms
from .models import UserProfile


# --------------------------------------------------------- PROFILE FORM
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    # --- Custom __init__ method
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True   # Sets autofocus to phone no field
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:                 # If field is required...
                    placeholder = f'{placeholders[field]} *'    # ... adds a star to placeholder
                else:
                    placeholder = placeholders[field]
                # Sets placeholder values to dict above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds CSS class for styling
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            # Removes field labels
            self.fields[field].label = False
