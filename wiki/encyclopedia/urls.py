from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("title/<str:title>",views.bytitle,name="bytitle"),
    path("random_page",views.random_page,name="random_page"),
    path("search",views.search,name="search"),
    path("createnew",views.createnew,name="createnew"),
    path("editpage/<str:title>",views.editpage,name="editpage")
]
