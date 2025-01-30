from selenium.webdriver.common.by import By
from constants import URL
from pages.AdminEventPage import AdminEventPage


def repeat_fill_fields(driver):
    admin_event_form = AdminEventPage(driver)
    admin_event_form.go_to_url(f'{URL}moon/resource/event-resource/form-page/37')
    admin_event_form.fill_field_dinamic(field='field-event-resource-6', value="Фестиваль 2024")
    admin_event_form.fill_field_dinamic(field='field-event-resource-7', value="skalodrom")
    admin_event_form.fill_field_dinamic(field='field-event-resource-8', value="Москва")
    admin_event_form.fill_field_dinamic(field='field-event-resource-10', value="Москва")
    admin_event_form.fill_field_dinamic(field='field-event-resource-11', value="20-04-2024")
    admin_event_form.fill_field_dinamic(field='field-event-resource-12', value="20-04-2026")
    return admin_event_form
