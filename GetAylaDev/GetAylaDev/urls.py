
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserProfile.urls')),
    path('mydash/', include('CurrentDashboard.urls')),
    path('', include('home.urls')),
    path('services/', include('home.urls')),
    path('account/', include('Accounts.urls')),

]
