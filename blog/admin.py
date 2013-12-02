#coding: utf-8
from django.contrib import admin
from blog.models import BlogTopic, BlogCategory, BlogPost, BlogImages
from utils.admin_image_widget import AdminImageWidget
from django.forms import ModelForm
from django_markdown.widgets import MarkdownWidget
from ckeditor.widgets import CKEditorWidget
from utils.ckeditor_widget import CKEditorSimple

class ImageForm(ModelForm):
    class Meta:
        model = BlogImages
        widgets = {
            'image' : AdminImageWidget,
        }

class TopicForm(ModelForm):
    class Meta:
        model = BlogTopic
        widgets = {
           # 'content' : CKEditorWidget,
           # 'content' : CKEditorSimple,
           'content' : MarkdownWidget,
        }


class BlogPostAdmin(admin.ModelAdmin):
    pass

class BlogCategoryAdmin(admin.ModelAdmin):
    pass


class BlogPostInline(admin.TabularInline):
    model = BlogPost
    verbose_name_plural = u'Посты'

class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    form = ImageForm
    verbose_name_plural = u'Изображения'

class BlogTopicAdmin(admin.ModelAdmin):
    form = TopicForm
    inlines = [
        BlogImagesInline,
        BlogPostInline,
    ]


admin.site.register(BlogTopic,BlogTopicAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory,BlogCategoryAdmin)
