from django.db import models

CONTACT_CHOICE = (
    ("ORDER QUERY", "ORDER QUERY"),
    ("PAYMENT ISSUE", "PAYMENT ISSUE"),
    ("LOGIN ISSUE", "LOGIN ISSUE"),
    ("GENERAL QUERY", "GENERAL QUERY"),
)


class Contact(models.Model):
    """
    A user contact model for contacting users
    """

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=80, null=True, blank=True)
    query = models.CharField(
        max_length=40, choices=CONTACT_CHOICE, default="GENERAL QUERY"
    )
    comments = models.CharField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.user.username
