from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Email клиента', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    SEND_FREQUENCY_CHOICES = (
        ('create', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    )
    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    )

    subject = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(verbose_name='Содержимое')
    frequency = models.CharField(max_length=50, choices=SEND_FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created', verbose_name='Статус')
    customers = models.ManyToManyField('Customer', verbose_name='Клиенты', related_name='newsletters')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


