import connexion
import six

from data_module.models.dataset import Dataset  # noqa: E501
from data_module import util


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


def data_kind_upload_post(kind, file_name=None, label=None):  # noqa: E501
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
    return 'do some magic!'
