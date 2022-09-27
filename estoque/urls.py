from django.urls import path, include
from . views import add_produto, produto

urlpatterns = [
    path('add_produto/', add_produto, name="add_produto"),
    path('produto/<slug:slug>', produto, name="produto")
]
