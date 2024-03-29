from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag_list', views.tag_list, name='tag_list'),
    path('setting', views.setting, name='setting'),
    path('search', views.search, name='search'),
    path('privacy', views.privacy, name='privacy'),
    path('net_a_tutorial', views.net_a_tutorial, name='net_a_tutorial'),
    path('my_page/', views.my_page, name='my_page'),
    path('my_fish', views.my_fish, name='my_fish'),
    path('history', views.history, name='history'),
    path('genre_list', views.genre_list, name='genre_list'),
    path('favorite_list', views.favorite_list, name='favorite_list'),
    path('edit_fish', views.edit_fish, name='edit_fish'),
    path('base', views.base, name='base'),
    path('add_fish', views.add_fish, name='add_fish'),
    path('registration', views.registration, name='registration'),
    path('base_root', views.base_root, name='base_root'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('info', views.info, name='info'),

    path('', views.index, name='index'),
    path('fish_info/<int:fish_info_id>/', views.fish_info, name='fish_info'),
    path('genre_list/<int:genre_id>/', views.genre, name='genre'),
    path('favorite_toggle/<int:fish_info_id>/', views.favorite_toggle, name='favorite_toggle'),
    path('search/results/', views.search_results, name='search_results'),
    path('search/', views.search_fish_info, name='search_fish_info'),
    path('add_fish', views.add_fish, name='add_fish'),
    path('icon_change/', views.icon_change, name='icon_change'),
    path('fish_new_list/', views.fish_new_list, name='fish_new_list'),
    path('fish_size_list/', views.fish_size_list, name='fish_size_list'),
    path('fish_favorite_list/', views.fish_favorite_list, name='fish_favorite_list'),
    path('fish_info/edit/<int:fish_id>/', views.edit_fish_info, name='edit_fish_info'),
    path('first', views.first, name='first'),
    path('setting_edit/', views.setting_edit, name='setting_edit'),
    path('setting_password/', views.setting_password, name='setting_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)