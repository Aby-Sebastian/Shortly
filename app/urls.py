from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('create/',views.link_shortner,name='hj'),
    path('showall/',views.showall,name='show'), # Test link
    path('showallusers/',views.showallusers,name='showusers'), # Test link

    path('reg/',views.reg,name='reg'),
    path('log/',views.log,name='log'),
    path('save/',views.save_data,name='save'),
    path('anonymous_save/',views.anonymous_save,name='anonymous_save'),

    path('search/',views.search,name='search'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),

    path('analytics_data/',views.analytics_data, name='analytics_data'),

    path('dashboard/',views.dashboard, name='dashboard'),
    path('link_page/',views.page_link, name='link_page'),
    path('test_links/', views.test_links, name='test_links'),
    path('settings/', views.settingsPage, name='settings'),
    path('tags/', views.tagsPage, name='tags'),
    path('files/', views.filesPage, name='files'),
    path('file/<str:pk>/', views.fileShare, name='fileshare'),
    path('ind/', views.ind, name='ind'),   # Test link

    path('links/',views.user_ceated_links, name='user_created_links'), # Test link
    path('delete/',views.delete,name='delete'),
    path('delete_file/',views.deleteFile,name='delete_file'),
    path('edit/',views.edit_links,name='edit'),
    path('edit_link/',views.edit,name='edit_link'),
    
    path('t/', views.temp, name="t"),

    path('qr/<str:short_url>',views.qr_code,name='qr'),
    path('analytics/',views.analytics, name='analytics'),

    path('<str:pk>/',views.go,name='go'),
]
