from pathlib import Path

from django.contrib.gis.utils import LayerMapping
from main.models import KiambuConstituencies


# Auto-generated `LayerMapping` dictionary for KiambuConstituencies model
kiambuconstituencies_mapping = {
    'objectid': 'OBJECTID',
    'const_nam': 'CONST_NAM',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'population': 'Population',
    'pop_densty': 'Pop_Densty',
    'geom': 'MULTIPOLYGON',
}
constituencies_shp = (Path(__file__).parent / 'data/KiambuConstituencies.shp').as_posix()


def run(verbose=True):
    lm = LayerMapping(KiambuConstituencies, constituencies_shp, kiambuconstituencies_mapping,
                      transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
