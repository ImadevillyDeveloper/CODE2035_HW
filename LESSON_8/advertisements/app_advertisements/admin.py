from django.contrib import admin
from .models import Advertisement
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
from app_advertisements.models import Advertisement
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'price','created_date','updated_date', 'auction']
    list_filter = ['auction','created_at', 'updated_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = (
        ("Общие", {
            'fields': ('title', 'description')
        }),
         ("Финансы", {
            'fields': ('price', 'auction'),
            'classes': ('collapse',),
        })
    )
    @admin.action(description="Убрать возможность торгов")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
        
    @admin.action(description="Вернуть возможность торгов")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)