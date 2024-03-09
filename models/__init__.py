#!/usr/bin/python3
"""init declarations"""

from .base_model import BaseModel
from .user import User
from .engine.file_storage import FileStorage

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
