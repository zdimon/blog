#coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from mixer.backend.django import mixer
from blog.models import BlogCategory, BlogTopic, BlogPost

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Deleting data.......' )
        BlogCategory.objects.all().delete()
        BlogTopic.objects.all().delete()
        BlogPost.objects.all().delete()

        self.stdout.write('Start loading.......' )
        categories = mixer.cycle(10).blend(BlogCategory)
        for c in categories:
            topics = mixer.cycle(10).blend(BlogTopic,category=c, title=u'Заголовок блога категории '+c.name)
            for t in topics:
                posts = mixer.cycle(10).blend(BlogPost,topic=t,content=mixer.fake, author='Fedot')
        self.stdout.write('Well done' )