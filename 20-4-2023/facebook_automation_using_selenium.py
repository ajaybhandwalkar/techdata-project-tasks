from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class FacebookSignUpAutomation:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def login_service(self):
        try:
            email = self.driver.find_element(By.ID, "email")
            email.send_keys("abc@abc.com")
            password = self.driver.find_element(By.ID, "pass")
            password.send_keys("1234567890")
            login_button = self.driver.find_element(By.NAME, "login")
            login_button.click()
        except Exception as e:
            print("Exception occurred in login_service, msg : ", e)

    def create_account_service(self):
        try:
            # create_account_button = self.driver.find_element(By.ID, "u_0_0_LE")
            create_account_button = self.driver.find_element(By.LINK_TEXT, "Create new account")
            create_account_button.click()

            # sleep(2)  # required because it takes time to load page contents
            self.driver.implicitly_wait(2)
            # try:
            #     # wait 10 seconds before looking for element
            #     first_name = WebDriverWait(self.driver, 10).until(
            #         EC.presence_of_element_located((By.NAME, "firstname")))
            #     first_name.send_keys("Ajay")
            # except Exception as e:
            #     print("Exception occurred in create_account_service, ", e)


            first_name = self.driver.find_element(By.NAME, "firstname")

            self.driver.find_element(By.NAME, "lastname").send_keys("Bhandwalkar")
            self.driver.find_element(By.NAME, "reg_email__").send_keys("abc@abc.com")
            self.driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("abc@abc.com")
            self.driver.find_element(By.NAME, "reg_passwd__").send_keys("abc@1231232")
            self.driver.find_element(By.ID, "day").send_keys("11")
            self.driver.find_element(By.ID, "month").send_keys("Sep")
            self.driver.find_element(By.ID, "year").send_keys("1997")
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span"
                                     "/span[2]/input").click()
            sign_up_button = self.driver.find_element(By.NAME, "websubmit")
            sign_up_button.click()

        except Exception as e:
            print("Exception occurred in create_account_service, ", e)

    def main(self):
        try:
            self.driver.get("https://www.facebook.com")
            self.driver.maximize_window()
            # sleep(1)
            # self.driver.set_script_timeout(1)
            # self.login_service()
            self.create_account_service()
        except Exception as e:
            print("Exception occurred in main, msg : ", e)


if __name__ == '__main__':
    obj = FacebookSignUpAutomation()
    obj.main()
