from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name= "ShopHome"),
    path('about/', views.about , name= "About"),
    path('contact/', views.contact, name= "Contact Us"),
    path('tracker/', views.tracker, name= "Tracking Status"),
    path('checkout/', views.checkout, name= "Cheak Out"),
    path('search/', views.search, name= "Seach"),
    path('products/<int:myid>', views.products, name= "ProductView"),
    path('handlerequest/', views.handlerequest, name= "HandleRequest"),
]