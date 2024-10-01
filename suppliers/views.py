from django.views import generic
from .models import Suppliers


class SupplierList(generic.ListView):
    """
    A view to show all suppliers.
    """
    model = Suppliers
    queryset = Suppliers.objects.all().order_by('supplier_name')
    template_name = 'suppliers/suppliers.html'
    paginate_by = 6