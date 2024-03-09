<<<<<<< HEAD
#!/usr/bin/python3
"""init declarations"""

from .base_model import BaseModel
from .user import User
from .engine.file_storage import FileStorage
=======
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
>>>>>>> cb77b257c13c07434eb9cc4b8b447a2fac7902e1

storage = FileStorage()
storage.reload()
