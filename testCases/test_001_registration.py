import os.path
import time

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg():
    baseUrl=ReadConfig.getBaseURL()
    logger=LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("*** test_001_accountReg is started***")
        self.driver=setup
        self.logger.info("*** test_001_accountReg browser launched***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp= HomePage(self.driver)
        self.logger.info("*** test_001_accountReg clicking on register ***")
        self.hp.clickOnRegister()
        self.rp=AccountRegistrationPage(self.driver)
        self.logger.info("*** test_001_accountReg entering form details ***")
        self.rp.setFirstName("John")
        self.rp.setLastName("Ramkumar")
        self.email=randomeString.random_string_generator()+'@test.com'
        self.rp.setEmail(self.email)
        self.rp.setPassword("test123")
        self.rp.setConfirmPassword("test123")
        self.logger.info("*** test_001_accountReg clicking on register submission ***")
        self.rp.submit_register()
        self.crmmsg= self.rp.chk_confirm_msg()

        if self.crmmsg == "Your registration completed":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screen"
                                                                   "shots\\"+"test_account_reg.png")
            self.logger.error("*** test_001_accountReg test case failed ***")

            self.driver.close()
            assert False

        self.logger.info("*** test_001_accountReg is completed ***")




