from django.db import models

# Contact form


class Contact(models.Model):
    """Contact, receive subject from the users """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name