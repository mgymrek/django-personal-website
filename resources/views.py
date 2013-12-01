from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from publications.models import Resource

def index(request):
    resources = Resource.objects.all().order_by("-date")
    return render_to_response('resources/index.html', {'resources': resources}, context_instance=RequestContext(request))
