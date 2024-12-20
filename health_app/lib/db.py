import logging

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from health_app.lib.model import parse_and_map_fhir_resource

log = logging.getLogger(__name__)
Base = declarative_base()


def get_db_session(database_url):
    """
    Retrieves a session with the database

    Parameters:
    database_url: The URL used to connect to the database

    Returns:
    model: a reference to the database
    """
    try:
        engine = create_engine(url=database_url)
    except Exception as err:
        log.error(f"Could not create database engine {err}")
        raise

    try:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
    except Exception as err:
        log.error(f"Unable to create session {err}")
        raise

    try:
        return db
    finally:
        db.close()


def save_to_db(fhir_resource, db) -> bool:
    """
    Saves an FHIR resource to the database based on the model

    Parameters:
    fhir_resource: the record we're trying to fit into the given model
    db: the database connection

    Returns:
    bool: True if success, False if failed.
    """
    try:
        model_instance = parse_and_map_fhir_resource(fhir_resource)
    except Exception as err:
        log.error(f"Problem mapping data to model {err}")
        return False

    if model_instance:
        try:
            db.add(model_instance)
            db.commit()
            db.refresh(model_instance)
        except Exception as err:
            log.error(f"Problem Committing Update: {err}")
            return False
        return True
    return False
