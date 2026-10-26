import os
import shutil
import zipfile
from pathlib import Path
from typing import Any

from django.core.management.base import BaseCommand, CommandError
from main.models import KiambuConstituencies, KiambuCounty, Shamba

# data.zip holds a top-level data/ folder of shapefiles; the load scripts read
# them from main/management/load_scripts/data/. It is kept out of the image and
# mounted read-only by the compose files (web/data.zip -> /seed/data.zip).
DATA_ZIP = Path(os.environ.get("GIS_DATA_ZIP", "/seed/data.zip"))
LOAD_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "load_scripts"


class Command(BaseCommand):
    help = (
        "Loads the shapefile data into the relevant DB tables. Safe to run on "
        "every start: only empty tables are loaded, and data.zip is only "
        "extracted when something needs loading."
    )

    def handle(self, *args: Any, **options: Any):
        from main.management.load_scripts import (
            load_constituencies,
            load_county,
            load_shambas,
        )

        loaders = [
            ("Kiambu County", KiambuCounty, load_county.run),
            ("Kiambu Constituencies", KiambuConstituencies, load_constituencies.run),
            ("Shamba", Shamba, load_shambas.run),
        ]
        pending = []
        for name, model, run in loaders:
            if model.objects.exists():
                print(f"{name} already exists. Skipping...")
            else:
                pending.append((name, run))
        if not pending:
            return
        if not DATA_ZIP.is_file():
            raise CommandError(
                f"GIS tables are empty but {DATA_ZIP} was not found; mount "
                "web/data.zip there (see compose.*.yaml) or set GIS_DATA_ZIP."
            )

        with zipfile.ZipFile(DATA_ZIP) as archive:
            archive.extractall(LOAD_SCRIPTS_DIR)
        try:
            for name, run in pending:
                print(f"Loading {name}...")
                run()
        finally:
            shutil.rmtree(LOAD_SCRIPTS_DIR / "data", ignore_errors=True)
