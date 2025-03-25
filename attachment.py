# -*- coding: utf-8 -*-
"""
    attachment

    Send attachments to S3

"""

try:
    import hashlib
except ImportError:
    hashlib = None
    import md5

from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.exception import S3ResponseError

from trytond.config import config
from trytond.transaction import Transaction
from trytond.pool import PoolMeta

__all__ = ['Attachment']


class Attachment(metaclass=PoolMeta):
    "Attachment"
    __name__ = 'ir.attachment'
    # no longer needed because of tryton-filestore-s3