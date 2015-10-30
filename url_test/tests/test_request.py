# -*- coding: utf-8 -*-

import pytest
import requests
import json

def test_request_status(setting, responses):
    for _, api in setting.get('apis').iteritems():
        response = responses.get(api.get('url'))

        # HTTP status
        if api.get('raise_for_status_required'):
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                pytest.fail("%s: get an HTTPError (%s)" % \
                            (api.get('url'), e.message))
        else:
            expected_value = api.get('http_status')
            actual_value = response.headers.get('status')

            if expected_value != actual_value:
                pytest.fail("%s: http status %s != %s" % \
                            (api.get('url'), actual_value, expected_value))

def test_request_content_type(setting, responses):
    for _, api in setting.get('apis').iteritems():
        url = api.get('url')
        response = responses.get(url)
        expected_value = api.get('content_type')
        actual_value = response.headers.get('content-type')

        if expected_value != actual_value:
            pytest.fail("%s: content-type %s != %s" % \
                        (url, actual_value, expected_value))

def test_request_content_value(setting, responses):
    for _, api in setting.get('apis').iteritems():
        url = api.get('url')
        response = responses.get(url)

        try:
            response.json()
        except ValueError:
            pytest.fail("%s: json convert fail" % url)

def test_request_content_size(setting, responses):
    for _, api in setting.get('apis').iteritems():
        url = api.get('url')
        response = responses.get(url)
        threshold = int(api.get('content_length_threshold'))
        actual_value = int(response.headers.get('content-length'))

        if  actual_value > threshold:
            pytest.fail("%s: content-size %d > %d" % \
                        (url, actual_value, threshold))
