from django.shortcuts import render, redirect
from .models import Topic, Image
from .forms import ImageUploadForm


def index(request):
    return render(request, 'myapp1/index.html')


def categories(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'myapp1/categories.html', context)


def upload_image(request):
    if request.method != 'POST':
        form = ImageUploadForm()
    else:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp1:categories')

    context = {'form': form}
    return render(request, 'myapp1/upload_image.html', context)


def display_photos(request, topic_id):
    # Получаем объект темы по ID
    topic = Topic.objects.get(pk=topic_id)
    # Фильтруем изображения, связанные с этой темой
    images = Image.objects.filter(title=topic)
    context = {'topics_with_images': images}
    return render(request, 'myapp1/display_photos.html', context)
