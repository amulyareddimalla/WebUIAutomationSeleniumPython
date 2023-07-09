import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testfour:
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
        elements_link = driver.find_element(By.XPATH, "//h5[normalize-space()='Elements']")
        # To hover the cursor over the elements link and click
        actions = ActionChains(driver)
        actions.move_to_element(elements_link).click().perform()
        elements_heading = driver.find_element(By.XPATH, "//div[@class ='main-header']").text
        print(elements_heading)
        assert "Elements" in elements_heading
        # driver.execute_script("window.scrollBy(0,300)")
        driver.find_element(By.XPATH,"//span[normalize-space()='Buttons']").click()
        time.sleep(5)
        doubleclick=driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")
        actions = ActionChains(driver)
        actions.double_click(doubleclick).perform()
        time.sleep(5)
        print(driver.find_element(By.XPATH,"//p[@id='doubleClickMessage']").text)
        RightClick=driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
        actions.move_to_element(RightClick).perform()
        actions.context_click(RightClick).perform()
        time.sleep(5)
        print(driver.find_element(By.XPATH, "//p[@id = 'rightClickMessage']").text)

