from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


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
    path('app/companyprofile/<int:id>',views.companyprofile,name='companyprofile'),
    path('app/companyprofile/update/<int:id>',views.company_update,name='company_update'),
    path('app/profile/choosecompany/<int:id>',views.choosecompany,name='choosecompany'),
    path('app/profile/update/<int:id>',views.guard_update,name='guard_update'),
    path('app/profile/photoupload/<int:id>',views.photoupload,name='photoupload'),
    path('app/download/guards',views.exportcsv_guard,name="exportcsv_guard"),
    path('app/download/company',views.exportcsv_company,name="exportcsv_company"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)