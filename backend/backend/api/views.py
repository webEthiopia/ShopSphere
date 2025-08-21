from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)