from rest_framework import serializers

from .models import Ingredient, Medication, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ingredient
		fields = ('id', 'name', 'aisle', 'shelf', 'column', 'row') 

class MedicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Medication
		fields = ('id', 'name', 'user', 'user_id', 'ingredients')
		depth = 1

	user_id = serializers.SerializerMethodField('get_user_id')

	def get_user_id(self, obj):
		return obj.user.id