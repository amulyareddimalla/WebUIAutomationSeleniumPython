import configparser

class ReadConfig:
    def __init__(self):
        self.config=configparser.RawConfigParser()
        self.config.read("C:\\Users\\amuly\\PycharmProjects1\\WebUIAutomation\\Configurations\\config.ini")

    def getApplicationURL(self):
        ui_url=self.config.get('common info', 'baseURL')
        return ui_url

    def getinputPath(self):
        input_path=self.config.get('common info', 'path')
        return input_path