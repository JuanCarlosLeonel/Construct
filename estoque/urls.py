from django.urls import path, include
from . views import add_produto

urlpatterns = [
    path('add_produto/', add_produto, name="add_produto"),
]
