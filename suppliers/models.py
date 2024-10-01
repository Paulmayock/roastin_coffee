from django.db import models

class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=100, null=False, blank=False)
    supplier_bio = models.TextField(null=False)
    supplier_image = models.ImageField(null=True, blank=True)
    supplier_website = models.TextField(null=False)

    def __str__(self):
        return self.supplier_name

    class Meta:
        db_table = 'Suppliers'
        # Add verbose name
        verbose_name = 'Supplier'
