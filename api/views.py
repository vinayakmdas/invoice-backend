from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User Registered Successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import User

@api_view(["POST"])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = User.objects.get(
            username=username,
            password=password
        )

        if not user.is_approved:
            return Response({
                "status": False,
                "message": "Waiting for Admin Approval"
            })

        return Response({
            "status": True,
            "message": "Login Success",
            "user_id": user.id,
            "name": user.name,
            "role": user.role
        })

    except User.DoesNotExist:

        return Response({
            "status": False,
            "message": "Invalid Username or Password"
        })   

# get all user 
@api_view(["GET"])
def get_users(request):

    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)  

    # aprove user data 
@api_view(["PUT"])
def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        print("USER ID:", user.id)
        print("BEFORE:", user.is_approved)

        user.is_approved = True
        user.save()

        user.refresh_from_db()

        print("AFTER:", user.is_approved)

        return Response({
            "status": True,
            "message": "User Approved Successfully",
            "approved": user.is_approved
        })

    except User.DoesNotExist:
        return Response({
            "status": False,
            "message": "User Not Found"
        })

     #   delete user

@api_view(["DELETE"])
def delete_user(request, user_id):

    try:

        user = User.objects.get(id=user_id)

        user.delete()

        return Response({
            "status": True,
            "message": "User Deleted Successfully"
        })

    except User.DoesNotExist:

        return Response({
            "status": False,
            "message": "User Not Found"
        })  

                #  items post 

from .models import Item
from .serializers import ItemSerializer


@api_view(["POST"])
def add_item(request):

    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():

        item = serializer.save()

        return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# get items  
@api_view(["GET"])
def get_items(request):

    items = Item.objects.all()

    serializer = ItemSerializer(
        items,
        many=True
    )

    return Response(serializer.data)        


# delete  items

@api_view(["DELETE"])
def delete_item(request, item_id):

    try:

        item = Item.objects.get(id=item_id)

        item.delete()

        return Response({
            "status": True,
            "message": "Item Deleted Successfully"
        })

    except Item.DoesNotExist:

        return Response({
            "status": False,
            "message": "Item Not Found"
        })   

        #  invoice 
from .models import Invoice
from .serializers import InvoiceSerializer


@api_view(["POST"])
def add_invoice(request):

    serializer = InvoiceSerializer(data=request.data)

    if serializer.is_valid():

        invoice = serializer.save()

        return Response(InvoiceSerializer(invoice).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# view

@api_view(["GET"])
def get_invoices(request):

    invoices = Invoice.objects.all()

    serializer = InvoiceSerializer(
        invoices,
        many=True
    )

    return Response(serializer.data)


    # delete 
@api_view(["DELETE"])
def delete_invoice(request, invoice_id):

    try:

        invoice = Invoice.objects.get(id=invoice_id)

        invoice.delete()

        return Response({
            "status": True,
            "message": "Invoice Deleted Successfully"
        })

    except Invoice.DoesNotExist:

        return Response({
            "status": False,
            "message": "Invoice Not Found"
        })    