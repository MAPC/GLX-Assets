from django.template import RequestContext
from django.shortcuts import render_to_response

from asset.models import Asset, AssetForm

# Create your views here.
def index(request):
    
    return render_to_response('asset/index.html', {
            },
            context_instance=RequestContext(request)
        )
    
def new(request):
    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.ip = request.META['REMOTE_ADDR']
            entry.save()
            return render_to_response('asset/thanks.html',
                                      {'asset': entry},
                                      context_instance=RequestContext(request))            
    else:
        form = AssetForm()
        
    return render_to_response('asset/new.html', 
                              {'form': form, 
                               }, 
                               context_instance=RequestContext(request))    