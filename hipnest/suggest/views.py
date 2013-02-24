from django.shortcuts import render_to_response
from django.template import RequestContext
import suggest.suggestion as suggest

def index(request):
  return render_to_response('base.html', { "echonest_api_key" : suggest.echonest_api_key},
                                        context_instance=RequestContext(request))
