'''
Blog URLs 

'''

from django.urls import path
from . import views

urlpatterns = [
# assigning post_list view to the root URL
path('', views.post_list, name = 'post_list'), 

]