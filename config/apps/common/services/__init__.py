# common/services/__init__.py
from .account import *
from .create import create_instance
from .update import update_instance
from .delete import delete_instance
from .deactivate_user import deactivate_user

#this __all__ is optional
__all__ = [
   " create_instance",
    "update_instance",
    "delete_instance",
    "deactivate_user",
]