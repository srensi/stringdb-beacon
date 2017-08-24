# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.statement_object import StatementObject
from swagger_server.models.statement_predicate import StatementPredicate
from swagger_server.models.statement_subject import StatementSubject
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Statement(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, subject: StatementSubject=None, predicate: StatementPredicate=None, object: StatementObject=None):
        """
        Statement - a model defined in Swagger

        :param id: The id of this Statement.
        :type id: str
        :param subject: The subject of this Statement.
        :type subject: StatementSubject
        :param predicate: The predicate of this Statement.
        :type predicate: StatementPredicate
        :param object: The object of this Statement.
        :type object: StatementObject
        """
        self.swagger_types = {
            'id': str,
            'subject': StatementSubject,
            'predicate': StatementPredicate,
            'object': StatementObject
        }

        self.attribute_map = {
            'id': 'id',
            'subject': 'subject',
            'predicate': 'predicate',
            'object': 'object'
        }

        self._id = id
        self._subject = subject
        self._predicate = predicate
        self._object = object

    @classmethod
    def from_dict(cls, dikt) -> 'Statement':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Statement of this Statement.
        :rtype: Statement
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Statement.
        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)

        :return: The id of this Statement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Statement.
        CURIE-encoded identifier for statement (can be used to retrieve associated evidence)

        :param id: The id of this Statement.
        :type id: str
        """

        self._id = id

    @property
    def subject(self) -> StatementSubject:
        """
        Gets the subject of this Statement.

        :return: The subject of this Statement.
        :rtype: StatementSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject: StatementSubject):
        """
        Sets the subject of this Statement.

        :param subject: The subject of this Statement.
        :type subject: StatementSubject
        """

        self._subject = subject

    @property
    def predicate(self) -> StatementPredicate:
        """
        Gets the predicate of this Statement.

        :return: The predicate of this Statement.
        :rtype: StatementPredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate: StatementPredicate):
        """
        Sets the predicate of this Statement.

        :param predicate: The predicate of this Statement.
        :type predicate: StatementPredicate
        """

        self._predicate = predicate

    @property
    def object(self) -> StatementObject:
        """
        Gets the object of this Statement.

        :return: The object of this Statement.
        :rtype: StatementObject
        """
        return self._object

    @object.setter
    def object(self, object: StatementObject):
        """
        Sets the object of this Statement.

        :param object: The object of this Statement.
        :type object: StatementObject
        """

        self._object = object

