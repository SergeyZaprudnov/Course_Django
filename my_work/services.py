from django.core.mail import send_mail

from config import settings
from my_work.models import Message, Log, Newsletter
from django.core.cache import cache


def daily_send():
    for item in Newsletter.objects.filter(frequency='daily'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def weekly_send():
    for item in Newsletter.objects.filter(frequency='weekly'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def monthly_send():
    for item in Newsletter.objects.filter(frequency='monthly'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def send_newsletter(message_item: Newsletter):
    customers_emails = message_item.customers.values_list('email', flat=True)

    for email in customers_emails:
        message = Message.objects.create(newsletter=message_item)
        try:
            send_mail(
                message_item.subject,
                message_item.body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            status = 'success'
            response = 'Email sent successfully'
        except Exception as e:
            status = 'error'
            response = str(e)
        Log.objects.create(message=message, status=status, response=response)


def get_cached_log_data(log):
    if settings.CACHE_ENABLE:
        cache_key = f'log_{log.pk}'
        cached_data = cache.get(cache_key)
        if cached_data is None:
            cached_data = {
                'message': log.message,
                'timestamp': log.timestamp,
                'status': log.status,
                'response': log.response,
            }
            cache.set(cache_key, cached_data, 300)
        return cached_data
    else:
        return {
            'message': log.message,
            'timestamp': log.timestamp,
            'status': log.status,
            'response': log.response,
        }
