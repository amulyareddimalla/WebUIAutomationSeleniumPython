import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testthree:
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
        driver.find_element(By.XPATH,"//span[normalize-space()='Web Tables']").click()

        first_name_header = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'First Name')]"))
        )
        ActionChains(driver).click(first_name_header).perform()

        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rt-tbody"))
        )
        sorted_order = sorted(rows, key=lambda x: x.text)

        if rows == sorted_order:
            print("First column is sorted")
        else:
            print("First column is not sorted")
