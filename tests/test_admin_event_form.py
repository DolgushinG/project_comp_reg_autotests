import time

import pytest
from selenium.webdriver.common.by import By

from conftest import PROJECT_ROOT
from constants import URL
from helpers.repeat_fill_field import repeat_fill_fields
from pages.AdminEventPage import AdminEventPage
from pages.EventPage import EventPage


@pytest.mark.usefixtures("driver")
class TestAdminEventForm:

    @pytest.mark.admin
    def test_event_classic(self, login_to_admin, delete_event):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()

    @pytest.mark.admin
    def test_event_classic_with_autocategories(self, login_to_admin):
        repeat_fill_fields(self.driver)
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_down()
        admin_event_form.click_to_btn_autocategories()
        admin_event_form.scroll_down()
        admin_event_form.click_add_autocategories()
        admin_event_form.select_category(category="1")
        admin_event_form.select_grade(grade="1")
        admin_event_form.click_add_autocategories()
        admin_event_form.select_category(category="2")
        admin_event_form.select_grade(grade="2")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        time.sleep(2)
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_pay()
        admin_event_form.verify_record_pay('12')
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_final()
        admin_event_form.verify_final()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_navigate_to_sidebar(self, login_to_admin):
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form.go_to_main()
        admin_event_form.verify_main()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.go_to_final()
        admin_event_form.verify_final()
        admin_event_form.go_to_pay()
        admin_event_form.verify_pay()

    @pytest.mark.admin
    def test_edit_and_delete_routes(self, login_to_admin):
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        # admin_event_form.click_to('Редактировать', 'a')
        # admin_event_form.scroll_down()
        # admin_event_form.click_to('Отправить', 'button')
        # admin_event_form.verify_title_success_create()
        admin_event_form.click_to('Удалить', 'a')
        admin_event_form.click_to('Подтвердить', 'button')
        admin_event_form.click_to('OK', 'button')
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        admin_event_form.verify_title_success_create()

    @pytest.mark.admin
    def test_event_classic_full(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        # admin_event_form.fill_field(field='amount_the_best_participant', value="15")
        # admin_event_form.fill_field(field='amount_point_flash', value="1.2")
        # admin_event_form.fill_field(field='amount_point_redpoint', value="1")
        # admin_event_form.click_to_all_route_radio_btn()
        admin_event_form.is_semifinal()
        # # admin_event_form.click_to('Классика финал для лучших в квалификации')
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_pay()
        admin_event_form.verify_record_pay('12')
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_final()
        admin_event_form.verify_final()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_event_france_system_full(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_france_system_radio_btn()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to(' Настроить кол-во трасс', 'a')
        admin_event_form.fill_field_dinamic('count_routes', '10')
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 5)
        time.sleep(10)
        admin_event_form.go_to_final()
        admin_event_form.verify_final()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_event_classic_full_with_all_route_mode(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.click_to_btn_all_route_radio_btn()
        admin_event_form.is_semifinal()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '3')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        admin_event_form.verify_result_qualification()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_final()
        admin_event_form.verify_final()
        admin_event_form.click_to(' Сгенерировать результаты[beta]', 'a')
        admin_event_form.click_to_generate_result_final()
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_edit_participant_result(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        # admin_event_form.fill_field(field='amount_the_best_participant', value="15")
        # admin_event_form.fill_field(field='amount_point_flash', value="1.2")
        # admin_event_form.fill_field(field='amount_point_redpoint', value="1")
        # admin_event_form.click_to_all_route_radio_btn()
        admin_event_form.is_semifinal()
        # # admin_event_form.click_to('Классика финал для лучших в квалификации')
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_to('Редактировать', 'a', 1)
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_add_result_one_route_beginner_in_semifinal(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.is_semifinal()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_to('Новичок по одной трассе', 'a', 1)
        admin_event_form.select_participant('Новичок')
        admin_event_form.select_number_route('Новичок')
        admin_event_form.fill_field_dinamic('amount_try_top', '2')
        admin_event_form.fill_field_dinamic('amount_try_zone', '2')
        admin_event_form.click_to('Отправить', 'button', 2)
        time.sleep(2)
        admin_event_form.click_to('Закрыть', 'button', 2)
        admin_event_form.page_reload()
        time.sleep(2)
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_add_result_one_route_in_semifinal(self, login_to_admin):
        admin_event_form = repeat_fill_fields(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.is_semifinal()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        time.sleep(4)
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_btn_add_one_route()
        admin_event_form.select_participant('Общий зачет по одному')
        admin_event_form.select_number_route('Общий зачет по одному')
        admin_event_form.fill_field_amount_try_top('2')
        admin_event_form.fill_field_amount_try_zone('2')
        admin_event_form.click_to('Отправить', 'button', 4)
        time.sleep(2)
        admin_event_form.click_to('Закрыть', 'button', 4)
        admin_event_form.page_reload()
        time.sleep(2)
        admin_event_form.verify_result_final()
        time.sleep(2)
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_add_result_all_in_semifinal(self, login_to_admin):
        repeat_fill_fields(self.driver)
        admin_event_form = AdminEventPage(self.driver);
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.is_semifinal()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        time.sleep(4)
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_btn_add_all_route()
        admin_event_form.select_participant('Общий зачет')
        admin_event_form.fill_field_amount_try_top_1('2')
        admin_event_form.fill_field_amount_try_zone_1('2')
        admin_event_form.fill_field_amount_try_top_2('2')
        admin_event_form.fill_field_amount_try_zone_2('2')
        admin_event_form.fill_field_amount_try_top_3('2')
        admin_event_form.fill_field_amount_try_zone_3('2')
        admin_event_form.fill_field_amount_try_top_4('2')
        admin_event_form.fill_field_amount_try_zone_4('2')
        admin_event_form.fill_field_amount_try_top_5('2')
        admin_event_form.fill_field_amount_try_zone_5('2')
        admin_event_form.click_to('Отправить', 'button', 5)
        admin_event_form.verify_result_final()
        admin_event_form.go_to_events()
        time.sleep(2)
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_edit_result_all_in_semifinal(self, login_to_admin):
        repeat_fill_fields(self.driver)
        admin_event_form = AdminEventPage(self.driver);
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.is_semifinal()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.go_to_setting_routes()
        admin_event_form.verify_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        time.sleep(5)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        time.sleep(4)
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        admin_event_form.click_switch_payment()
        admin_event_form.go_to_semifinal()
        admin_event_form.verify_semifinal()
        admin_event_form.click_btn_add_all_route()
        admin_event_form.select_participant('Общий зачет')
        admin_event_form.fill_field_amount_try_top_1('2')
        admin_event_form.fill_field_amount_try_zone_1('2')
        admin_event_form.fill_field_amount_try_top_2('2')
        admin_event_form.fill_field_amount_try_zone_2('2')
        admin_event_form.fill_field_amount_try_top_3('2')
        admin_event_form.fill_field_amount_try_zone_3('2')
        admin_event_form.fill_field_amount_try_top_4('2')
        admin_event_form.fill_field_amount_try_zone_4('2')
        admin_event_form.fill_field_amount_try_top_5('2')
        admin_event_form.fill_field_amount_try_zone_5('2')
        admin_event_form.click_to('Отправить', 'button', 5)
        admin_event_form.verify_result_final()
        admin_event_form.click_to('Редактировать', 'a', 1)
        admin_event_form.click_to('Отправить', 'button', 1)
        admin_event_form.verify_title_success_create()
        admin_event_form.go_to_events()
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()

    @pytest.mark.admin
    def test_event_classic_with_autocategories_checking_list_participant(self, login_to_admin):
        repeat_fill_fields(self.driver)
        event_form = EventPage(self.driver)
        admin_event_form = AdminEventPage(self.driver)
        admin_event_form.click_btn_tab_options()
        admin_event_form.click_to_btn_classic_radio_btn()
        admin_event_form.click_to_btn_add_categories()
        admin_event_form.fill_field_category(number=1, value="Новичок")
        admin_event_form.fill_field_category(number=2, value="Общий зачет")
        admin_event_form.scroll_down()
        admin_event_form.click_to_btn_autocategories()
        admin_event_form.scroll_down()
        admin_event_form.click_add_autocategories()
        admin_event_form.select_category(category="1")
        admin_event_form.select_grade(grade="1")
        admin_event_form.click_add_autocategories()
        admin_event_form.select_category(category="2")
        admin_event_form.select_grade(grade="2")
        admin_event_form.scroll_up()
        admin_event_form.click_btn_tab_control()
        admin_event_form.click_btn_submit()
        admin_event_form.verify_title_success_create()
        admin_event_form.diactivate_old_event()
        admin_event_form.activate_new_event()
        admin_event_form.click_to('Редактировать','a', 1)
        admin_event_form.click_btn_tab_control()
        admin_event_form.scroll_down()
        time.sleep(1)
        admin_event_form.click_is_public('off')
        time.sleep(1)
        admin_event_form.click_btn_submit()
        admin_event_form.go_to_setting_routes()
        admin_event_form.click_to('Сгенерировать трассы', 'a')
        admin_event_form.scroll_down()
        admin_event_form.click_to('Отправить', 'button')
        admin_event_form.verify_title_success_create()
        admin_event_form.verify_setting_routes()
        admin_event_form.go_to_url(f'{URL}/admin/events')
        admin_event_form.verify_events()
        admin_event_form.click_to('Редактировать', 'a', 2)
        admin_event_form.click_btn_tab_control()
        admin_event_form.scroll_down()
        time.sleep(1)
        admin_event_form.click_is_public('on')
        time.sleep(1)
        admin_event_form.click_btn_submit()
        admin_event_form.go_to_qualification()
        admin_event_form.verify_qualification()
        admin_event_form.click_to(' Сгенерировать участников [beta](Ожидание до ~ 2 мин)', 'a')
        admin_event_form.fill_field_dinamic('count', '10')
        admin_event_form.click_to('Отправить', 'button', 3, 'text()')
        time.sleep(10)
        event_form.go_to_url(f'{URL}/')
        event_form.click_event_with_js()
        event_form.click_list_participant()
        time.sleep(2)
        event_form.verify_list_participant()
        admin_event_form.go_to_url(f'{URL}/admin/events')
        admin_event_form.verify_events()
        admin_event_form.diactivate_new_event()
        admin_event_form.activate_old_event()
        admin_event_form.delete_event()
        time.sleep(2)
        admin_event_form.click_to('Редактировать', 'a', 1)
        admin_event_form.click_btn_tab_control()
        admin_event_form.scroll_down()
        admin_event_form.click_is_public('on')
        admin_event_form.click_btn_submit()