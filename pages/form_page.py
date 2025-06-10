from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def open(self):
        self.driver.get(self.url)

    def fill_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def select_gender(self, gender):
        self.driver.find_element(By.XPATH, f"//label[text()='{gender}']").click()

    def fill_mobile_number(self, number):
        self.driver.find_element(By.ID, "userNumber").send_keys(number)

    def set_date_of_birth(self, date_str):
        date_input = self.driver.find_element(By.ID, "dateOfBirthInput")
        date_input.click()
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(date_str)
        date_input.send_keys(Keys.ENTER)

    def fill_subjects(self, subjects):
        input_subject = self.driver.find_element(By.ID, "subjectsInput")
        for subject in subjects:
            input_subject.send_keys(subject)
            input_subject.send_keys(Keys.ENTER)

    def select_hobby(self, hobby):
        self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']").click()

    def upload_picture(self, path):
        self.driver.find_element(By.ID, "uploadPicture").send_keys(path)

    def fill_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)

    def select_state(self, state):
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(state)
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

    def select_city(self, city):
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(city)
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()