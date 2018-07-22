from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Person, Group


def index(request):
	template = loader.get_template('namedrawing/profile/index.html')
	group_list = Group.objects.order_by('name')
	context = {
		'username': 'Brian',
		'groups': group_list,
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
	return HttpResponseRedirect(reverse('namedrawing:index'))