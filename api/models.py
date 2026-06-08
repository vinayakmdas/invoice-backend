from django.db import models

# User
class User(models.Model):

    name = models.CharField(max_length=100)

    username = models.CharField(
        max_length=50,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=10,
        unique=True
    )

    password = models.CharField(
        max_length=255
    )

    is_approved = models.BooleanField(
        default=False
    )

    role = models.CharField(
        max_length=20,
        default="user"
    )

    def __str__(self):
        return self.username


# Item
class Item(models.Model):

    ITEM_TYPES = (
        ('Goods', 'Goods'),
        ('Service', 'Service'),
    )

    name = models.CharField(max_length=100)

    item_type = models.CharField(
        max_length=20,
        choices=ITEM_TYPES
    )

    hsn_sac = models.CharField(
        max_length=6,
        unique=True
    )

    taxable = models.BooleanField(
        default=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name



#  invoice
class Invoice(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=10)

    address = models.TextField()

    date = models.DateField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name