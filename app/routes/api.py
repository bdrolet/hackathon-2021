from app.models.issue import IssueType
from app.models.issue import CreateIssueResp, Issue
from app.models import create_issue_resp, create_issue_req
from app.services.jira import jira_client
from typing import Dict
from typing import Any
from flask import blueprints
from flask import request
from marshmallow import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs, use_args
from app.handlers.decomposition_handler import calculate_estimate
from app.handlers.fuzzy_logic_handler import calculate_fuzzy_estimate
from app.handlers.t_shirt_handler import get_net_business_value


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


@blueprint.route("/api/t-shirt", methods=["POST"])
def get_t_shirt_response() -> Dict[str, Any]:
    # call get_net_business_value function in t_shirt_handler
    return get_net_business_value(request.json["features"])


@blueprint.route("/api/issue/create", methods=["POST"])
def create_issue() -> CreateIssueResp:
    data = create_issue_req.load(request.get_json())
    issue = jira_client.create_issue(
        name=data["name"],
        story_points=data["story_points"] if "story_points" in data else None,
        issue_type=data["issue_type"]
    )
    return create_issue_resp.dump(obj=issue)
