from django.urls import path
from my_work.apps import MyWorkConfig
from django.views.decorators.cache import cache_page
from my_work.utils.index_view import IndexView

app_name = MyWorkConfig.name

urlpatterns = [
    path('', cache_page(5)(IndexView.as_view()), name='index'),

]
