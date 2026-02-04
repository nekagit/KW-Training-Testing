import logging
from typing import List, Dict, Any

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# --- Enhanced Custom Exceptions ---

class UserManagementError(Exception):
    """Base exception. Includes a status code for API compatibility."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code

class UserNotFoundError(UserManagementError):
    """Raised when a user lookup fails."""
    def __init__(self, user_id: Any):
        self.user_id = user_id
        self.message = f"User with ID {user_id} was not found in the system."
        super().__init__(self.message, status_code=404)

class ValidationError(UserManagementError):
    """Raised when input data fails validation rules."""
    def __init__(self, reason: str):
        self.message = f"Validation Failed: {reason}"
        super().__init__(self.message, status_code=400)

# --- Core Service ---

class UserService:
    def __init__(self):
        # Initial state
        self._db: List[Dict[str, Any]] = [
            {'id': 0, 'name': 'kathrin'}, 
            {'id': 1, 'name': 'nenad'}
        ]
        # Set next_id based on current max ID in the list
        self._next_id = max([u['id'] for u in self._db], default=-1) + 1

    def add_user(self, name: str) -> Dict[str, Any]:
        """Adds a user after validating the name."""
        if not isinstance(name, str) or len(name.strip()) < 2:
            raise ValidationError("Name must be a string with at least 2 characters.")

        new_user = {'id': self._next_id, 'name': name.strip()}
        self._db.append(new_user)
        self._next_id += 1
        
        logger.info(f"Created: {new_user}")
        return new_user

    def update_user(self, user_id: int, new_name: str) -> Dict[str, Any]:
        """Updates an existing user's details."""
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValidationError("Updated name cannot be empty.")

        for user in self._db:
            if user['id'] == user_id:
                user['name'] = new_name.strip()
                logger.info(f"Updated ID {user_id} to {new_name}")
                return user
        
        raise UserNotFoundError(user_id)

    def delete_user(self, user_id: int) -> bool:
        """Removes a user. Raises UserNotFoundError if ID is missing."""
        for index, user in enumerate(self._db):
            if user['id'] == user_id:
                self._db.pop(index)
                logger.info(f"Deleted ID {user_id}")
                return True
        
        raise UserNotFoundError(user_id)

    def list_db(self) -> List[Dict[str, Any]]:
        """Returns the current database state."""
        return self._db

