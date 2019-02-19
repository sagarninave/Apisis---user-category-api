from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import *
from . serializers import *

# Create your views here.
class GetPostUser(APIView):  #################################### user get/post class
	class UserSerializer(serializers.ModelSerializer):
		class Meta:
			model = User
			fields = ('first_name', 'last_name', 'email','phone')

	def post(self, request): #################################### create user post 
		first_name = request.data.get("first_name")
		last_name = request.data.get("last_name")
		email = request.data.get("email")
		phone = request.data.get("phone")

		user = User()
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.phone = phone
		user.save()
		return Response({"status": True, "user": UserSerializer(user).data})

	def get(self, request, *args, **kwargs):   #################################### get all user
		users = User.objects.all()
		return Response({"status": True,"users": UserSerializer(users, many = True).data})

class GetSingleUser(APIView):#################################################### get single user class
	class GetSingleUserSerializer(serializers.ModelSerializer):
		class Meta:
			model = User
			fields = 'id'

	def get(self, request, *args, **kwargs): #################################### get single user with input id in url
		user_id = kwargs.get('id')
		user_data = User.objects.filter(id=user_id).all()
		return Response({'status':True, "users":UserSerializer(user_data, many=True).data})

class GetPostCategory(APIView):  #################################### category get/post class
	class GetPostCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Category
			fields = ('category_name','description')

	def post(self, request): #################################### category get
		category_name1 = request.data.get('category_name')
		description1 = request.data.get('description')

		category = Category()
		category.category_name = category_name1
		category.description = description1
		category.save()
		return Response({'status':True, 'category':CategorySerializer(category).data})

	def get(self, request, *args, **kwargs): #################################### get all category method 
		category = Category.objects.all() 
		return Response({"status":True, "category":CategorySerializer(category, many=True).data})


class GetSingleCategory(APIView): #################################### get single category class 
	class GetSingleCatagorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Category
			fields = ('id')

	def get(self, request, *args, **kwargs): #################################### get single category method
		category_id = kwargs.get('id')
		category_data = Category.objects.filter(id=category_id)
		return Response({"status":True, "category list":CategorySerializer(category_data, many=True).data})

class GetPostUserCategory(APIView): #################################### user category get/post class
	class GetPostUserCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = UserCategory
			fields = ('user', 'category')

	def post(self, request): #################################### user category post method
		user_id = request.data.get('user')
		category_id = request.data.get('category')

		userdata = User.objects.filter(id=user_id).first()
		if userdata is not None:
			
			categorydata = Category.objects.filter(id=category_id).first()
			if categorydata is not None:

				usercategory = UserCategory()
				usercategory.user_id = user_id
				usercategory.category_id = category_id
				usercategory.save()

		return Response({'status':True, 'usercategory':UserCategorySerializer(usercategory).data})

	def get(self, request, *args, **kwargs): #################################### get all user category method
		usercategory = UserCategory.objects.all()
		return Response({"status":True, "usercategory":UserCategorySerializer(usercategory, many=True).data})

class GetSingleUserCategory(APIView): ############################# user single user category by id in url class
	class GetSingleUserCategory(serializers.ModelSerializer):
		class Meta:
			model = UserCategory
			fields = ("id")
	def get(self, request, *args, **kwargs): ####################### get single user inputed by category id in url (class)
		usercategory_id = kwargs.get("id")
		usercategory_data = UserCategory.objects.filter(id=usercategory_id)
		return Response({"status":True, "User Category":UserCategorySerializer(usercategory_data, many=True).data})

class CategoryHasUsers(APIView): ############### get enrolled users in category inputed by category id in url (class)
	class CategoryHasUsersSerializer(serializers.ModelSerializer):
		class Meta:
			model = UserCategory
			field = ('category')

	def get(self, request, *args, **kwargs): ## get enrolled users in category inputed by category id in url (method)
		category_id = kwargs.get('id')

		usercategory = UserCategory.objects.filter(category=category_id).all()
		if usercategory is not None:
			users_list = []
			for x in usercategory:
				user_json = {}
				usercourse = User.objects.filter(id=x.user.id).first()

				user_json["id"] = usercourse.id
				user_json["first_name"] = usercourse.first_name
				users_list.append(user_json)

			return Response({"status": True,"enrolled user": users_list})

class UserHasCategory(APIView): ####### get user enrolled in many category inputed by user id (class)
	class UserHasCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = User
			field = ('id')
	def get(self, request, *args, **kwargs): ####### get user enrolled in many category inputed by user id (method)
		user_id = kwargs.get('id')
		user = User.objects.filter(id=user_id).first()
		if user is not None:
				user_category = UserCategory.objects.filter(user=user_id).all()
		return Response({"status": True,"user having categories": UserCategorySerializer(user_category, many = True).data})

class GetPostSubCategory(APIView): ############################# post sub category class
	class PostSubCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = SubCategory
			fields = ('sub_category_name', 'description', 'category')

	def post(self, request):  ####################################### post sub category method
		sub_category_name = request.data.get('sub_category_name')
		description = request.data.get('description')
		category = request.data.get('category')

		category_data = Category.objects.filter(id=category).first()
		if category_data is not None:
			sub_category = SubCategory()
			sub_category.sub_category_name = sub_category_name
			sub_category.description = description
			sub_category.category_id = category
			sub_category.save()

		return Response({"status":True, "sub_category":SubCategorySerializer(sub_category).data})

	def get(self, request, *args, **kwargs): ############################# get all sub category method
		sub_category = SubCategory.objects.all()
		return Response({"status":True, "sub category":SubCategorySerializer(sub_category, many=True).data})

class GetSingleSubCategory(APIView): ############################# get single sub category class
	class GetPostSingleCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = SubCategory
			fields = ('id')
	def get(self, request, *args, **kwargs): ############################# get all sub category method
		sub_category_id = kwargs.get('id')
		sub_category_data = SubCategory.objects.filter(id=sub_category_id).first()
		return Response({"status":True, "sub category data":SubCategorySerializer(sub_category_data).data})

class GetAllSubCategoryUnderParticularCategory(APIView): ###### get all sub categories included in particular category (class)
	class GetAllSubCategoryUnderParticularCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Category
			fields = ('id')
	def get(self, request, *args, **kwargs): ###### get all sub categories included in particular category (method)
		category_id = kwargs.get('id')
		category_data = Category.objects.first()
		if category_data is not None:
			sub_category_data = SubCategory.objects.filter(category=category_id).all()

		return Response({"status":True, "sub category data":SubCategorySerializer(sub_category_data, many=True).data})
	
class GetPostItem(APIView): ############################## get/post item (class)
	class GetPostItemSerializes(serializers.ModelSerializer):
		class Meta:
			model  = Item
			fields = ('item_name', 'description', 'sub_category')

	def post(self, request): ############################## post single item (class)
		item_name = request.data.get('item_name')
		description = request.data.get('description')
		sub_category = request.data.get('sub_category')

		sub_category_data = SubCategory.objects.filter(id=sub_category).first()
		if sub_category_data is not None: 
			item = Item()
			item.item_name = item_name
			item.description = description
			item.sub_category_id = sub_category
			item.save()
		return Response({'status':True, 'item': ItemSerializer(item).data})

	def get(self, request, *args, **kwargs): ############################## get all item (method)
		item_data = Item.objects.all()
		return Response({'status':True, 'item':ItemSerializer(item_data, many=True).data})

class GetSingleItem(APIView): ############################## get single item inputed by id method
	class GetSingleItemSerializer(serializers.ModelSerializer):
		class Meta:
			model = Item
			fields = ('id')
	def get(self, request, *args, **kwargs): ################ get single item inputed by id (method)
		item_id = kwargs.get('id')
		item_data = Item.objects.filter(id=item_id).first()
		return Response({'status':True, 'item':ItemSerializer(item_data).data})

class GetAllItemUnderSubCategory(APIView): ####### get single item inputed by sub category id (class)
	class GetAllItemUnderSubCategory(serializers.ModelSerializer):
		class Meta:
			model = SubCategory
			fields = ('id')
	def get(self, request, *args, **kwargs): ####### get all item inputed by sub category id (method)
		sub_category_id = kwargs.get('id')
		sub_category_data = SubCategory.objects.first()
		if sub_category_data is not None:
			item_data = Item.objects.filter(sub_category=sub_category_id).all()
		return Response({'status':True, 'All Item':ItemSerializer(item_data, many=True).data})

class GetSubCategoryAndItemUnderCategory(APIView): ###### get sub category anditemunder category (class)
	class GetSubCategoryAndItemUnderCategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Category
			fields = ('id')
	def get(self, request, *args, **kwargs): ###### get sub category and item under category (method)
		category_id = kwargs.get('id')
		category_data = Category.objects.filter(id = category_id).first()
		if category_data is not None:
			sub_category = SubCategory.objects.filter(category=category_id).all()

			subcat_list = []
			for sub_cat in sub_category:

				sub_cat_json = {}
				sub_cat_json["id"] = sub_cat.id
				sub_cat_json["sub category name"] = sub_cat.sub_category_name
				sub_cat_json["description"] = sub_cat.description
				sub_cat_json["category"] = sub_cat.category.id

 				item = Item.objects.filter(sub_category=sub_cat.id).all()
				item_list = []
				for x in item:
					item_json = {}
					item_json["id"] = x.id
					item_json["item_name"] = x.item_name
					item_json["description"] = x.description
					item_json["sub_category"] = x.sub_category.id
					item_list.append(item_json)
				sub_cat_json["items"] = item_list

				subcat_list.append(sub_cat_json)

		return Response({"status": True,"category data": subcat_list})

class GetCategorySubCategoryItemUnderUser(APIView): #### get category, sub category, item of user (class) 
	class GetCategorySubCategoryItemUnderUserSerializer(serializers.ModelSerializer):
		class Meta:
			model = User
			field = ('id')
	def get(self, request, *args, **kwargs): #### get category, sub category, item of user (method)
		user_id = kwargs.get('id')
		user_data = User.objects.filter(id=user_id).first()

		if user_data is not None:
			category = UserCategory.objects.filter(user=user_id).all()
			category_list = []

			for c in category:
				category_json = {}
				category_json['category id'] = c.category.id
				category_json['category name'] = c.category.category_name
				category_json['description'] = c.category.description 
				category_json['user id'] = c.user.id
				category_json['user name'] = c.user.first_name + " " + c.user.last_name 
				

				sub_category = SubCategory.objects.filter(category=c.category.id).all()

				sub_category_list = []
				for sub_cat in sub_category:

					sub_category_json = {}
					sub_category_json["sub category id"] = sub_cat.id
					sub_category_json["sub category name"] = sub_cat.sub_category_name
					sub_category_json["description"] = sub_cat.description
					#sub_category_json["category id"] = sub_cat.category.id

					item = Item.objects.filter(sub_category=sub_cat.id).all()
					item_list = []
					for x in item:
						item_json = {}
						item_json["id"] = x.id
						item_json["item_name"] = x.item_name
						item_json["description"] = x.description
						#item_json["sub_category"] = x.sub_category.id
						item_list.append(item_json)

					sub_category_json['item list'] = item_list
					sub_category_list.append(sub_category_json)

				category_json['sub category'] = sub_category_list
				category_list.append(category_json)

		return Response({'status':True, 'User Data':category_list})