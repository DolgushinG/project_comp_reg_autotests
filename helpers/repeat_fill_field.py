from selenium.webdriver.common.by import By
from constants import URL
from pages.AdminEventPage import AdminEventPage


def repeat_fill_fields(driver):
    admin_event_form = AdminEventPage(driver)
    admin_event_form.go_to_url(f'{URL}/moon/resource/event-resource/event-form-page')
    admin_event_form.fill_field_dinamic(field='title', value="Фестиваль 2024")
    admin_event_form.fill_field_dinamic(field='climbing_gym_name', value="skalodrom")
    admin_event_form.fill_field_dinamic(field='city', value="Москва")
    admin_event_form.fill_field_dinamic(field='address', value="Москва")
    admin_event_form.fill_field_dinamic(field='start_date', type=By.ID ,value="20-04-2024")
    admin_event_form.fill_field_dinamic(field='end_date', type=By.ID ,value="20-04-2027")
    return admin_event_form
