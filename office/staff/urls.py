from django.urls import path
from.import views
urlpatterns =[
    path("",views.index,name="index"),
    path("about",views.about, name="about"),
    path("blog",views.blog, name="blog"),
    path("class",views.class1, name="class"),
    path("hello",views.hello, name="hello")
]