from app.models.issue import IssueType
from app.models.issue import CreateIssueResp, Issue
from app.models import create_issue_resp, create_issue_req
from typing import Dict
from typing import Any
from flask import blueprints
from flask import request
from marshmallow import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs, use_args
from app.handlers.decomposition_handler import calculate_estimate
from app.handlers.fuzzy_logic_handler import calculate_fuzzy_estimate


blueprint = blueprints.Blueprint("hackathon-2021", __name__)


@blueprint.route("/api/hello", methods=["GET"])
@use_kwargs(
    {"name": fields.Str(missing="world", validate=validate.Length(min=1))},
    location="query",
)
def hello_world(*, name: str) -> Dict[str, str]:
    # your data transformation logic should go in here.
    # Business logic should be made into new modules and called from the endpoint.
    return {"msg": f"Hello, {name}!"}


@blueprint.route("/api/decomp", methods=["POST"])
def get_response() -> Dict[str, Any]:
    # call calculate_estimate function in decomposition_handler
    return calculate_estimate(request.json["features"])


@blueprint.route("/api/fuzzy", methods=["POST"])
def get_fuzzy_response() -> Dict[str, Any]:
    # call calculate_fuzzy_estimate function in fuzzy_logic_handler
    return calculate_fuzzy_estimate(request.json["features"])


@blueprint.route("/api/issue/create", methods=["POST"])
def create_issue() -> CreateIssueResp:
    # TOOO: create an epic

    return create_issue_resp.dump(
        obj=Issue(
            id="HACK-1234",
            name="The best feature ever made...probably.",
            issue_type=IssueType.EPIC.value,
            url="http://lyft.com",
        )
    )
