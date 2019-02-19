from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'^getpostuser$', GetPostUser.as_view()), ################################## # TESTED # get/post user
    url(r'^getsingleuser/(?P<id>\d+)$', GetSingleUser.as_view()), ################## # TESTED # get single user
    url(r'^getpostcategory$', GetPostCategory.as_view()), ########################## # TESTED # get/post category
    url(r'^getsinglecategory/(?P<id>\d+)$', GetSingleCategory.as_view()), ########## # TESTED # get single category
    url(r'^getpostusercategory$', GetPostUserCategory.as_view()),################### # TESTED # get/post user category
    url(r'^getsingleusercategory/(?P<id>\d+)$', GetSingleUserCategory.as_view()), ## # TESTED # get single user category
	url(r'^categoryhasusers/(?P<id>\d+)$', CategoryHasUsers.as_view()), ############ # TESTED # get all users in which category by id
	url(r'^userhascategory/(?P<id>\d+)$', UserHasCategory.as_view()), ############## # TESTED # get all category in which users is by id
    url(r'^getpostsubcategory$', GetPostSubCategory.as_view()), #################### # TESTED # get/post sub category
    url(r'^getsinglesubcategory/(?P<id>\d+)$', GetSingleSubCategory.as_view()), #### # TESTED # get single sub category
    url(r'^getallsubcategoryunderparticularcategory/(?P<id>\d+)$', GetAllSubCategoryUnderParticularCategory.as_view()), ### # TESTED # get all sub category under paricular category
    url(r'^getpostitem$', GetPostItem.as_view()), ################################## # TESTED # get/post item
    url(r'^getsingleitem/(?P<id>\d+)$', GetSingleItem.as_view()), ################## # TESTED # get single item
    url(r'^getallitemundersubcategory/(?P<id>\d+)$', GetAllItemUnderSubCategory.as_view()), ############################### # TESTED # get all item under sub category
	url(r'^getsubcategoryanditemundercategory/(?P<id>\d+)$', GetSubCategoryAndItemUnderCategory.as_view()), ############### # TESTED # get sub category and item under category
	url(r'^getcategorysubcategoryitemunderuser/(?P<id>\d+)$', GetCategorySubCategoryItemUnderUser.as_view()), ############# # TESTED # get category sub category and item under user
]