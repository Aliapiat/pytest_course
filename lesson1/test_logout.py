import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def driver():
    # Open browser
    driv = webdriver.Chrome()  # Или любой другой браузер
    yield driv   # передаём в функцию, которой вызываем фикстуру
    # Close the browser
    driv.quit()


def test_logout(driver):
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(0.5)
    logout_button = driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link")
    logout_button.click()
    time.sleep(0.5)
    assert driver.current_url == "https://www.saucedemo.com/"