from pages.form_page import FormPage
from utils.helpers import take_screenshot

def test_fill_form_success(driver):
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
    take_screenshot(driver, "formulario_preenchido")
    form.submit_form()

    assert form.is_modal_displayed(), "O modal de confirmação não apareceu após o envio do formulário."

    form.close_modal()
