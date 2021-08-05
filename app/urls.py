from django.urls import path
from . import views


urlpatterns = [
	
	path('app/dashboard/',views.dashboard,name='dashboard'),
    path('guard_add/',views.guard_add,name='guard_add'),
    path('view_guards/',views.view_guards,name='view_guards'),
    path('add_company/',views.addcompany,name='add_company'),
    path('view_company/',views.viewcompany,name='view_company'),
    path('feedback/',views.feedback,name='feedback'),
    path('app/', views.home, name="login"),
    path('app/logout',views.logoutUser,name="logout"),
    path('app/profile/<int:id>',views.profile,name='profile'),
    path('app/search',views.search,name='search'),
]