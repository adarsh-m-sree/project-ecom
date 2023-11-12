from django.urls import path
from . import views
app_name='shop'


urlpatterns=[
    path('',views.AllProducts,name='AllProducts'),
    path('<slug:cat_slug>/',views.AllProducts,name='product_by_category'),
    path('<slug:cat_slug>/<slug:product_slug>/',views.product_details,name='product_details_by_category'),
]