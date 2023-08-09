from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'description', 'price', 'created_date', 'updated_date', 'auction',
                    'show_image']
    list_filter = ['auction', 'created_at']

    actions = ['make_auction_as_false', 'make_auction_as_true', 'set_default_image']

    fieldsets = (
        ('Общее', {'fields': ('title', 'user', 'description', 'image')}),
        ('Финансы', {'fields': ('price', 'auction'), 'classes': ['collapse']})
    )

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='установить изображение по умолчанию')
    def set_default_image(self, request, queryset):
        queryset.update(image='adv.png')

admin.site.register(Advertisements, AdvertisementAdmin)
