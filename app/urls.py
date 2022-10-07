from django.urls import path
from . import views
from gallery.views import gallery, delete_img

urlpatterns = [
    path('',views.home,name='index'),
    path('create/',views.link_shortner,name='hj'),

    path('save/',views.save_data,name='save'),
    path('anonymous_save/',views.anonymous_save,name='anonymous_save'),

    path('search/',views.search,name='search'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),

    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard_chart/',views.dashboard_chart_api, name='dashboard_chart'),
    path('test_links/', views.test_links, name='test_links'),
    path('settings/', views.settingsPage, name='settings'),
    path('tags/', views.tagsPage, name='tags'),
    path('files/', views.filesPage, name='files'),
    path('file/<str:pk>/', views.fileShare, name='fileshare'),

    path('gallery/',gallery, name="gallery"),
    path('delete_img/',delete_img, name="delete_img"),

    path('links/',views.user_ceated_links, name='user_created_links'), # Test link
    path('delete/',views.delete,name='delete'),
    path('delete_file/',views.deleteFile,name='delete_file'),
    path('edit/',views.edit_links,name='edit'), # Json resp+
    path('edit_link/',views.edit,name='edit_link'), # Json resp
    
    path('qr/<str:short_url>',views.qr_code,name='qr'),
    path('analytics/',views.analytics, name='analytics'),

    path('<str:pk>/',views.go,name='go'),
]
