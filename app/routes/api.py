from typing import Dict
from flask import blueprints
from marshmallow import fields
from marshmallow import validate
from webargs.flaskparser import use_kwargs


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
