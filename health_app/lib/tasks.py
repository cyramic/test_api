import json
import logging

from celery import Celery
from decouple import config

from health_app.lib.db import get_db_session, save_to_db
from health_app.lib.file import get_temp_fs
from health_app.lib.process_fhir_file import validate_file

redis_url = config("REDIS_URL", default="redis://localhost:6379")
upload_dir = config("UPLOAD_DIR", default="osfs:///tmp/uploads")
database_url = config(
    "DATABASE_URL", default="postgresql://postgres:postgres@127.0.0.1:5432/db"
)

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)
celery = Celery(__name__, broker=redis_url, backend=redis_url)

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def store_data(resource) -> bool:
    """
    Stores a validated record into the database.

    Parameters:
    item: A model object to store in the database

    Returns:
    bool: whether the storage was successful or not
    """
    log.info("Storing Data in database...")
    res = False
    with get_db_session(database_url) as db:
        res = save_to_db(resource, db)
    return res


@celery.task
def process_file(file: str):
    """
    A celery task to handle processing an uploaded file
    separate from the API itself

    Parameters:
    A filename to parse from temporary storage

    Returns:
    None
    """
    log.info(f"Processing uploaded file {file}")
    file_fs = get_temp_fs(upload_dir)
    if not file_fs:
        log.error(f"Could not access upload directory: {upload_dir}")
        return False
    with file_fs.open(file, "r") as f:
        data = json.loads(f.read())
        items = validate_file(data)
        if items:
            log.debug(f"Storing {len(items)} items to database")
            for item in items:
                res = store_data(item)
        else:
            log.error("Could not process file")
            return False
