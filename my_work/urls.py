from django.urls import path
from my_work.apps import MyWorkConfig
from django.views.decorators.cache import cache_page

from my_work.utils.client_foo import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from my_work.utils.index_view import IndexView

from my_work.views import contact

app_name = MyWorkConfig.name

urlpatterns = [
    path('', cache_page(5)(IndexView.as_view()), name='index'),
    path('contact/', contact, name='contact'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('newsletters/', NewsletterListView.as_view(), name='newsletters'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/newsletter_details/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('logs/', cache_page(60)(LogListView.as_view()), name='logs'),
    path('log_details/<int:pk>/', LogDetailView.as_view(), name='log_details'),
]
