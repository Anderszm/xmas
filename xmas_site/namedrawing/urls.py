from django.urls import path
from . import views
from namedrawing.views import GroupView

app_name = 'namedrawing'
urlpatterns = [
	path('profile/', views.index, name='index'),
	path('groups/new/', GroupView.as_view(), name='newgroup_get'),
	path('groups/new/', GroupView.as_view(), name='newgroup_post'),
	path('groups/<str:groupid>/show', views.showgroup, name='showgroup'),
	path('groups/<str:groupid>/delete', views.deletegroup, name='deletegroup'),
	path('groups/<str:groupid>/join', views.joingroup, name='joingroup'),
	path('signup/', views.signup, name='signup'),
	
]
