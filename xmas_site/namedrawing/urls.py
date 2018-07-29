from django.urls import path

from . import views

app_name = 'namedrawing'
urlpatterns = [
	path('profile/', views.index, name='index'),
	path('groups/new/', views.creategroup, name='creategroup'),
	path('groups/new/create', views.postcreategroup, name='postcreategroup'),
	path('people/', views.createpeople, name='people'),
	path('people/create', views.postcreatepeople, name='postcreatepeople'),
]
