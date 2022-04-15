
from django.urls import path,include
from . import views

app_name='movies'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/comments/',views.comments_create,name='comments_create'),

]