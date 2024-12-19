from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form to create a contact"""

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "phone_number",
            "query",
            "comments",
        ]
