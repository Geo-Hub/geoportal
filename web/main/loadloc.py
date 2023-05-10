import os
from django.contrib.gis.utils import LayerMapping
from models import KiambuLocation

# Auto-generated `LayerMapping` dictionary for KiambuDivision model
# Auto-generated `LayerMapping` dictionary for KiambuLocations model
kiambulocations_mapping = {
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
    'varname_4' : 'VARNAME_4',
    'type_4' : 'TYPE_4',
    'engtype_4' : 'ENGTYPE_4',
    'validfr_4' : 'VALIDFR_4',
    'validto_4' : 'VALIDTO_4',
    'remarks_4' : 'REMARKS_4',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

kiambulocations_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'data/KiambuLocation.shp'))
def run (verbose=True):
	lm = LayerMapping(KiambuLocation, kiambulocations_shp, kiambulocations_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)