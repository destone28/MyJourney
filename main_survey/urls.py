from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageView.get, name='first_page'),
    #path('<int:page_id>', views.PageView.get, name='show_page'),

]
