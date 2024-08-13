from selenium.webdriver.common.by import By

from conftest import PROJECT_ROOT
from constants import URL
from pages.AdminEventPage import AdminEventPage


def repeat_fill_fields(driver):
    admin_event_form = AdminEventPage(driver)
    admin_event_form.go_to_url(f'{URL}/admin/events/create')
    admin_event_form.fill_field_dinamic(field='title', value="Фестиваль 2024")
    admin_event_form.fill_field_climbing_gym("skalodrom")
    admin_event_form.fill_field_dinamic(field='city', value="Москва")
    admin_event_form.fill_field_dinamic(field='start_date', value="2024-04-19")
    admin_event_form.fill_field_dinamic(field='end_date', value="2024-04-19")
    # admin_event_form.upload_image(f"{PROJECT_ROOT}/image.jpg")
    admin_event_form.fill_field_description(value="long text")
    admin_event_form.fill_field_dinamic(field='contact', value="79992200222")
    admin_event_form.scroll_up()
    admin_event_form.click_btn_tab_pay()
    admin_event_form.fill_field_dinamic(field='link_payment', value="https://ya.ru")
    admin_event_form.fill_field_dinamic(field='amount_start_price', value="1200")
    admin_event_form.fill_field((By.XPATH,'(//div[contains(@class, "note-editable")])[2]'), "text")
    return admin_event_form
