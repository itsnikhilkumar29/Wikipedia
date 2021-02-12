from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util
import random
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def bytitle(request,title):
	if util.get_entry(title):
		return render(request, "encyclopedia/display_article.html",{
			"content":util.get_entry(title),
			"title":title
			})
	else:
		return HttpResponse("Sorry, requested article not found")

def random_page(request):
	return bytitle(request,random.choice(util.list_entries()))
	# randomtitle=random.choice(util.list_entries())
	# return render(request,"encyclopedia/random_page.html",{
	# 	'title':randomtitle,
	# 	'content':util.get_entry(randomtitle)
	# 	})

def search(request):
	title=request.POST['q']
	all_titles=util.list_entries()
	if title in all_titles:
		return HttpResponse(util.get_entry(title))
	else:
		search_results=[]
		for each_title in all_titles:
			if title.lower() in each_title.lower():
				search_results.append(each_title)
		return render(request,"encyclopedia/search_results.html",{
			'search_results':search_results,
			'search_query':title
			})

def createnew(request):
	if request.method=="GET":
		return render(request,"encyclopedia/newpage.html")
	else:
		content=request.POST['content']
		title=request.POST['titlename']
		util.save_entry(title,content)
		return HttpResponseRedirect(reverse("bytitle",kwargs={'title':title}))

def editpage(request,title):
	if request.method=='GET':
		return render(request,"encyclopedia/newpage.html",{
			"title":title,
			"content":util.get_entry(title)
			})

