from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):
    help = "Loads the shapefile data into the relevant DB tables."

    def handle(self, *args: Any, **options: Any):
        from main.management.load_scripts import (
            load_county,
            load_constituencies,
            load_shambas
        )
        load_county.run()
        load_constituencies.run()
        load_shambas.run()
