from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# itemsSerializer

from .models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"

# invoice 
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"