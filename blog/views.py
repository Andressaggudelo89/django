from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
	{
		'author' : 'Andres Agg',
		'title' : 'Blog post 1',
		'content' : 'First post Content',
		'date_posted' : 'July 27, 2016'
	},
	{
		'author' : 'Daniela Nav',
		'title' : 'Blog post 2',
		'content' : 'Second post Content',
		'date_posted' : 'July 27, 2017'
	},
	{
		'author' : 'Leyanis Tsk',
		'title' : 'Blog post 3',
		'content' : 'Third post Content',
		'date_posted' : 'May 31, 2018'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})