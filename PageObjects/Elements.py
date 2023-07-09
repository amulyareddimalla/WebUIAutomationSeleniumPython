from selenium.webdriver.common.by import By

class Elements:

    elements_link = (By.XPATH, "//h5[normalize-space()='Elements']")
    elements_heading=(By.XPATH,"//div[@class ='main-header']")
    elements_textbox=(By.XPATH, "//span[normalize-space()='Text Box']")
    textbox_fullname=(By.XPATH,"//input[@id='userName']")
    textbox_email=(By.XPATH, "//input[@id='userEmail']")
    textbox_current_address=(By.XPATH, "//textarea[@id='currentAddress']")
    textbox_permanent_address=(By.XPATH, "//textarea[@id='permanentAddress']")
    textbox_submit_button=(By.XPATH, "//button[@id = 'submit']")
    fullname_validation=(By.XPATH, "//p[@id='name']")
    email_validation=(By.XPATH, "//p[@id='email']")
    current_address_validation=(By.XPATH, "//p[@id='currentAddress']")
    permanent_address_validation=(By.XPATH, "//p[@id='permanentAddress']")


    '''when you create an object of this in actual test case like e2e then this
    constructor will be invoked to assign the main driver to this local driver'''
    def __init__(self, driver):
        self.driver = driver

    def click_elements_link(self):
        return self.driver.find_element(*Elements.elements_link) #if we add '*' it treats login as a tuple and treats it as line 5

    def verify_elements_heading(self):
        return self.driver.find_element(*Elements.elements_heading)

    def click_elements_textbox(self):
        return self.driver.find_element(*Elements.elements_textbox)

    def input_textbox_fullname(self):
        return self.driver.find_element(*Elements.textbox_fullname)

    def input_textbox_email(self):
        return self.driver.find_element(*Elements.textbox_email)

    def input_textbox_currentaddress(self):
        return self.driver.find_element(*Elements.textbox_current_address)

    def input_textbox_permanentaddress(self):
        return self.driver.find_element(*Elements.textbox_permanent_address)

    def click_submit_button(self):
        return self.driver.find_element(*Elements.textbox_submit_button)

    def verify_fullname(self):
        return self.driver.find_element(*Elements.fullname_validation)

    def verify_email(self):
        return self.driver.find_element(*Elements.email_validation)

    def verify_current_addresss(self):
        return self.driver.find_element(*Elements.current_address_validation)

    def verify_current_addresss(self):
        return self.driver.find_element(*Elements.current_address_validation)

    def verify_permanent_addresss(self):
        return self.driver.find_element(*Elements.permanent_address_validation)

