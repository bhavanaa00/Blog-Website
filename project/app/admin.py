from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'status', 'created_on')
  list_filter = ('status',)
  search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('fullname', 'phone', 'message')

admin.site.register(Contact, ContactAdmin)

admin.site.register(Newsletter)

