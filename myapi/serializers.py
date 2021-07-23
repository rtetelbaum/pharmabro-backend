from rest_framework import serializers

from .models import Ingredient, Medication, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')

class MedicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Medication
		fields = ('name', 'user')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ingredient
		fields = ('name', 'aisle', 'shelf', 'column', 'row') 