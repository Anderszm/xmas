#**********************************************************
# Name		Date		Change
# Zach		7/29/18		Adjusted postcreategroup to redirect to people.html


#**********************************************************
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, path
from .models import Person, Group, Membership, Friendship
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
	if request.user.is_authenticated:
		template = loader.get_template('namedrawing/profile/index.html')
		group_list = Group.objects.order_by('name')
		people_list = Group.objects.order_by('name')
		context = {
			'username': request.user.username,
			'groups': group_list,
			'people': people_list,
		}
		return render(request, 'namedrawing/profile/index.html', context)
	else:
		return HttpResponseRedirect(reverse('login'))
		#HttpResponse(template.render(context, request))

def creategroup(request):
	#template = loader.get_template('namedrawing/groups/new.html')
	context = {'name': 'Brian'}
	#return HttpResponse(template.render(context, request))
	return render(request, 'namedrawing/groups/new.html', context)
	
def postcreategroup(request):
	groupname= request.POST['group_name']
	
	g1 = Group.objects.create(name=groupname)
	
	m1 = Membership.objects.create(user = request.user,
		group = g1,
		isAdmin = True)

	return HttpResponseRedirect(reverse('namedrawing:addpersontogroup'))

def addpersontogroup(request):
	context = {'name': 'Brian'}
	return render(request, 'namedrawing/groups/addperson.html', context)

def postaddpersontogroup(request):
	user_name = request.POST['user_username']
	groupname = request.POST['group_groupname']
	usr = User.objects.get(username = user_name)
	grp = Group.objects.get(name = groupname)
	membrship = Membership.objects.create(user = usr, group = grp)
	# friendship = Friendship.objects.create(user = usr)
	
	usrlist = User.objects.filter(group__id = grp.id)
	
	for _user in usrlist:
		print(_user.username)
		friendship = Friendship.objects.create(user = _user, membership = membrship)
	
	return HttpResponseRedirect(reverse('namedrawing:index'))
	
	
	
def createpeople(request):
	return render(request,'namedrawing/groups/people.html')

def postcreatepeople(request):
	personname= request.POST['person_name']
	Group.objects.create(name=personname)
	return HttpResponseRedirect(reverse('namedrawing:index'))

#signup is here
#login is based on the MDN tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
def signup(request):
	if request.method== 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# leaving this commented out for now. Getting an error doing authenticate and login
			# stackoverflow suggested removing the authenticate. 
			# current solution may not be scrubbing the inputs though
			
			# form.save()
			# username = form.cleaned_data.get('username')
			# raw_password = form.cleaned_data.get('password')
			# user = authenticate(username=username, password=raw_password)
			# login(request, user)
			
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('namedrawing:index')
	else:
		form = UserCreationForm()
	return render(request, 'namedrawing/profile/signup.html', {'form': form})