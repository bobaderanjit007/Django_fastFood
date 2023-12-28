from django.urls import path
from delivery import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home ),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('login/', views.loginPage),
    path('signup/', views.signup),
    path('cart/<str:pk>', views.mycart),
    path('cart/delete/<int:pk>/<str:pid>', views.removeCart ),
    path('orders/<str:pk>', views.orders),
    path('logout/', views.logoutPage),
    path('update/<str:pk>', views.updateProfile),
    path('cart/<str:pk>/<str:pid>', views.addCart),
    path('checkout/<int:unit>/<int:product_id>/', views.orderNow, name="orderNow"),

]
