import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.Elements import Elements
from Utils import XLUtils
from Utils.BaseClass import BaseClass
from Utils.readProperties import ReadConfig


class TestOne(BaseClass):
    log = BaseClass.getLogger()
    def test_datadriven(self):
        readconfig = ReadConfig()  # create object without any argument
        self.baseURL = readconfig.getApplicationURL()
        self.path= readconfig.getinputPath()
        self.driver.get(self.baseURL)
        self.log.info("Opened the URL")
        self.log.info(self.driver.title)
        elements_page=Elements(self.driver)
        # Scroll down to the "Elements" link
        self.driver.execute_script("window.scrollBy(0,300)")
        # elements_link = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Elements']")
        elements_link = elements_page.click_elements_link()
        #To hover the cursor over the elements link and click
        actions = ActionChains(self.driver)
        actions.move_to_element(elements_link).click().perform()
        self.log.info("Clicked on Elements")
        # elements_heading=self.driver.find_element(By.XPATH,"//div[@class ='main-header']").text
        elements_heading = elements_page.verify_elements_heading().text
        self.log.info(elements_heading)
        assert "Elements" in elements_heading

        # self.driver.find_element(By.XPATH, "//span[normalize-space()='Text Box']").click()
        elements_page.click_elements_textbox().click()
        self.log.info("Clicked on Text Box")
        workbook = openpyxl.load_workbook(
            "C:/Users/amuly/PycharmProjects1/WebUIAutomation/Input/Input_TestBox.xlsx")
        worksheet = workbook.active
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        for r in range(2, self.rows+1):
            self.Fullname_value = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Email_value = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.CurrentAddress_value = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.PermenantAdd_value = XLUtils.readData(self.path, 'Sheet1', r, 4)
            # Fullname_input=self.driver.find_element(By.XPATH,"//input[@id='userName']")
            Fullname_input = elements_page.input_textbox_fullname()
            Fullname_input.clear()
            Fullname_input.send_keys(self.Fullname_value)
            self.log.info("Given Full Name")
            # Email_input = self.driver.find_element(By.XPATH, "//input[@id='userEmail']")
            Email_input = elements_page.input_textbox_email()
            Email_input.clear()
            Email_input.send_keys(self.Email_value)
            self.log.info("Given Email")
            # CurrentAddr_input = self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
            CurrentAddr_input = elements_page.input_textbox_currentaddress()
            CurrentAddr_input.clear()
            CurrentAddr_input.send_keys(self.CurrentAddress_value)
            self.log.info("Given Current Address")
            # PermanantAdd_input = self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
            PermanantAdd_input = elements_page.input_textbox_permanentaddress()
            PermanantAdd_input.clear()
            PermanantAdd_input.send_keys(self.PermenantAdd_value)
            self.log.info("Given Permenant Address")
            self.driver.execute_script("window.scrollBy(0,300)")
            # self.driver.find_element(By.XPATH, "//button[@id = 'submit']").click()
            elements_page.click_submit_button().click()
            self.log.info("Clicked on Submit button")
            time.sleep(5)
            FullName=self.driver.find_element(By.XPATH, "//p[@id='name']").text
            Email=self.driver.find_element(By.XPATH, "//p[@id='email']").text
            Current_Address=self.driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
            Permanent_Address=self.driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
            self.log.info(FullName)
            self.log.info(Email)
            self.log.info(Current_Address)
            self.log.info(Permanent_Address)
            self.log.info("Form details displayed on UI as given in text boxes")
            split_name=FullName.split(':')
            name_split=split_name[1]
            if name_split == self.Fullname_value:
                assert True
                self.log.info("Pass")
            else:
                assert False
                self.log.info("Fail")















