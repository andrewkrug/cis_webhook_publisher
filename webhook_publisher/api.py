import json
import logging
from flask import Flask
from flask import jsonify
from flask_cors import cross_origin
from webhook_publisher.idp import requires_auth
from webhook_publisher.idp import requires_scope
from webhook_publisher.exceptions import AuthError
from webhook_publisher import __version__

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# This doesn't need authentication
@app.route("/version")
@cross_origin(headers=['Content-Type', 'Authorization'])
def version():
    response = __version__
    return jsonify(message=response)

@app.route("/v1/profile", methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@cross_origin(headers=["Access-Control-Allow-Origin", "*"])
def profile():
    if requires_scope("write:user_profile"):
        profile_data = json.loads(request.data)

        # Parse the profile data

        # Query the auth0 management api?

        # Create a CIS Change

        # Send to CIS

        # Return the result of lambda invocation ( kinesis stream sequence number ? )
    else:
        raise AuthError({
            "code": "Unauthorized",
            "description": "You don't have access to this resource."
        }, 403)

# This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=['Content-Type', 'Authorization'])
def public():
    response = "Hello from a public endpoint!"
    return jsonify(message=response)


# This does need authentication
@app.route("/api/private")
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def private():
    response = "Hello from a private endpoint!"
    return jsonify(message=response)


@app.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "*"])
@requires_auth
def private_scoped():
    """A valid Access Token and an appropriate scope are required to access this route
    """
    if requires_scope("read:messages"):
        response = "Hello from a private endpoint!."
        return jsonify(message=response)
