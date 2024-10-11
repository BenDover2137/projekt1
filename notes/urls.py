from django.urls import path
from .views import note_list, note_detail, note_create, note_edit, login_view, note_delete

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/<int:pk>/', note_detail, name='note_detail'),
    path('note/add/', note_create, name='note_create'),
    path('note/<int:pk>/edit/', note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
    path('login/', login_view, name='login'),

]
