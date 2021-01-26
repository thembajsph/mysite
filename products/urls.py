# to ref a url we need to import the path function

from django.urls import path

# now you need to import the views function to use it
from . import views

# when we import views that views folder become an object
# views.index()

# /products in the root of this app  , urls
#  /product/1/details
#  /products/new

# first argument is the empty root and second is our views functions

urlpatterns = [

 path('', views.index),
 path('new', views.new)

]