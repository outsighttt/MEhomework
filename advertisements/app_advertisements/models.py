from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisements(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128)
    description = models.TextField('описание объявления')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('возможность торга', help_text='Отметьте если торг уместен.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date()==timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} <span/>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} <span/>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Объявление'

    def __str__(self):
        return "%s object (%s)" % (self.__class__.__name__, f'id={self.id}, title={self.title}, price={float(self.price)}')
