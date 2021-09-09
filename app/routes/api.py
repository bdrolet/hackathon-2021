from app.models.epic import CreateEpicResp, Epic
from typing import Dict
from typing import Any
from flask import blueprints
from flask import request
from marshmallow import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs
from app.handlers.decomposition_handler import calculate_estimate


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


@blueprint.route("/api/jira/epic/create", methods=["POST"])
def create_epic() -> CreateEpicResp:
    # TOOO: create an epic
    epic = Epic(
        id="HACK-1234",
        name="The best feature ever made...probably.",
        url="http://lyft.com",
    )
    return CreateEpicResp().dump(obj=epic)
