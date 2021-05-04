from selenium import webdriver
from tools.address_list import *
from tools.locators_list import *
from tools.creds_generator import CredsGenerator
import pytest


@pytest.mark.registration
@pytest.mark.ui
class TestRegistrationUI:
    # Checks if existing user can be registered.
    def test_registration(self):
        user_email, user_password, user_name = CredsGenerator.get_ui_creds(self)
        driver = webdriver.Chrome()
        driver.get(target_url)
        driver.find_element_by_xpath(enter_login_button).click()
        driver.find_element_by_xpath(email_reg_button).send_keys(user_email)
        driver.find_element_by_xpath(name_reg_button).send_keys(user_name)
        driver.find_element_by_xpath(password_reg_button).send_keys(user_password)
        driver.find_element_by_xpath(finish_reg_button).click()
        # On successfull registration we get logged in by default. UI-created users are not shown in the user list
        # for some reason, so I am going to check if *tasks* web element is present.
        assert driver.find_element_by_xpath(tasks_field).is_displayed(), \
                                                        "Registration failed! Wasn't redirected to the proper page."
        driver.quit()  # TODO use teardown fixture

    # Checks if new user can't be registered without a password.
    def test_bad_data_registration(self):
        user_email, user_password, user_name = CredsGenerator.get_ui_creds(self)
        driver = webdriver.Chrome()
        driver.get(target_url)
        driver.find_element_by_xpath(enter_login_button).click()
        driver.find_element_by_xpath(email_reg_button).send_keys(user_email)
        driver.find_element_by_xpath(name_reg_button).send_keys(user_name)
        driver.find_element_by_xpath(finish_reg_button).click()
        # Trying to register without a password yields a popup with relevant warning. For now it is easier
        # to assert that finish_reg_button is still present after clicking on it, meaning reg has failed.
        assert driver.find_element_by_xpath(finish_reg_button).is_displayed(), \
            "User was registered without a password!"
        driver.quit()  # TODO use teardown fixture