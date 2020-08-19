import connexion
import six
import botocore
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
from werkzeug.utils import secure_filename
from flask import request

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

    # save in disk: simple
    #filenameWithPath = os.path.join('/home' , secure_filename(dataset.file_name))
    #_file.stream.seek(0)
    #_file.save(filenameWithPath)

    # save in disk: complex
    inMemoryFile = io.BytesIO(_file.read())
    inMemoryFile.seek(0)
    #writeToFile(filenameWithPath, inMemoryFile)
    
    # 
    s3.uploadFileObject(inMemoryFile.read(), bucketName, userId + '/' + secure_filename(dataset.file_name))
    #s3.uploadFileObject(_file.read(), bucketName, userId + '/' + secure_filename(dataset.file_name))
    
    
    
    #inMemoryFile.getbuffer()
    #inMemoryFile.getvalue()

    #with connexion.request.files['file'].stream.read() as data:
    #    s3.uploadFileObject(data, bucketName, userId + '/' + 'bl2a.jpg')
    #s3.uploadFileObject(connexion.request.files['file'].stream.read(), bucketName, userId + '/' + 'bl2a.jpg')
    #print(connexion.request.files['file'].read(), flush=True)   

    #connexion.request.files['file'].save(os.path.join('/home' , secure_filename(dataset.file_name)))
    #_file.save(inMemoryFile)
    #inMemoryFile.seek(0)
    #d = connexion.request.files['file'].read()

    #s3.uploadFileObject(d, bucketName, userId + '/' + secure_filename(dataset.file_name))
    
    
    
    
    
    
    """
    print(dataset.location, flush=True)

    dataset.location = 'unknown'
    
    # store persistent data
    add_dataset = ("INSERT INTO Data "
               "(id, fileName, format, kind, label, location) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
    data_dataset = (dataset.id, dataset.file_name, dataset.format, dataset.kind, dataset.label, dataset.location)
    db.add(add_dataset, data_dataset)
    """

    '''
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
    print(user, flush=True)

    print(connexion.request.files['file'], flush=True)
    print(connexion.request.form['label'], flush=True)
    print(kind, flush=True)
    '''

    return 'do some magic!'

def writeToFile(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does
    not exist yet. 
    """
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())