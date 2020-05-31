
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, path
from .models import Person, Group, Membership, Friendship
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator

@login_required
def index(request):	
	memberships = Membership.objects.filter(user = request.user)
	grouplist = {}
	
	for membership in memberships:
		grouplist[membership.group.id] = membership.group.name
	
	context = {
		'username': request.user.username,
		'groups': grouplist
	}
	return render(request, 'accounts/index.html', context)

#signup is here
#login is based on the MDN tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'../templates/registration/login.html')
			
    context['form']=form
    return render(request,'registration/signup.html',context)

@login_required
def userlandingpage(request):
	return render(request, 'namedrawing/userlandingpage.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
	def get(self, request):	
		memberships = Membership.objects.filter(user = request.user)
		grouplist = {}
		
		for membership in memberships:
			grouplist[membership.group.id] = membership.group.name
		
		context = {
			'activetab': 'User Profile',
			'username': request.user.username,
			'groups': grouplist
		}
		return render(request, 'namedrawing/profile/show.html', context)

@method_decorator(login_required, name='dispatch')
class GroupView_new(View):

	def get(self, request):
		context = {'name': request.user.username}
		return render(request, 'namedrawing/groups/new.html', context)
	
	def post(self, request):
		groupname= request.POST['group_name']
	
		g1 = Group.objects.create(name=groupname)
		
		m1 = Membership.objects.create(user = request.user,
			group = g1, 
			isAdmin = True)
			
		return HttpResponseRedirect(reverse('namedrawing:userlandingpage'))
		
		
@method_decorator(login_required, name='dispatch')
class GroupView(View):
	def get(self, request, groupid):
		membershiplist = Membership.objects.filter(group__id = groupid) 
		#print(membershiplist)
		context = {
			'username': request.user.username,
			'group': Group.objects.get(id = groupid),
			'memberships': membershiplist,
		}
		users=[]
		for member in membershiplist:
			users.append(member.user_id)

		if(request.user.id in users):
			return render(request, 'namedrawing/groups/show.html', context)
		else:
			return HttpResponseRedirect(reverse('namedrawing:userlandingpage'))
		

	#delete route
	def post(self, request, groupid):
		group = Group.objects.get(id = groupid)
		
		membershiplist = Membership.objects.filter(group__id = groupid)
		
		for member in membershiplist:
			if member.user == request.user:
				if member.isAdmin == True:
					group.delete()
		
		return HttpResponseRedirect(reverse('namedrawing:index'))

@login_required
def listgroups(request):
	membershiplist = Membership.objects.filter(user__id = request.user.id)
	
	grouplist = {}
	for groups in membershiplist:
		grouplist[groups.group_id]=groups.group
	
	context = {
		'username': request.user.username,
		'groups': grouplist
	}

	return render(request, 'namedrawing/groups/listgroups.html', context)

@login_required
def joingroup(request, groupid):
	usr = request.user
	grp = Group.objects.get(id = groupid)
	
	#get all membership in a group and add a friendship containing the new user
	membershiplist = Membership.objects.filter(group__id = grp.id) 
	
	
	isMember = False
	#check if user is already a member of the group
	for member in membershiplist:
		if member.user == usr:
			isMember = True
	
	# create membership and friendships if not already a member
	if not isMember:
		for _membership in membershiplist:
			Friendship.objects.create(user = usr, membership = _membership)
		
		#create new membership for this user and add friendships for all the current members of the group
		membrship = Membership.objects.create(user = usr, group = grp)
		usrlist = User.objects.filter(group__id = grp.id)
		
		for _user in usrlist:
			print(_user.username)
			if _user == usr:
				pass
			else:
				friendship = Friendship.objects.create(user = _user, membership = membrship)
			
	return HttpResponseRedirect(reverse('namedrawing:index'))

	
