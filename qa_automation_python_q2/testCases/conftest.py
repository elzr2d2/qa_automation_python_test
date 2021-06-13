import calendar
import time
import requests
import json
import pytest
from selenium import webdriver
from utilities.logger import LogGen
from utilities.readProperties import ReadConfig
from utilities.convertJson import convertJson


@pytest.fixture
def data_body(key, value, value_type):
    data_body = json.dumps({
        "data": [
            {
                "key": key,
                "val": value,
                "valType": value_type
            }
        ]
    })

    return data_body
