"""
URL configuration for E_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from instructorApp import views
from studentApp import views as studView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructor/register',views.InstructorView.as_view(),name="instructor_reg"),

    path('student/register',studView.StudentRegister.as_view(),name="student_reg"),
    path('student/login',studView.StudentLoginView.as_view(),name="student_log"),
    path('',studView.StudentView.as_view(),name="student_view"),
    path('course/detail/<int:id>',studView.CourseDetailView.as_view(),name="course_detail"),
    path('add/cart/<int:id>',studView.AddToCartView.as_view(),name="add_to_cart"),
    path('student/logout',studView.LogoutView.as_view(),name="student_logout"),
    path('cart/summary',studView.CartSummary.as_view(),name="cart_summary"),
    path('cart/delete/<int:id>',studView.CartDeleteView.as_view(),name="cart_delete"),
    path('checkout',studView.CheckOutView.as_view(),name="checkout_view"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
