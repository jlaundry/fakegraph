
from datetime import datetime
from http import HTTPStatus
import json
import uuid

from flask import Flask, jsonify, make_response

app = Flask(__name__)

USERS = json.load(open('data/users.json', 'r'))

JSONIFY_PRETTYPRINT_REGULAR = True

def error_response(code, message, http_status=404):
    client_request_id = str(uuid.uuid4())
    return make_response(
        jsonify({
            "error": {
                "code": code,
                "message": message,
                "innerError": {
                    "date": datetime.utcnow().isoformat(),
                    "request-id": client_request_id,
                    "client-request-id": client_request_id
                }
            }
        }),
        http_status
    )

@app.errorhandler(404)
def page_not_found(e):
    return error_response(
        "BadRequest",
        e.description,
        404
    )

@app.route("/")
def root():
    return "Yes, and?"

@app.route("/v1.0/users")
@app.route("/beta/users")
def users():
    return jsonify({
        "@odata.context": "https://graph.microsoft.com/beta/$metadata#users",
        "value": USERS,
    }, )

@app.route("/v1.0/users/<uuid:id>")
@app.route("/beta/users/<uuid:id>")
def user_select(id):
    id = str(id)
    try:
        user = [x for x in USERS if x['id'] == id][0]
    except IndexError:
        return error_response(
            "Request_ResourceNotFound",
            f"Resource '{id}' does not exist or one of its queried reference-property objects are not present.",
            404
        )
        
    user["@odata.context"] = "https://graph.microsoft.com/beta/$metadata#users"
    return jsonify(user)
