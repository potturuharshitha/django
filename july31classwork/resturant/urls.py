from django.urls import path
from resturant import views
urlpatterns = [
    path('food',views.func2,name='frest'),
    path('additem',views.insert_data,name='spfood')
]
