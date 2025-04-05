from rest_framework.views import APIView

from rest_framework import viewsets 
from .models import Profile, Transaction, Category
from .serializers import ProfileSerializer, TransactionSerializer, CategorySerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .models import Transaction


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios autenticados puedan acceder

    def get_queryset(self):
        """
        Filtra las transacciones para devolver solo las del usuario autenticado.
        """
        user = self.request.user  # Obtiene el usuario autenticado
        return Transaction.objects.filter(user=user)  # Devuelve las transacciones del usuario autenticado
    
    def retrieve(self, request, *args, **kwargs):
        """
        Permite obtener los detalles de una transacción específica.
        """
        # Obtiene el objeto de la transacción según el ID
        return super().retrieve(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """
        Guarda una nueva transacción para el usuario autenticado.
        """
        serializer.save(user=self.request.user)  # Asigna el usuario autenticado a la transacción

    def perform_update(self, serializer):
        """
        Actualiza una transacción existente.
        """
        serializer.save()

    def perform_destroy(self, serializer):
        """
        Elimina una transacción existente."""
        serializer.delete()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Clase para registrar usuarios
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "Todos los campos son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "El nombre de usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)


# Clase para login de usuarios
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise AuthenticationFailed('Nombre de usuario y contraseña son requeridos')

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Credenciales incorrectas')

        # Crear un token JWT para el usuario
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'access_token': access_token
        })