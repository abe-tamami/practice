from django.urls import path
from . import views

app_name = 'fusen'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fusen_id>', views.detail, name='detail'),
    path('new_fusen', views.new_fusen, name='new_fusen'),
    path('delete_fusen/<int:fusen_id>', views.delete_fusen, name='delete_fusen'),
    path('edit_fusen/<int:fusen_id>', views.edit_fusen, name='edit_fusen'),
]
