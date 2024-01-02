from django.urls import path

from .views import index, upload_image, display_photos, categories

app_name = 'myapp1'
urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('upload/', upload_image, name='upload_image'),
    path('photos/<int:topic_id>/', display_photos, name='display_photos'),
]
