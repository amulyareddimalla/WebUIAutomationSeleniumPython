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
        windows_link = driver.find_element(By.XPATH, "//h5[normalize-space()='Alerts, Frame & Windows']")
        # To hover the cursor over the Alerts, Frame & Windows link and click
        actions = ActionChains(driver)
        actions.move_to_element(windows_link).click().perform()
        windows_heading = driver.find_element(By.XPATH, "//div[@class='main-header']").text
        print(windows_heading)
        assert "Alerts" in windows_heading
        driver.execute_script("window.scrollBy(0,300)")
        driver.find_element(By.XPATH,"//div[normalize-space()='Alerts, Frame & Windows']").click()
        driver.find_element(By.XPATH,"//span[normalize-space()='Alerts']").click()
        driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
        alert=driver.switch_to.alert
        print(alert.text)
        alert.accept()
        driver.find_element(By.XPATH,"//button[@id='timerAlertButton']").click()
        time.sleep(5)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        print(driver.find_element(By.XPATH,"//span[@id='confirmResult']").text)
        driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
        alert = driver.switch_to.alert
        alert.send_keys('Automation Tester')
        alert.accept()
        print(driver.find_element(By.XPATH,"//span[@id = 'promptResult']").text)


