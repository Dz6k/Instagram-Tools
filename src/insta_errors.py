class InvalidFormatError(Exception):
    def __init__(self, msg="Wrong url format. Send format: https://www.website.com/p/linkID"):
        self.msg = msg
        super().__init__(self.msg)
        # -------------------------------------------- #
    

class InvalidZeroParamError(Exception):
    def __init__(self, msg="Number 0(zero) is not accept"):
        self.msg = msg
        super().__init__(self.msg)
        # -------------------------------------------- #


class ExpiredCookiesError(Exception):
    def __init__(self, msg="maybe your cookies was expired! Try login before!"):
        self.msg = msg
        super().__init__(self.msg)
        # -------------------------------------------- #


class XPathInstagramError(Exception):
    def __init__(self, msg="Update or change your XPath"):
        self.msg = msg
        super().__init__(self.msg)
        # -------------------------------------------- #
