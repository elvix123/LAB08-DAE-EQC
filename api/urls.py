from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()



urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('producto',views.ProductoView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    
]
