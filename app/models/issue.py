from typing import Optional
from enum import Enum
from marshmallow import fields
from marshmallow.schema import Schema
from dataclasses import dataclass
from marshmallow_enum import EnumField


@dataclass
class IssueType(Enum):
    UNKNOWN = 0
    EPIC = "Epic"
    STORY = "Story"
    TASK = "Task"
    BUG = "Bug"


@dataclass
class Issue:
    id: str
    name: str
    issue_type: IssueType
    url: str
    story_points: Optional[int]


class CreateIssueReq(Schema):
    name = fields.Str(required=True)
    issue_type = EnumField(IssueType)
    story_points = fields.Int(required=False)


class CreateIssueResp(Schema):
    id = fields.Str(required=True)
    url = fields.Url(required=True)
    name = fields.Str(required=True)
    issue_type = EnumField(IssueType)
    story_points = fields.Int(required=False)
