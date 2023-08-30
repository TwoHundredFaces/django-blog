
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_text', 'pub_date')
    list_filter = ('pub_date',)