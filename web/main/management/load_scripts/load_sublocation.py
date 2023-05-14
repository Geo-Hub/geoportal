import os
from django.contrib.gis.utils import LayerMapping
from models import KiambuSublocation

# Auto-generated `LayerMapping` dictionary for KiambuDivision model
# Auto-generated `LayerMapping` dictionary for KiambuLocations model
# Auto-generated `LayerMapping` dictionary for KiambuSublocations model
kiambusublocations_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'id_3' : 'ID_3',
    'name_3' : 'NAME_3',
    'id_4' : 'ID_4',
    'name_4' : 'NAME_4',
    'id_5' : 'ID_5',
    'name_5' : 'NAME_5',
    'type_5' : 'TYPE_5',
    'engtype_5' : 'ENGTYPE_5',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}

kiambusublocations_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'data/KiambuSublocation.shp'))
def run (verbose=True):
	lm = LayerMapping(KiambuSublocation, kiambusublocations_shp, kiambusublocations_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)