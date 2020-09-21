from django.urls import path
from . import views
urlpatterns = [
    path('get-spot-obj/',views.GetSpot.as_view()),
    path('search-spot/',views.SearchSpot.as_view()),
    path('update-spot/<int:pk>/',views.UpdateSpot.as_view()),
    path('create-spot/',views.PostSpot.as_view()),
    path('delete-spot/<int:pk>/',views.DeleteSpot.as_view()),
    path('get-user-obj/', views.GetUsers.as_view()),
    path('search-user/', views.SearchUser.as_view()),
    path('update-user/<int:pk>/', views.UpdateUser.as_view()),
    path('create-user/', views.PostUser.as_view()),
    path('delete/<int:pk>/', views.DeleteUser.as_view()),
]