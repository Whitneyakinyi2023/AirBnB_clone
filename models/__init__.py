#!/usr/bin/python3
"""init declarations"""

from .base_model import BaseModel
from .user import User
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
