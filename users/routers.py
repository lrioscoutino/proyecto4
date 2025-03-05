from rest_framework import routers
from users.viewsets import CustomerViewset

router = routers.DefaultRouter()

router.register('customers', CustomerViewset),