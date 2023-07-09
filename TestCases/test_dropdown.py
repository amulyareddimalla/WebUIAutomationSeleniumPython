import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testseven:
    def test_table(self):
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
        widgets_link = driver.find_element(By.XPATH, "//h5[normalize-space()='Widgets']")
        # To hover the cursor over the elements link and click
        actions = ActionChains(driver)
        actions.move_to_element(widgets_link).click().perform()
        time.sleep(5)
        widgets_heading = driver.find_element(By.XPATH, "//div[@class ='main-header']").text
        print(widgets_heading)
        driver.execute_script("window.scrollBy(0,700)")
        # driver.find_element(By.XPATH, "//div[contains(@class ,'header-text')][normalize-space()='Widgets']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[normalize-space()='Select Menu']").click()
        time.sleep(5)
        static_dropdown=Select(driver.find_element(By.XPATH,"//select[@id='oldSelectMenu']"))
        static_dropdown.select_by_index(1)



