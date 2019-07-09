"""
API version 1 instances/namespaces
"""
from flask import Blueprint
from flask_restplus import Api, Namespace, fields, Resource
from apis.book_api import NS_BOOK

__all__ = ('Api', 'Namespace', 'fields', 'Resource')

__VERSION_ID = 'v1'

BLUEPRINT_API = Blueprint(name=__file__, import_name=__name__)

API_V1 = Api(BLUEPRINT_API, title='Books API', version=__VERSION_ID,
             description='A simple book api', doc='/docs')

# remove default namespace
API_V1.namespaces.clear()

# add namespaces for api v1
API_V1.add_namespace(NS_BOOK)
