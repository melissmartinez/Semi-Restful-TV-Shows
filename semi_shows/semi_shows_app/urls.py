from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index, name='index'),
    path('show/new',views.new_show),
    path('new_show', views.create_show),
    path('show/<int:id>', views.show_one), #GET
    path('show/<int:id>/delete', views.delete), #POST
    path('show/<int:id>/edit', views.edit), #GET
    path('show/<int:id>/update', views.update) #POST
]

    
