#**********************************************************
# Name		Date		Change
# Zach		7/29/18		Adjusted postcreategroup to redirect to people.html


#**********************************************************
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Person, Group


def index(request):
	template = loader.get_template('namedrawing/profile/index.html')
	group_list = Group.objects.order_by('name')
	people_list = Group.objects.order_by('name')
	context = {
		'username': 'Adding Group and People',
		'groups': group_list,
		'people': people_list,
	}
	return render(request, 'namedrawing/profile/index.html', context)
	#HttpResponse(template.render(context, request))

def creategroup(request):
	#template = loader.get_template('namedrawing/groups/new.html')
	context = {'name': 'Brian'}
	#return HttpResponse(template.render(context, request))
	return render(request, 'namedrawing/groups/new.html', context)
	
def postcreategroup(request):
	groupname= request.POST['group_name']
	Group.objects.create(name=groupname)
	return HttpResponseRedirect(reverse('namedrawing:people'))

def createpeople(request):
	return render(request,'namedrawing/groups/people.html')

def postcreatepeople(request):
	personname= request.POST['person_name']
	Group.objects.create(name=personname)
	return HttpResponseRedirect(reverse('namedrawing:index'))