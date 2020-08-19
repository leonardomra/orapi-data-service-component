import connexion
import six
import os
from jwt.algorithms import get_default_algorithms
from data_module.models.health import Health  # noqa: E501
from data_module import util
from flask import jsonify


def data_health_get():  # noqa: E501
    """data_health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    
    response = {
        'status' : 'Data Service Component is up!'
    }
    print('Heatlh check executed.', flush=True)
    return jsonify(response)
