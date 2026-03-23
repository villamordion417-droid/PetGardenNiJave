from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_post, name='upload'),
    path('wall/', views.wall_view, name='wall'),
    path('candle/<int:post_id>/', views.add_candle, name='candle'),
]
