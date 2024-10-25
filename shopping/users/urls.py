from django urls import path
from shopping import views
urlpatterns = [
    path('users/<int:id>',views.usearch,name=customer)
]