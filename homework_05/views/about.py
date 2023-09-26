from dataclasses import dataclass, field

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound

about = Blueprint(
    "about",
    __name__,
    url_prefix="/about",
)

@about.get("/", endpoint="about")
def get_products_list():
    return render_template(
        "about.html"
    )