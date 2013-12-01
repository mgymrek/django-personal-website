from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from utils import *

def index(request):
    UpdatePublicationDatabase()
    updated_pub_list = Publication.objects.all().order_by('-pubdate')
    return render_to_response('publications/index.html', {'updated_pub_list': updated_pub_list}, context_instance=RequestContext(request))

def article(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    resources = Resource.objects.filter(publication=pub)
    preleases = PressRelease.objects.filter(publication=pub)
    return render_to_response('publications/article.html', {'pub': pub, 'resources': resources, 'preleases': preleases}, context_instance=RequestContext(request))
