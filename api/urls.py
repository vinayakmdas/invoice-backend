from django.urls import path
from .views import (
    register,
    login,
    get_users,
    approve_user,
    delete_user,
    add_item,
    get_items,
    delete_item,
    add_invoice,
    get_invoices,
    delete_invoice
)

urlpatterns = [
    path("register/", register),
    path("login/", login),

    path("users/", get_users),

    path(
        "approve-user/<int:user_id>/",
        approve_user
    ),

    path(
        "delete-user/<int:user_id>/",
        delete_user
    ),

    path(
        "items/",
         get_items
         
         ),
    path(
        "add-item/",
         add_item
         ),
    path(
        
        "delete-item/<int:item_id>/",
        
         delete_item),

     path(
        "add-invoice/",
         add_invoice
         ),
    path(
        "invoices/", 
        get_invoices
        ),
    path(
        "delete-invoice/<int:invoice_id>/",
         delete_invoice
         ),    
]