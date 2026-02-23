import pytest
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utilities.data_reader import load_json
from config import Config

# 1. Load the unified JSON file
all_data = load_json("users.json")

# 2. Extract the list of users for data-driven testing
# This matches the "data_driven_users" key we added to your JSON
user_list = all_data["data_driven_users"]


@pytest.mark.parametrize("user", user_list)
def test_full_registration_and_login(page, user):
    register = RegisterPage(page)
    register.navigate()
    register.fill_initial_signup(user['name'], user['email'])
    register.fill_account_details(user) # This passes the whole dictionary
    assert register.account_created_msg.is_visible()