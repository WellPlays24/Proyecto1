from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, TransactionViewSet, CategoryViewSet, RegisterView, LoginView

# Crear el enrutador de la API
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Rutas estándar de la API
    path('register/', RegisterView.as_view(), name='register'),  # Ruta para el registro
    path('login/', LoginView.as_view(), name='login'),  # Ruta para el login
]
