import os
from django.contrib.gis.utils import LayerMapping
from models import KiambuConstituencies


# Auto-generated `LayerMapping` dictionary for KiambuConstituencies model
kiambuconstituencies_mapping = {
    'objectid' : 'OBJECTID',
    'const_nam' : 'CONST_NAM',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'population' : 'Population',
    'pop_densty' : 'Pop_Densty',
    'geom' : 'MULTIPOLYGON',
}
constituencies_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
	'data/KiambuConstituencies.shp'))
def run (verbose=True):
	lm = LayerMapping(KiambuConstituencies, constituencies_shp, kiambuconstituencies_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)