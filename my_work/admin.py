from django.contrib import admin

from my_work.models import Client, Newsletter, Message, Log



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment')
    list_filter = ('email', 'full_name', 'comment')
    search_fields = ('email', 'full_name')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'frequency', 'status')
    list_filter = ('frequency', 'status')
    search_fields = ('customers__first_name', 'customers__last_name', 'customers__email')
    # filter_horizontal = ('customers',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['newsletter']
    list_filter = ['newsletter']
    search_fields = ['newsletter']


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp', 'status')
    list_filter = ('message', 'timestamp', 'status')
    search_fields = ('message', 'timestamp', 'status')