from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail, create_product, ProductUpdate, ProductDelete


urlpatterns = [
   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('create/', create_product, name='product_create'),
   path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]


