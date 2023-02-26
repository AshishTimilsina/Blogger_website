from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>",views.Blogpost, name="bloggerHome"),
    path("about/",views.about,name="aboutus"),
    path("contact/",views.contact,name="contactus"),
    path("search/",views.search,name="search"),
    path("signup/",views.handlesignup,name="handlesignup"),
    path("login/",views.handleLogin,name="handleLogin"),
    path("logout/",views.handleLogout,name="handleLogout"),
    path("postcomment/",views.postcomment,name="postcomment"),
]
admin.site.site_header="Blogger.com "
admin.site.site_title="Blogger.com"
admin.site.index_title="Blogger.com Admin Panel"
