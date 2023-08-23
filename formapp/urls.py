from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export_csv', views.export_to_csv, name='export_csv'),
    path('submissions', views.submissions, name='submissions'),
    path('submission/<str:cn>', views.submission, name='submission'),
    path('submission/edit/<str:cn>', views.edit, name='edit'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)