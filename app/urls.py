from django.urls import path
from . import views


urlpatterns = [
	
	path('app/dashboard/',views.dashboard,name='dashboard'),
    path('guard_add/',views.guard_add,name='guard_add'),
    path('view_guards/',views.view_guards,name='view_guards'),
    
    path('app/', views.home, name="login"),
    path('app/logout',views.logoutUser,name="logout"),
    
]