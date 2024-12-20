from pydantic import BaseModel

from health_app.lib.process_fhir_file import parse_item


class MetaModel(BaseModel):
    profile: list[str] = []


class ItemModel(BaseModel):
    resourceType: str
    id: str
    meta: MetaModel | None = None


def test_validate_item_success():
    item = {
        "resourceType": "Dummy",
        "id": "1234abc",
        "meta": {"profile": ["http://some/dummy/url"]},
    }
    assert parse_item(item, ItemModel) == ItemModel(
        resourceType="Dummy",
        id="1234abc",
        meta=MetaModel(profile=["http://some/dummy/url"]),
    )


def test_validate_item_failure_missing_field():
    item = {"resourceType": "Dummy", "meta": {"profile": ["http://some/dummy/url"]}}
    assert parse_item(item, ItemModel) == False
