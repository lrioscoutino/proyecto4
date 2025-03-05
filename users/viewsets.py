from rest_framework import viewsets
from users.seriakizers import CustomerSerializer
from users.models import Customer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer