from django.contrib import admin
from main.models import Picture,UserProfile,Comment
# Register your models here.

# class PictureAdmin(admin.ModelAdmin):
#     list_display = ('send_by','send_to','created_time','content')

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Comment)