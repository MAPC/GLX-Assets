from django.contrib.gis.db import models
from django.forms import ModelForm, HiddenInput, TextInput, RadioSelect

# workaround for South custom fields issues 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^django\.contrib\.gis\.db\.models\.fields\.PointField'])
except ImportError:
    pass

ASSET_CATEGORIES = (
    ('p', 'Preservation'),
    ('c', 'Change'),
)

class Asset(models.Model):
    title = models.CharField('Asset Title', max_length=100,)
    category = models.CharField('Asset Category', max_length=1, choices=ASSET_CATEGORIES)
    ip = models.IPAddressField('IP Address', blank=True, null=True)
    # GeoDjango
    location = models.PointField(geography=True, blank=True, null=True, default='POINT(0 0)') # default SRS 4326
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'%s' % (self.id)

class AssetForm(ModelForm):
    
    class Meta:
        model = Asset
        exclude = ('ip',)
        widgets = {
            'title': TextInput(attrs={'size': '100'}),
            'category': RadioSelect(),
            'location': HiddenInput(),         
        }