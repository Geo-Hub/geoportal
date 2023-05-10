import os
from django.contrib.gis.utils import LayerMapping
from models import Shamba

# Auto-generated `LayerMapping` dictionary for Shamba model
shamba_mapping = {
    'objectid_1' : 'OBJECTID_1',
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'y_coordina' : 'Y_coordina',
    'x_coordina' : 'X_coordina',
    'perimeter' : 'Perimeter',
    'parcel_no' : 'parcel_No',
    'owner' : 'Owner',
    'soil_type' : 'soil_type',
    'state' : 'State',
    'cost_value' : 'cost_value',
    'pic_url' : 'pic_url',
    'electricit' : 'Electricit',
    'water' : 'Water',
    'outlinetra' : 'OutlineTra',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

shamba_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
	'data/realwgs84.shp'))
def run (verbose=True):
	lm = LayerMapping(Shamba, shamba_shp, shamba_mapping,transform=False,encoding='iso-8859-1')
	lm.save(strict=True, verbose=verbose)