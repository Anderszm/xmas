from django.urls import path
from . import views
from namedrawing.views import GroupView, GroupView_new, ProfileView

app_name = 'namedrawing'
urlpatterns = [
	path('profile/', ProfileView.as_view(), name='profile_get'),
	path('groups/new/', GroupView_new.as_view(), name='newgroup_get'),
	path('groups/new/', GroupView_new.as_view(), name='newgroup_post'),
	path('groups/<str:groupid>', GroupView.as_view(), name='showgroup'),
	path('groups/<str:groupid>', GroupView.as_view(), name='deletegroup'),
	path('groups/<str:groupid>/join', views.joingroup, name='joingroup'),
	path('signup/', views.signup, name='signup'),
	
]
