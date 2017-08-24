# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class StatementPredicate(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None):
        """
        StatementPredicate - a model defined in Swagger

        :param id: The id of this StatementPredicate.
        :type id: str
        :param name: The name of this StatementPredicate.
        :type name: str
        """
        self.swagger_types = {
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'StatementPredicate':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatementPredicate of this StatementPredicate.
        :rtype: StatementPredicate
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this StatementPredicate.
        CURIE-encoded identifier of predicate resource 

        :return: The id of this StatementPredicate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this StatementPredicate.
        CURIE-encoded identifier of predicate resource 

        :param id: The id of this StatementPredicate.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this StatementPredicate.
        human readable label of concept

        :return: The name of this StatementPredicate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this StatementPredicate.
        human readable label of concept

        :param name: The name of this StatementPredicate.
        :type name: str
        """

        self._name = name

