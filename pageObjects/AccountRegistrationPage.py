from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    txt_firstname_id="FirstName"
    txt_lastname_id="LastName"
    txt_email_name="Email"
    txt_password_id="Password"
    txt_confirmpwd_id="ConfirmPassword"
    btn_register_id="register-button"
    text_msg_conf_xpath="//div[@class='result']"

    def __init__(self,driver):
        self.driver=driver


    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)

    def setConfirmPassword(self,confirmPwd):
        self.driver.find_element(By.ID,self.txt_confirmpwd_id).send_keys(confirmPwd)

    def submit_register(self):
        self.driver.find_element(By.ID,self.btn_register_id).click()

    def chk_confirm_msg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None


