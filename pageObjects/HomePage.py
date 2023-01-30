from selenium.webdriver.common.by import By


class HomePage():
    link_register_xpath = "//a[normalize-space()=\'Register\']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnRegister(self):
        print("click on regis")
        self.driver.find_element(By.XPATH, self.link_register_xpath).click()
