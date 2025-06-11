from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        gender_label = self.driver.find_element(By.XPATH, f"//label[text()='{gender}']")
        self.driver.execute_script("arguments[0].click();", gender_label)

    def fill_mobile_number(self, number):
        self.driver.find_element(By.ID, "userNumber").send_keys(number)

    def set_date_of_birth(self, date_str):
        date_input = self.driver.find_element(By.ID, "dateOfBirthInput")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        self.driver.execute_script("arguments[0].click();", date_input)
        date_input.clear()
        date_input.send_keys(date_str)
        date_input.send_keys(Keys.ENTER)

    def fill_subjects(self, subjects):
        input_subject = self.driver.find_element(By.ID, "subjectsInput")
        for subject in subjects:
            input_subject.send_keys(subject)
            input_subject.send_keys(Keys.ENTER)

    def select_hobby(self, hobby):
        hobby_checkbox = self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
        self.driver.execute_script("arguments[0].click();", hobby_checkbox)

    def upload_picture(self, path):
        absolute_path = os.path.abspath(path)
        self.driver.find_element(By.ID, "uploadPicture").send_keys(absolute_path)

    def fill_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)

    def select_state(self, state):
        state_input = self.driver.find_element(By.ID, "react-select-3-input")
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, city):
        city_input = self.driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

    def submit_form(self):
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def wait_for_modal(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            return modal
        except TimeoutException:
            return None

    def is_modal_displayed(self, timeout=5):
        return self.wait_for_modal(timeout) is not None

    def close_modal(self):
        close_btn = self.driver.find_element(By.ID, "closeLargeModal")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", close_btn)
        self.driver.execute_script("arguments[0].click();", close_btn)
