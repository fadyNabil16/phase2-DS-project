from django.urls import path, include
from .views import *

urlpatterns = [
    path('history', History, name='history'),
    path('deleteitem', DeleteItem, name='deleteitem'),
    path('additem', AddItem, name='additem'),
    path('search', Search, name='search'),
    path('edititem', EditItem, name='edititem'),
    path('login', Login, name='login'),
    path('signup', Signup, name='signup'),
    path('cash', Cash, name='cash'),
    path('addcash', AddCash, name='addcash'),
    path('help', Help, name='help'),
    path('buyitem', BuyItem, name='buyitem'),
    path('allitems', AllItems, name='allitems'),
]
