import os
from django.contrib.gis.utils import LayerMapping
from models import KiambuDivision

# Auto-generated `LayerMapping` dictionary for KiambuDivision model
kiambudivisions_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'id_3' : 'ID_3',
    'name_3' : 'NAME_3',
    'varname_3' : 'VARNAME_3',
    'nl_name_3' : 'NL_NAME_3',
    'hasc_3' : 'HASC_3',
    'type_3' : 'TYPE_3',
    'engtype_3' : 'ENGTYPE_3',
    'validfr_3' : 'VALIDFR_3',
    'validto_3' : 'VALIDTO_3',
    'remarks_3' : 'REMARKS_3',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}

kiambudivisions_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'data/KiambuDivision.shp'))
def run (verbose=True):
	lm = LayerMapping(KiambuDivision, kiambudivisions_shp, kiambudivisions_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)