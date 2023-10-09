from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_in_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)

    name1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link").text

    button = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()

    time.sleep(2)

    cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart.click()

    time.sleep(2)

    name2 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link").text

    assert name1 == name2

    driver.quit()

