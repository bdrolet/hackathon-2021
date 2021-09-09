from marshmallow import fields
from marshmallow.schema import Schema
from dataclasses import dataclass


@dataclass
class Epic:
    id: str
    name: str
    url: str


class CreateEpicReq(Schema):
    name = fields.Str(required=True)


class CreateEpicResp(Schema):
    id = fields.Str(required=True)
    url = fields.Url(required=True)
    name = fields.Str(required=True)
