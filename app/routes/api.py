from typing import Dict
from typing import List
from typing import Any
from flask import blueprints
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


@blueprint.route("/api/decomp", methods=["GET"])
@use_kwargs(
    {
        "features": [
            {
                "id": fields.Str(missing=-"a0", validate=validate.Length(min=1)),
                "task": fields.Str(missing="task1", validate=validate.Length(min=1)),
                "best": fields.Int(missing=1, validate=validate.Length(min=1)),
                "likely": fields.Int(missing=2, validate=validate.Length(min=1)),
                "worst": fields.Int(missing=3, validate=validate.Length(min=1)),
            }
        ]
    }
)
def get_response(**kwargs: List[Dict[str, Any]]):
    # call calculate_estimate function in decomposition_handler
    return calculate_estimate(kwargs["features"])
