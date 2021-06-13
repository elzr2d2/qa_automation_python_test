import unittest

from actionObjects import http_requests
from utilities.readProperties import ReadConfig


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.hr = http_requests
        self.username = ReadConfig.get_username()
        self.password = ReadConfig.get_password()

    def test_valid_login(self):
        response = self.hr.create_token(self.username, self.password)

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert False
        else:
            assert True

    def test_invalid_username(self):
        response = self.hr.create_token("not a username", self.password)

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_invalid_password(self):
        response = self.hr.create_token(self.username, "not a password")

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_invalid_username_and_password(self):
        response = self.hr.create_token("not a username", "not a password")

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_empty_username(self):
        response = self.hr.create_token(None, self.password)

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_empty_password(self):
        response = self.hr.create_token(self.username, None)

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_empty_username_and_password(self):
        response = self.hr.create_token(None, None)

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False
