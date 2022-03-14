import typing as tp

if tp.TYPE_CHECKING:
    from user_auth.models import LoginToken


class TokenOperation(object):

    def __init__(self, token_instance: "LoginToken"):
        self.token_instance = token_instance
