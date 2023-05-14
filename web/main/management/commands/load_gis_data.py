from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError, CommandParser

class Command(BaseCommand):
    help = "Loads the shapefile data into the relevant DB tables."

    def handle(self, *args: Any, **options: Any) -> str | None:
        from main.management.load_scripts import load_county
        load_county.run()
