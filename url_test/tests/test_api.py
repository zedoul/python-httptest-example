# -*- coding: utf-8 -*-

import json

def test_number_of_elements_in_list(setting, responses):
    assert len(responses.get("/catches").json()) == \
               setting.get('apis').get('catches').get('number_of_elements')
    assert len(responses.get("/species").json()) == \
               setting.get('apis').get('species').get('number_of_elements')
    assert len(responses.get("/methods").json()) == \
               setting.get('apis').get('methods').get('number_of_elements')

def test_specific_element_with_verbosity(setting, responses):
    assert len(responses.get("/catches/81?verbosity=1").json()) == \
               setting.get('apis').get('catches_verb_1').get('number_of_elements')
    assert len(responses.get("/catches/81?verbosity=2").json()) == \
               setting.get('apis').get('catches_verb_2').get('number_of_elements')
    assert len(responses.get("/catches/81?verbosity=3").json()) == \
               setting.get('apis').get('catches_verb_3').get('number_of_elements')

def test_input_error_handlings(setting, responses):
    response = responses.get("/catches/-1")
    assert str(response.json()) == \
               str(setting.get('apis').get('catches_errorcase_1').get('error_msg'))
    response = responses.get("/catches/asdf")
    assert str(response.json()) == \
               str(setting.get('apis').get('catches_errorcase_2').get('error_msg'))
    response = responses.get("/species/-1")
    assert str(response.json()) == \
               str(setting.get('apis').get('species_errorcase_1').get('error_msg'))
#    response = responses.get("/species/asdf")
#    assert str(response.json()) == \
#               str(setting.get('apis').get('species_errorcase_2').get('error_msg'))
    response = responses.get("/methods/-1")
    assert str(response.json()) == \
               str(setting.get('apis').get('methods_errorcase_1').get('error_msg'))
    response = responses.get("/methods/asdf")
    assert str(response.json()) == \
               str(setting.get('apis').get('methods_errorcase_2').get('error_msg'))

def test_moments(setting, responses):
    response = responses.get("/moments")
    assert str(response.json()) == str({u'errors': [u'You are not authorized to perform that action']})
