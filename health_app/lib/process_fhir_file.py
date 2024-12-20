import logging

from fhir.resources.careplan import CarePlan
from fhir.resources.careteam import CareTeam
from fhir.resources.claim import Claim
from fhir.resources.condition import Condition
from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.documentreference import DocumentReference
from fhir.resources.encounter import Encounter
from fhir.resources.explanationofbenefit import ExplanationOfBenefit
from fhir.resources.immunization import Immunization
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.observation import Observation
from fhir.resources.patient import Patient
from fhir.resources.procedure import Procedure
from fhir.resources.provenance import Provenance
from pydantic import ValidationError
from pydantic.v1.error_wrappers import ValidationError as ValidationErrorV1

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

MODELS = {
    "Patient": Patient,
    "Condition": Condition,
    "DiagnosticReport": DiagnosticReport,
    "DocumentReference": DocumentReference,
    "Claim": Claim,
    "ExplanationOfBenefit": ExplanationOfBenefit,
    "Encounter": Encounter,
    "CarePlan": CarePlan,
    "CareTeam": CareTeam,
    "Observation": Observation,
    "Procedure": Procedure,
    "MedicationRequest": MedicationRequest,
    "Immunization": Immunization,
    "Provenance": Provenance,
}


def parse_item(item: dict, model):
    """
    Parses a dictionary into a given model

    Parameters:
    item: the record we're trying to fit into the given model
    model: The model we're trying to use to validate the item

    Returns:
    model: the resulting object, False if the parsing fails.
    """
    try:
        return model(**item)
    except ValidationError as err:
        # log.error(f"Validation of the item failed {err}")
        pass
    except ValidationErrorV1 as err:
        # log.error(f"Validation of the item failed {err}")
        pass
    return False


def validate_file(file_data: dict) -> list:
    """
    This function loops over the data and determines what pieces
    are present.  It will then add these pieces to a stack if they
    are found to match the schemas for that resource type

    Parameters:
    file_data (dict): Unvalidated file data, parsed as JSON/dict

    Returns:
    list: a list of validated records
    """
    items = []
    stack = [file_data]
    while stack:
        current_item = stack.pop()
        if current_item["resourceType"] == "Bundle":
            log.info("Found a bundle. Unpacking...")
            for entry in current_item["entry"]:
                stack.append(entry["resource"])
        else:
            model = MODELS.get(current_item["resourceType"], False)

            if model:
                # log.debug(
                #    f"Parsing item of resource type: {current_item['resourceType']}"
                # )
                item_record = parse_item(current_item, model)
                if item_record:
                    items.append(item_record)
            else:
                log.error(
                    f"Resource type not yet implemented: {current_item['resourceType']}"
                )
    return items
