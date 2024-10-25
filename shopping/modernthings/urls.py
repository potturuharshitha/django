from django ulrs import path
from modernthings import path
urlpatterns = [
    path('mobiles/<int:id>',views.msearch,name='ms')
    path('laptops/<int:id>',views.lsearch,name='ls')
    path('airpods/<int:id>',views.asearch,name='as')
]