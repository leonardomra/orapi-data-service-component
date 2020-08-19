import connexion
import six
import botocore
import time
import uuid
import os
import jwt
import io
from data_module.models.dataset import Dataset  # noqa: E501
from data_module import util
from urhandler.user_handler import UserHandler
from dbhandler.mysql_handler import MySQLHandler
from data_module.models.datacomplex import DataComplex
from s3handler.s3_handler import S3Handler
from flask import request
from werkzeug.utils import secure_filename

db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])
ur = UserHandler(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])
s3 = S3Handler(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])

def data_kind_get(kind, limit=None):  # noqa: E501
    """data_kind_get

    Obtain information about files. # noqa: E501

    :param kind: Kind of data.
    :type kind: str
    :param limit: The amount of files to be returned.
    :type limit: int

    :rtype: List[Dataset]
    """
    return 'do some magic!'


def data_kind_id_delete(id, kind):  # noqa: E501
    """data_kind_id_delete

    Use this endpoint to delete a specific dataset. # noqa: E501

    :param id: Id of dataset.
    :type id: 
    :param kind: Kind of data.
    :type kind: str

    :rtype: Dataset
    """
    return 'do some magic!'


def data_kind_id_get(id, kind):  # noqa: E501
    """data_kind_id_get

    Use this endpoint to obtain metadata of specific dataset. # noqa: E501

    :param id: Id of dataset.
    :type id: 
    :param kind: Kind of data.
    :type kind: str

    :rtype: Dataset
    """
    return 'do some magic!'


def data_kind_id_put(id, kind, label):  # noqa: E501
    """data_kind_id_put

    Use this endpoint to modify the mentadata of a specific dataset. # noqa: E501

    :param id: Id of dataset.
    :type id: 
    :param kind: Kind of data.
    :type kind: str
    :param label: Label of dataset.
    :type label: str

    :rtype: Dataset
    """
    return 'do some magic!'


def data_kind_upload_post(kind, file=None, label=None):  # noqa: E501
    """data_kind_upload_post

    Upload a dataset in CSV format. # noqa: E501

    :param kind: Kind of data.
    :type kind: str
    :param file_name: 
    :type file_name: strstr
    :param label: 
    :type label: str

    :rtype: Dataset
    """

    dataset = DataComplex()
    dataset.id = str(uuid.uuid4())

    try:
        dataset.file_name = connexion.request.files['file'].filename
    except Exception:
        return '"file" parameter expected.', 400 
    
    try:
        dataset.label = connexion.request.form['label']
    except Exception:
        return '"label" parameter expected.', 400

    try:
        dataset.kind = kind
    except Exception:
        return '"label" parameter expected.', 400 

    try:
        dataset.format = connexion.request.files['file'].mimetype
    except Exception:
        return '"format" parameter expected.', 400 

    # get tocken
    accessToken = connexion.request.headers['Authorization']
    decodedAccessToken = jwt.decode(accessToken.replace('Bearer ', ''), verify=False)
    userId = decodedAccessToken['sub']
    
    # check/create bucket
    bucketName = 'openresearch' 
    s3.createBucket(bucketName.lower())
    s3.listBuckets()
    
    # get file to store
    _file = request.files['file']
    inMemoryFile = io.BytesIO(_file.read())
    inMemoryFile.seek(0)
   
    # store s3
    key = userId + '/' + secure_filename(dataset.file_name)
    existingKeys = s3.listObjectsInBucket(bucketName, userId + '/')
    if key in existingKeys:
        return 'file name already exists. Either delete the file from storage or rename it.', 400 

    s3Resp = s3.uploadFileObject(inMemoryFile.read(), bucketName, key)
    # inMemoryFile.getbuffer(), inMemoryFile.getvalue()
    
    if s3Resp:
        dataset.location = bucketName + '/' + key
        # store persistent data
        add_dataset = ("INSERT INTO Data "
                "(id, fileName, format, kind, label, location) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
        data_dataset = (dataset.id, dataset.file_name, dataset.format, dataset.kind, dataset.label, dataset.location)
        db.add(add_dataset, data_dataset)

    return dataset

