from src.models.user import User
from src.services.user_storage import load_user_data


user_data = load_user_data()

current_user = User(
    user_data["name"]
)

current_user.interests = user_data["interests"]
current_user.goals = user_data["goals"]
current_user.preferences = user_data["preferences"]