from typing import Any, Optional

from django.core.management.base import BaseCommand
from main.models import KiambuCounty, KiambuDivision, Shamba


class Command(BaseCommand):
    help = "Loads the shapefile data into the relevant DB tables."

    def handle(self, *args: Any, **options: Any):
        from main.management.load_scripts import (
            load_constituencies,
            load_county,
            load_shambas,
        )

        if KiambuCounty.objects.count() == 0:
            load_county.run()
        else:
            print("Kiambu County already exists. Skipping...")
        if KiambuDivision.objects.count() == 0:
            load_constituencies.run()
        else:
            print("Kiambu Division already exists. Skipping...")
        if Shamba.objects.count() == 0:
            load_shambas.run()
        else:
            print("Shamba already exists. Skipping...")
