import pytest
from pages.form_page import FormPage
from utils.helpers import take_screenshot


@pytest.mark.parametrize("email", ["invalid@", "user@.com", "email"])
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
    take_screenshot(driver, f"invalid_email_{email.replace('@', '_at_').replace('.', '_dot_')}")

    assert not form.is_modal_displayed(), f"O modal foi exibido mesmo com email inválido: {email}"


@pytest.mark.xfail(reason="O formulário é enviado mesmo com campo de e-mail vazio")
def test_empty_email_submission(driver):
    form = FormPage(driver)
    form.open()
    form.fill_first_name("Celia")
    form.fill_last_name("Bruno")
    form.fill_email("")
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
    take_screenshot(driver, "invalid_email_empty")

    assert not form.is_modal_displayed(), "O modal foi exibido com e-mail vazio"


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
    take_screenshot(driver, "missing_first_name")

    assert not form.is_modal_displayed(), "O modal foi exibido mesmo sem preencher o primeiro nome"


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
    take_screenshot(driver, "invalid_mobile_number")

    assert not form.is_modal_displayed(), "O modal foi exibido mesmo com número de celular inválido"