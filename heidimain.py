import logging
from typing import List, Dict, Any


Configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

#Enhanced Custom Experience
class UserManagementError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code

class UsrNotFoundError(UserManagementError):
    def __init__(self, user_id: Any):
        self.user_id