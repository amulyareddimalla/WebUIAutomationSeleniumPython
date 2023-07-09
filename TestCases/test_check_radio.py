import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Testtwo:
    def test_check_radio(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(
            "C:/Users/amuly/PycharmProjects1/WebUIAutomation/Drivers/chromedriver.exe"))
        driver.maximize_window()
        driver.get("https://demoqa.com/")
        print(driver.title)
        # driver.execute_script("window.scrollTo(0, -100);")
        # Scroll down to the "Elements" link
        driver.execute_script("window.scrollBy(0,300)")
        elements_link = driver.find_element(By.XPATH, "//h5[normalize-space()='Elements']")
        # To hover the cursor over the elements link and click
        actions = ActionChains(driver)
        actions.move_to_element(elements_link).click().perform()
        elements_heading = driver.find_element(By.XPATH, "//div[@class ='main-header']").text
        print(elements_heading)
        assert "Elements" in elements_heading
        driver.find_element(By.XPATH, "//span[normalize-space()='Check Box']").click()
        driver.find_element(By.XPATH, "//span[@class='rct-checkbox']//*[name()='svg']").click()
        print(driver.find_element(By.XPATH, "//div[@id='result']").text)
        driver.find_element(By.XPATH, "//button[@title='Toggle']//*[name()='svg']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Radio Button']").click()
        radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
        print(len(radio_buttons))
        driver.find_element(By.XPATH, "//label[normalize-space()='Impressive']").click()
        print(driver.find_element(By.XPATH, "//p[@class='mt-3']").text)






