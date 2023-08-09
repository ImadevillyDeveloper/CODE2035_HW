from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price','created_date','updated_date','auction','get_thumbnail']
    list_filter = ['auction','created_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = [
        ("Общее", {'fields':['title', 'description', 'image']}),
        ("Финансы", {'fields': ['price','auction'], "classes": ['collapse']}),
    ]

    def get_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" width="100" height="100" />')
    get_thumbnail.short_description = 'Изображение'

    @admin.action(description="Убрать возможность торга")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Поставить возможность торга")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
