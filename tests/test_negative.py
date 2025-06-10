import pytest
from pages.form_page import FormPage
from utils.helpers import take_screenshot

@pytest.mark.parametrize("email", ["", "invalid@", "user@.com"])
def test_invalid_email_submission(driver, email):
    form = FormPage(driver)
    form.open()
    form.fill_first_name("Celia")
    form.fill_last_name("Bruno")
    form.fill_email(email)
    form.select_gender("Female")
    form.fill_mobile_number("11999999999")
    form.set_date_of_birth("16 Jan 1996")
    form.fill_subjects(["Maths"])
    form.select_hobby("Reading")
    form.upload_picture("files/image.png")
    form.fill_address("Rua das Flores, 123")
    form.select_state("NCR")
    form.select_city("Delhi")
    form.submit_form()

    if "Thanks for submitting the form" in driver.page_source:
        take_screenshot(driver, f"unexpected_success_{email or 'empty'}")
        assert False, f"Form should not have been submitted with email: {email}"


def test_missing_first_name(driver):
    form = FormPage(driver)
    form.open()
    # Nome vazio
    form.fill_last_name("Bruno")
    form.fill_email("celia@example.com")
    form.select_gender("Female")
    form.fill_mobile_number("11999999999")
    form.set_date_of_birth("16 Jan 1996")
    form.fill_subjects(["English"])
    form.select_hobby("Reading")
    form.upload_picture("files/image.png")
    form.fill_address("Rua das Flores, 123")
    form.select_state("NCR")
    form.select_city("Delhi")
    form.submit_form()

    if "Thanks for submitting the form" in driver.page_source:
        take_screenshot(driver, "unexpected_success_missing_first_name")
        assert False, "Form should not be submitted without first name"

def test_invalid_mobile_number(driver):
    form = FormPage(driver)
    form.open()
    form.fill_first_name("Celia")
    form.fill_last_name("Bruno")
    form.fill_email("celia@example.com")
    form.select_gender("Female")
    form.fill_mobile_number("123")
    form.set_date_of_birth("16 Jan 1996")
    form.fill_subjects(["History"])
    form.select_hobby("Reading")
    form.upload_picture("files/image.png")
    form.fill_address("Rua das Flores, 123")
    form.select_state("NCR")
    form.select_city("Delhi")
    form.submit_form()

    if "Thanks for submitting the form" in driver.page_source:
        take_screenshot(driver, "unexpected_success_invalid_mobile")
        assert False, "Form should not be submitted with invalid mobile number"