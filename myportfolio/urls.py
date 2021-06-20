
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('myportfolio/', include('portfolioApp.urls')),
    path('admin/', admin.site.urls),
]
