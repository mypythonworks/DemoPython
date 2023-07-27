from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name='movieapp'

urlpatterns = [
    # path('',views.operate,name='home'),
    # path('result/', views.result, name='result')
    path('',views.index,name='index'),
    path('movie/<int:mov_id>/', views.details, name='details'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:mov_id>', views.update, name='update'),
    path('delete/<int:mov_id>', views.delete, name='delete')

]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)