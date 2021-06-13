from actionObjects import http_requests
from utilities.readProperties import ReadConfig
import unittest


class Test_Data_Object(unittest.TestCase):
    def setUp(self):
        self.hr = http_requests
        self.username = ReadConfig.get_username()
        self.password = ReadConfig.get_password()

        self.token = self.hr.create_token(self.username, self.password)

    def test_valid_data_creation(self, data_body):
        key = "key1"
        value = "value1"
        value_type = "str"
        response = self.hr.post_request(self.token, data_body(key, value, value_type))

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert False
        else:
            assert True

    def test_duplicate_data_creation(self, data_body):
        key = "key2"
        value = "value2"
        value_type = "str"
        response1 = self.hr.post_request(self.token, data_body(key, value, value_type))

        key = "key2"
        value = "value2"
        value_type = "str"
        response2 = self.hr.post_request(self.token, data_body(key, value, value_type))

        if not response1 or response2:
            assert False
        elif "AuthenticationFailed" in response1 or "AuthenticationFailed" in response2:
            assert True
        else:
            assert False

    def test_missing_key(self, data_body):
        key = None
        value = "value2"
        value_type = "str"
        response = self.hr.post_request(self.token, data_body(key, value, value_type))

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_missing_value(self, data_body):
        key = "key3"
        value = None
        value_type = "str"
        response = self.hr.post_request(self.token, data_body(key, value, value_type))

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False

    def test_missing_key_and_value(self, data_body):
        key = None
        value = None
        value_type = "str"
        response = self.hr.post_request(self.token, data_body(key, value, value_type))

        if not response:
            assert False
        elif "AuthenticationFailed" in response:
            assert True
        else:
            assert False
