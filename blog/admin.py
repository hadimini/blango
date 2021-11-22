from django.contrib import admin

from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
  list_display = ['slug', 'published_at']
  prepopulated_fields = {'slug': ('title', )}
  

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
