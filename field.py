# -*- coding: utf-8 -*-
"""
    field

    Add S3Binary field which automatically sends the file to S3 instead of
    storing in filesystem

"""
import logging

from boto.s3.key import Key
from boto.exception import S3ResponseError
from boto.s3.connection import S3Connection
from trytond.model import fields
from trytond.config import config
from trytond.transaction import Transaction


class S3Binary(fields.Function):
    # no longer needed because of tryton-filestore-s3
    pass
