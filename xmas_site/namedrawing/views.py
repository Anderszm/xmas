from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('profile/index.html')
	context = {
		'name': 'Brian',
	}
	return HttpResponse(template.render(context, request))