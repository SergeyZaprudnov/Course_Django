from django.db.models import Count
from django.shortcuts import render
from django.views import generic

from my_work.models import Newsletter, Client
from blog.models import BlogPost


class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        newsletters_count = Newsletter.objects.count()  # получаем информацию об общем количестве рассылок
        newsletters_count_run = Newsletter.objects.filter(
            status='running').count()  # получаем информацию об количестве активных рассылок
        unique_customers_count = Client.objects.annotate(num_newsletters=Count('newsletters')).filter(
            num_newsletters__gt=0).count()  # получаем информацию об уникальных клиентах
        blog_posts = list(BlogPost.objects.filter(is_active=True).order_by('?').values_list('title', flat=True)[
                          :3])  # получаем три случайные публикации из блока
        context = {
            'title': 'Главная',
            'newsletters_count': newsletters_count,
            'newsletters_count_run': newsletters_count_run,
            'unique_customers_count': unique_customers_count,
            'blog_posts': blog_posts
        }
        return render(request, 'my_work/index.html', context)
