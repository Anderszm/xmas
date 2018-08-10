from django.urls import path
from . import views

app_name = 'namedrawing'
urlpatterns = [
	path('profile/', views.index, name='index'),
	path('groups/<str:groupid>/show', views.showgroup, name='showgroup'),
	path('groups/new/', views.creategroup, name='creategroup'),
	path('groups/new/create', views.postcreategroup, name='postcreategroup'),
	path('groups/addperson', views.addpersontogroup, name='addpersontogroup'),
	path('groups/<str:groupid>/join', views.joingroup, name='joingroup'),
	path('groups/addperson/add', views.postaddpersontogroup, name='postaddpersontogroup'),
	path('people/', views.createpeople, name='people'),
	path('people/create', views.postcreatepeople, name='postcreatepeople'),
	path('signup/', views.signup, name='signup'),
	
]
