import logging

import fhir
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

log = logging.getLogger(__name__)

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"
    id = Column(String, primary_key=True)
    name = Column(String)
    birthDate = Column(String)


class Observation(Base):
    __tablename__ = "observation"
    id = Column(String, primary_key=True)
    status = Column(String)
    effectiveDateTime = Column(String)
    valueQuantity_value = Column(Integer)
    valueQuantity_unit = Column(String)
    patient_id = Column(String, ForeignKey("patient.id"))
    patient = relationship("Patient")


def parse_and_map_fhir_resource(resource):
    """
    This function matches an FHIR model to the database

    Parameters:
    resource: A validated FHIR resource

    Returns:
    Record: A new record to be stored in the database that matches the FHIR model
    """

    if isinstance(resource, fhir.resources.patient.Patient):
        log.info("Patient")
        record = Patient(
            id=resource.id, name=resource.name[0].text, birthDate=resource.birthDate
        )
    elif isinstance(resource, fhir.resources.careplan.CarePlan):
        log.info("Care Plan not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.careteam.CareTeam):
        log.info("Care Team not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.diagnosticreport.DiagnosticReport):
        log.info("Diagnostic Report not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.documentreference.DocumentReference):
        log.info("Document Reference not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.encounter.Encounter):
        log.info("Encounter not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.explanationofbenefit.ExplanationOfBenefit):
        log.info("Explanation of Benefit not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.immunization.Immunization):
        log.info("Immunization not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.medicationrequest.MedicationRequest):
        log.info("Medication Request not implemented yet")
        record = None
    elif isinstance(resource, fhir.resources.observation.Observation):
        log.info("Observation")
        record = Observation(
            id=resource.id,
            status=resource.status,
            effectiveDateTime=resource.effectiveDateTime,
            valueQuantity_value=resource.valueQuantity_value,
            valueQuantity_unit=resource.valueQuantity_unit,
            patient_id=resource.pateint_id,
            patient=resource.patient,
        )
    elif isinstance(resource, fhir.resources.procedure.Procedure):
        log.info("Procedure not implemented yet")
        return None
    elif isinstance(resource, fhir.resources.provenance.Provenance):
        log.info("provenance not implemented yet")
        return None
    else:
        # Handle other resource types or raise an error
        log.error(f"Unsupported resource type: {type(resource)}")
        return None
    return record
