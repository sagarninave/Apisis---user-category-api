from django.db import models

# Create your models here.
class User(models.Model):
	id = models.IntegerField(null = False, primary_key = True)
	first_name = models.CharField(max_length = 100, blank = False)
	last_name = models.CharField(max_length = 100, blank = True)
	email = models.CharField(max_length = 200, blank = False, unique = True)
	phone = models.CharField(max_length = 10, blank = True)

	def __str__(self):
		return self.first_name

class Category(models.Model):
	id = models.IntegerField(null = False, primary_key = True)
	category_name = models.CharField(max_length = 100, blank = False)
	description = models.CharField(max_length = 100, blank = False)

	def __str__(self):
		return self.category_name

class UserCategory(models.Model):
	id = models.IntegerField(null = False, primary_key = True)
	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, blank = False)
	category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, blank = False)

	# def __str__(self):
	# 	return self.user, self.category
		
class SubCategory(models.Model):
	id = models.IntegerField(null = False, primary_key = True)
	sub_category_name = models.CharField(max_length = 100, blank = False)
	description = models.CharField(max_length = 100, blank = False)
	category = models.ForeignKey(Category, related_name='sub_category', on_delete=models.CASCADE, blank = False)

	def __str__(self):
		return self.sub_category_name

class Item(models.Model):
	id = models.IntegerField(null = False, primary_key = True)
	item_name = models.CharField(max_length = 100, blank = False)
	description = models.CharField(max_length=100, blank = False)
	sub_category = models.ForeignKey(SubCategory, related_name='item_subcategory', on_delete=models.CASCADE, blank = False)

	def __str__(self):
		return self.item_name