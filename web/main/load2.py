import os
from django.contrib.gis.utils import LayerMapping
from models import KiambuCounty

# Auto-generated `LayerMapping` dictionary for KiambuCounty model
kiambucounty_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'varname_2' : 'VARNAME_2',
    'nl_name_2' : 'NL_NAME_2',
    'hasc_2' : 'HASC_2',
    'cc_2' : 'CC_2',
    'type_2' : 'TYPE_2',
    'engtype_2' : 'ENGTYPE_2',
    'validfr_2' : 'VALIDFR_2',
    'validto_2' : 'VALIDTO_2',
    'remarks_2' : 'REMARKS_2',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}

kiambu_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'data/kiambucounty.shp'))
def run (verbose=True):
	lm = LayerMapping(KiambuCounty, kiambu_shp, kiambucounty_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)