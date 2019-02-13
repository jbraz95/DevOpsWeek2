import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util


def persons_get(pageSize=None, pageNumber=None):  # noqa: E501
    """Gets some persons

    Returns a list containing all persons. The list supports paging. # noqa: E501

    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'


def persons_post(person=None):  # noqa: E501
    """Creates a person

    Adds a new person to the persons list. # noqa: E501

    :param person: The person to create.
    :type person: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def persons_username_delete(username):  # noqa: E501
    """Deletes a person

    Delete a single person identified via its username # noqa: E501

    :param username: The person&#39;s username
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def persons_username_friends_get(username, pageSize=None, pageNumber=None):  # noqa: E501
    """Gets a person&#39;s friends

    Returns a list containing all persons. The list supports paging. # noqa: E501

    :param username: The person&#39;s username
    :type username: str
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'


def persons_username_get(username):  # noqa: E501
    """Gets a person

    Returns a single person for its username. # noqa: E501

    :param username: The person&#39;s username
    :type username: str

    :rtype: Person
    """
    return 'do some magic!'
