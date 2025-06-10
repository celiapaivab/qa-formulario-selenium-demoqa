from pages.form_page import FormPage
from utils.helpers import take_screenshot


def test_fill_form_success(driver):
    try:
        form = FormPage(driver)
        form.open()
        form.fill_first_name("Celia")
        form.fill_last_name("Bruno")
        form.fill_email("celia@example.com")
        form.select_gender("Female")
        form.fill_mobile_number("11999999999")
        form.set_date_of_birth("16 Jan 1996")
        form.fill_subjects(["Maths", "English"])
        form.select_hobby("Reading")
        form.upload_picture("files/image.png")
        form.fill_address("Rua das Flores, 123")
        form.select_state("NCR")
        form.select_city("Delhi")
        form.submit_form()

        assert "Thanks for submitting the form" in driver.page_source

    except AssertionError:
        take_screenshot(driver, "test_fill_form_success_failure")
        raise

