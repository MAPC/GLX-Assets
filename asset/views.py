from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml

from asset.models import Asset, AssetForm

# Create your views here.
def index(request):
    
    assets  = Asset.objects.all()
    
    return render_to_response('asset/index.html', 
            {'assets' : assets},
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
    
def detail(request, asset_id):
    asset = Asset.objects.get(pk=asset_id)
    return render_to_response('asset/detail.html',
                            {'asset': asset,
                             },
                            context_instance=RequestContext(request)) 
    
def kml(request):
     assets  = Asset.objects.kml()
     return render_to_kml('asset/assets.kml', 
                            {'assets' : assets},
                            context_instance=RequestContext(request)) 