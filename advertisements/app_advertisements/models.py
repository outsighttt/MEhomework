from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.urls import reverse

User = get_user_model()

def validate_title(value):
    if value.startswith('?'):
        raise ValidationError(
            gettext_lazy('Заголовок не может начинаться с символа "?"'),
            params={'value':value}
        )

class Advertisements(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128, validators=[validate_title])
    description = models.TextField('описание объявления')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('возможность торга', help_text='Отметьте если торг уместен.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image=models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} <span/>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} <span/>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='изображение')
    def show_image(self):
        return format_html('<img src=/media/{} height=50>', self.image)

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Объявление'

    def get_absolute_url(self):
        return reverse('adv_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return "%s object (%s)" % (self.__class__.__name__, f'id={self.id}, title={self.title}, price={float(self.price)}')
