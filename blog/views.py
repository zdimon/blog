#coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from blog.models import BlogCategory


class CategoryDetailView(DetailView):
    model = BlogCategory
    template_name = 'blogcategory_detail.html'

from blog.models import BlogTopic
class TopicDetailView(DetailView):
    model = BlogTopic
    template_name = 'blogtopic_detail.html'

def home(request):
    return render_to_response('home.html', {},context_instance=RequestContext(request))

# ckeditor
from json import JSONEncoder
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from utils.elFinder import connector as elfConnector
from utils.extras import upload_file_to, find_dir

@csrf_exempt
def connector(request):
    elf_opts={'root':'/www/lessons/blog_ve/blog/media/uploads',
              'URL':'http://localhost:8000/media/uploads',
              'rootAlias':'Server Root',
              'fileURL':True,
              'dotFiles':True,
              'dirSize':True,
              'fileMode':0644,
              'dirMode':0755,
              'imgLib':False,
              'tmbDir':'.tmb',
              'tmbAtOnce':5,
              'tmbSize':48,
              'uploadMaxSize':256,
              'uploadAllow':[],
              'uploadDeny':[],
              'uploadOrder':['allow', 'deny'],
              'defaults':{'read':True, 'write':True, 'rm':True},
              'perms':{},
              'archiveMimes':{},
              'archivers':{},
              'disabled':[],
              'debug':True}

    output=None
    elf=elfConnector(elf_opts)

    if not (request.user.is_authenticated() and request.user.is_active and request.user.is_staff):
        return HttpResponseServerError()

    if request.method == 'GET':
        http_status, http_header, http_response=elf.run(request.GET)
        output=JSONEncoder().encode(http_response)

    if request.method == 'POST':
        cur_cmd=request.POST.get('cmd', False)

        if cur_cmd and cur_cmd == 'upload':
            cur_dir=request.POST.get('current', False)
            files=request.FILES.lists()
            path=find_dir(cur_dir, elf_opts['root'])
            output=upload_file_to(files, path, elf_opts['uploadMaxSize'])
        else:
            http_status, http_header, http_response=elf.run(request.POST)
            output=JSONEncoder().encode(HttpResponse)
    output2 = '''
    {"files": [{"dirs": 1, "hash": "llffim_Lw", "name": "Elfinder images", "read": 1, "volumeid": "llffim_", "ts": 1385880296.0798478, "write": 1, "mime": "directory", "locked": 1, "hidden": 0, "size": "unknown"}, {"dim": "204x204", "hash": "llffim_YnVzLmpwZw", "name": "bus.jpg", "read": 1, "ts": 1385880296.0798478, "write": 1, "tmb": "llffim_YnVzLmpwZw1385880296.08.png", "mime": "image/jpeg", "phash": "llffim_Lw", "locked": 0, "hidden": 0, "size": 5125}], "uplMaxSize": 134217728, "options": {"disabled": ["mkfile", "archive"], "copyOverwrite": 1, "separator": "/", "pathUrl": "/media/images/", "url": "/media/images/", "path": "Elfinder images", "tmbUrl": "/media/images/.tmb/", "archivers": {"create": ["application/x-tar", "application/x-bzip2", "application/x-gzip", "application/zip"], "extract": ["application/x-tar", "application/x-bzip2", "application/x-gzip", "application/zip"]}}, "netDrivers": [], "api": "2.0", "cwd": {"dirs": 1, "hash": "llffim_Lw", "name": "Elfinder images", "read": 1, "volumeid": "llffim_", "ts": 1385880296.0798478, "write": 1, "mime": "directory", "locked": 1, "hidden": 0, "size": "unknown"}}
    '''
    return HttpResponse(output)
