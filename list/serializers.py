from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = '__all__'

class UserCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = UserCategory
		fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = SubCategory
		fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = '__all__'


