from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('username')
	serializer_class = UserSerializer

# -----

from rest_framework import viewsets

from .serializers import IngredientSerializer
from .models import Ingredient

class IngredientViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all().order_by('name')
	serializer_class = IngredientSerializer

# -----
from rest_framework import viewsets

from .serializers import MedicationSerializer
from .models import Medication

class MedicationViewSet(viewsets.ModelViewSet):
	queryset = Medication.objects.all().order_by('name')
	serializer_class = MedicationSerializer