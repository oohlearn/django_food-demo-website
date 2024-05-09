"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
# 導入內建的app: dfango.contrib.auth，去使用裡面內建的login、logout功能
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("food/", include("food.urls")),
    path("", include("users.urls")),
    path("register/", user_views.register, name="register"),
    # login 和logout這兩個是based on class的views，所以後面要加as_view()
    # ，然後括號裡面可以加templates的路徑，告訴django去那邊找templates
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    # Django 5.0後，教材版本失效，要自己刻新的LogoutView
    path("logout/", user_views.UserLogoutView.as_view(http_method_names=["get", "post", "options"]), name="logout"),
    path("profile/", user_views.profile_page, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
