"""Module for IQ Option http auth resource."""

from exnova.http.resource import Resource


class Auth(Resource):
    """Class for IQ Option http auth resource."""

    # pylint: disable=too-few-public-methods

    url = "auth"
