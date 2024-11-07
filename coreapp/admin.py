from django.contrib import admin
from .models import add_post
# Register your models here.
@admin.register(add_post)
class show(admin.ModelAdmin):
    list_display = ['title','desh']