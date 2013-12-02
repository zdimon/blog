# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
import os
from sorl.thumbnail import get_thumbnail

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value:
            image = get_thumbnail(value.path, '130x100', crop='center', quality=99)
            output.append(u' <div style="float:right; padding: 10px 20px 10px 300px;"><a href="%s" target="_blank"><img src="%s" alt="%s" /></a></div> %s ' % \
                (value.url, image.url, image.url, u'Изменить:'))
        output.append(u'<div sttyle="float:left">'+super(AdminFileWidget, self).render(name, value, attrs)+u'</div>')
        return mark_safe(u''.join(output))