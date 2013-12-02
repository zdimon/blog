#coding: utf-8
from django import forms
from django.utils.safestring import mark_safe

class CKEditorSimple(forms.Textarea):
    class Media:
        # Пути до файлов CKEditor относительно переменной MEDIA_ROOT
        js = ('js/ckeditor/ckeditor.js', 'js/ckeditor/config.js')

    def __init__(self, attrs=None):
        self.attrs = {}
        if attrs and isinstance(attrs, dict):
            self.attrs.update(attrs)
        super(CKEditorSimple, self).__init__(self.attrs)

    def render(self, name, value, attrs=None):
        parrent_render = super(CKEditorSimple, self).render(name, value, attrs)
        child_render = u'''<script type="text/javascript">
                               CKEDITOR.replace('id_%s');
                           </script>''' % name
        return mark_safe('<br/><br/>') + parrent_render + mark_safe(child_render)
