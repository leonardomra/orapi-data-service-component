import connexion
import six
import jwt
import os
from jwt.algorithms import get_default_algorithms
from data_module.models.health import Health  # noqa: E501
from data_module import util
from flask import jsonify

from urhandler.user_handler import UserHandler
import botocore

ur = UserHandler(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])

def data_health_get():  # noqa: E501
    """data_health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    
    accessToken = connexion.request.headers['Authorization']
    decodedAccessToken = jwt.decode(accessToken.replace('Bearer ', ''), verify=False)
    print(decodedAccessToken['sub'], flush=True)
    print(os.environ['AWS_USERPOOL_ID'], flush=True)
    print(decodedAccessToken, flush=True)

    user = None
    try:
        user = ur.getUser(os.environ['AWS_USERPOOL_ID'], decodedAccessToken['username'])
    except botocore.exceptions.ClientError as e:
        print(e)
   
    
    response = {
        'status' : 'Data Service Component is up!'
    }
    print('Heatlh check executed.', flush=True)
    return jsonify(response)
