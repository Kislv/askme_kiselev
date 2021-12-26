"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path('admin/', admin.site.urls),
    path('hot/', views.hot, name='hot'),
    path('question/<int:number>/', views.question, name='question'),
    path('ask/', views.ask, name="ask"),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),
    path('tag/<slug:tag>/', views.tag, name="tag"),
    path('tag/', views.tag, name="tag"),
    path('user_settings/', views.user_settings, name="user_settings"),
    path('new/', views.index, name="new"),
    path('', views.index, name="index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
