from featureflagtech.main import FeatureFlag

import pytest
import requests

def validMock(requests_mock):
    requests_mock.get("https://api.featureflag.tech",
    request_headers= {"fft-api-key": "1234"},
    text= "{\"foo\": \"True\"}",
    status_code= 200)

def invalidMock(requests_mock):
    requests_mock.get("https://api.featureflag.tech",
    status_code= 400)

def test_constructor_apiKey():
    with pytest.raises(Exception, match= "apiKey not given"):
        FeatureFlag({"foo": "bar"})

def test_constructor_set_apiKey(requests_mock):
    validMock(requests_mock)
    fft = FeatureFlag({"apiKey": "1234"})
    assert fft.apikey == {"fft-api-key": "1234"}

def test_constructor_inavlid_apiKey(requests_mock):
    invalidMock(requests_mock)
    with pytest.raises(Exception, match= "Invalid API key"):
        FeatureFlag({"apiKey": "invalidKey"})

def test_constructor_set_flags(requests_mock):
    validMock(requests_mock)
    fft = FeatureFlag({"apiKey": "1234"})
    assert fft.flags == {"foo": "True"}

def test_get(requests_mock):
    validMock(requests_mock)
    fft = FeatureFlag({"apiKey": "1234"})
    assert fft.get("foo") == "True"

def test_get_error(requests_mock):
    validMock(requests_mock)
    fft = FeatureFlag({"apiKey": "1234"})
    with pytest.raises(Exception, match= "Flag not found"):
        fft.get("bar")