# -*- coding: utf-8 -*-

import pytest
import requests
import yaml

@pytest.fixture
def setting(scope='session'):
    with open("api.yaml") as f:
        _setting = yaml.load(f)
    return _setting

@pytest.fixture(scope='function')
def responses(setting):
    hosturl = setting.get('hosturl')
    CONNECTION_TIMEOUT = setting.get('connection_timeout')
    READ_TIMEOUT = setting.get('read_timeout')

    responses = {}

    try:
        for _, api in setting.get('apis').iteritems():
            response = requests.get(url= hosturl + api.get('url'), \
                                  verify=True,
                                  timeout=(CONNECTION_TIMEOUT, \
                                           READ_TIMEOUT))
            responses[api.get('url')] = response

    # DNS look up fail
    except requests.exceptions.ConnectionError as e: 
        pytest.fail(e.args, 'The domain does not exist')
    # Timeout: connection
    except requests.exceptions.ConnectTimeout as e: 
        pytest.fail(e.args, 'connection time took more than %s ' % \
                           str(CONNECTION_TIMEOUT))
    # Timeout: read
    except requests.exceptions.ReadTimeout as e: 
        pytest.fail(e.args, 'read time took more than %s ' % \
                           str(READ_TIMEOUT))
    # SSL Error
    except requests.exceptions.SSLError as e: # 
        pytest.fail(e.args, 'It is not vertified')
    # etc
    except Exception as e:
        pytest.fail(e)

    return responses
