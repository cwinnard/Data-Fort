from flask_login import login_user

from psql.schema.master import User

class LoginFacilitator:
    """Uses flask functionality to set the current_user for use throughout app """ 
    
    def log_user_in(user):
        login_user(user)
