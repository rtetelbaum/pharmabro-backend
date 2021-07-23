from rest_framework import serializers

from .models import Ingredient, Medication, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

class MedicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Medication
		fields = ('id', 'name', 'user')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ingredient
		fields = ('id', 'name', 'aisle', 'shelf', 'column', 'row', 'medications') 