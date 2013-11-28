#coding: utf-8
from django.contrib import admin
from blog.models import BlogTopic, BlogCategory, BlogPost, BlogImages

class BlogPostAdmin(admin.ModelAdmin):
    pass

class BlogCategoryAdmin(admin.ModelAdmin):
    pass



class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    verbose_name_plural = u'Изображения'

class BlogTopicAdmin(admin.ModelAdmin):
    inlines = [
        BlogImagesInline,
    ]


admin.site.register(BlogTopic,BlogTopicAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory,BlogCategoryAdmin)
