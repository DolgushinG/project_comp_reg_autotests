import pytest

from conftest import PROJECT_ROOT
from constants import URL
from pages.AdminEventPage import AdminEventPage


@pytest.mark.usefixtures("driver")
class TestAdminEventForm:

    def test_event_classic(self):
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form._go_to_url(f'{URL}/admin')
        admin_event_form.fill_username('admin2')
        admin_event_form.fill_password('admin')
        admin_event_form.click_btn_enter()
        admin_event_form.verify_header_admin()
        admin_event_form._go_to_url(f'{URL}/admin/events/create')
        admin_event_form.fill_field(field='title', value="Фестиваль 2024")
        admin_event_form.fill_field(field='climbing_gym_name', value="skalodrom")
        admin_event_form.fill_field(field='city', value="Москва")
        admin_event_form.fill_field(field='address', value="ул. Ленина 1")
        admin_event_form.fill_field(field='start_date', value="2024-03-19")
        admin_event_form.fill_field(field='start_time', value="00:00:00")
        admin_event_form.fill_field(field='end_date', value="2024-03-19")
        admin_event_form.fill_field(field='end_time', value="00:00:00")
        admin_event_form.upload_image(f"{PROJECT_ROOT}/image.png")
        admin_event_form.fill_field_description(value="long text")
        admin_event_form.fill_field(field='contact', value="79992200222")
        admin_event_form.click_to('Оплата')
        admin_event_form.fill_field(field='link_payment', value="https://ya.ru")
        # admin_event_form.fill_field(field='qr_image', value="/path")
        admin_event_form.fill_field(field='amount_start_price', value="1200")
        # admin_event_form.fill_field(field='info_payment', value="long text")
        admin_event_form.click_to('Параметры соревнования')
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.fill_field(field='amount_the_best_participant', value="15")
        admin_event_form.fill_field(field='amount_point_flash', value="1.2")
        admin_event_form.fill_field(field='amount_point_redpoint', value="1")
        admin_event_form.click_to_all_route_radio_btn()
        # admin_event_form.click_to('С полуфиналом')
        # admin_event_form.click_to('Классика финал для лучших в квалификации')
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()