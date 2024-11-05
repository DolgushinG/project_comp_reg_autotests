from selenium.webdriver.common.by import By


class AdminEventPageLocators:
    btn_try = (By.CSS_SELECTOR, '[class="btn btn-warning"]')
    btn_zone = (By.XPATH, "//span[contains(text(), 'Зона')]")
    btn_top = (By.XPATH, "//span[contains(text(), 'Топ')]")
    btn_send_generate_participant = (By.CSS_SELECTOR, 'div[id="app-admin-actions-batchgenerateparticipant"] button[type="submit"]')
    btn_send_result_off = (By.XPATH, "//input[contains(@class,'is_send_result_state') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-on bootstrap-switch-success')]")
    btn_send_result_on = (By.XPATH, "//input[contains(@class,'is_send_result_state') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-off bootstrap-switch-default')]")
    open_table_analytics = (By.XPATH, '//a[contains(text(), "competition")]')
    analytics_table = (By.CSS_SELECTOR, '[class="dataTables_wrapper form-inline dt-bootstrap no-footer"]')
    btn_analytics = (By.XPATH, '//span[contains(text(), "Аналитика")]')
    checkbox_is_public_analytics_on = (By.XPATH, "//input[contains(@class,'is_open_public_analytics') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-off bootstrap-switch-default')]")
    checkbox_is_full_results_on = (By.XPATH, "//input[contains(@class,'is_open_send_result_state') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-off bootstrap-switch-default')]")
    btn_add_autocategories = (By.XPATH, '//div[contains(@id, \'has-many-options_categories\')]//div[contains(text(), "Добавить")]')
    field_climbing_gym = (By.XPATH, '(//input[@id="climbing_gym_name"])[2]')
    checkbox_is_public_on = (By.XPATH, "//input[contains(@class,'is_public') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-off bootstrap-switch-default')]")
    checkbox_is_public_off = (By.XPATH, "//input[contains(@class,'is_public') and @type='checkbox']/../span[contains(@class, 'bootstrap-switch-handle-on bootstrap-switch-success')]")
    select_grade_from_1 = (By.CSS_SELECTOR, 'select[name="options_categories[new_1][От какой категории сложности определять эту категорию]"]')
    select_grade_from_2 = (By.CSS_SELECTOR, 'select[name="options_categories[new_2][От какой категории сложности определять эту категорию]"]')
    select_grade_to_1 = (By.CSS_SELECTOR, 'select[name="options_categories[new_1][До какой категории сложности определять эту категорию]"]')
    select_grade_to_2 = (By.CSS_SELECTOR, 'select[name="options_categories[new_2][До какой категории сложности определять эту категорию]"]')
    select_category_1 = (By.CSS_SELECTOR, 'select[name="options_categories[new_1][Категория участника]"]')
    select_category_2 = (By.CSS_SELECTOR, 'select[name="options_categories[new_2][Категория участника]"]')
    checkbox_autocategories = (By.XPATH, '//*[@class="is_auto_categories1"]')
    field_amount_try_zone_5 = (By.XPATH, '(//*[@id="amount_try_zone_5"])[2]')
    field_amount_try_top_5 = (By.XPATH, '(//*[@id="amount_try_top_5"])[2]')
    field_amount_try_zone_4 = (By.XPATH, '(//*[@id="amount_try_zone_4"])[2]')
    field_amount_try_top_4 = (By.XPATH, '(//*[@id="amount_try_top_4"])[2]')
    field_amount_try_zone_3 = (By.XPATH, '(//*[@id="amount_try_zone_3"])[2]')
    field_amount_try_top_3 = (By.XPATH, '(//*[@id="amount_try_top_3"])[2]')
    field_amount_try_zone_2 = (By.XPATH, '(//*[@id="amount_try_zone_2"])[2]')
    field_amount_try_top_2 = (By.XPATH, '(//*[@id="amount_try_top_2"])[2]')
    field_amount_try_zone_1 = (By.XPATH, '(//*[@id="amount_try_zone_1"])[2]')
    field_amount_try_top_1 = (By.XPATH, '(//*[@id="amount_try_top_1"])[2]')
    btn_add_all_route = (By.XPATH, '(//a[contains(text(), "Общий зачет")])[2]')
    record_pay = (By.CSS_SELECTOR, "td.column-amount_for_pay")
    switch_payment_1 = (By.XPATH, "(//span[contains(@class,'bootstrap-switch-handle-off bootstrap-switch-default')])[1]")
    result_qualification = (By.XPATH, "(//td[contains(@class, 'column-user-middlename')])[1]")
    btn_generate_result_final = (By.XPATH, '//button[contains(., "Отправить") and @class="swal2-confirm swal2-styled"]')
    result_final = (By.CSS_SELECTOR, 'tbody > tr')
    event_festival_2024 = (
    By.XPATH, '//td[contains(.,"Фестиваль 2024")]/..//a[@class="btn event_delete btn-error"]')
    event_festival_2024_yes = (By.XPATH,
                               '//td[contains(.,"Фестиваль 2024")]/..//span[@class="bootstrap-switch-handle-on bootstrap-switch-success"]')
    event_festival_2024_no = (By.XPATH,
                              '//td[contains(.,"Фестиваль 2024")]/..//span[@class="bootstrap-switch-handle-off bootstrap-switch-default"]')
    event_competition_yes = (
    By.XPATH, '//td[contains(.,"competition")]/..//span[@class="bootstrap-switch-handle-on bootstrap-switch-success"]')
    event_competition_no = (
    By.XPATH, '//td[contains(.,"competition")]/..//span[@class="bootstrap-switch-handle-off bootstrap-switch-default"]')
    nav_pay = (By.XPATH, '//span[contains(text(), "Оплата за сервис")]')
    is_semifinal = (By.XPATH, '(//div[@id="is_semifinal"])[1]')
    is_not_semifinal = (By.XPATH, '(//div[@id="is_semifinal"])[2]')
    title_final = (By.XPATH, '//a[contains(text(), "Карточки для финалистов")]')
    btn_all_add_result_one_route = (By.XPATH, '//a[contains(text(), "Общий зачет по одной трассе")]')
    field_amount_try_top = (By.XPATH, '(//*[@id="amount_try_top"])[2]')
    field_amount_try_zone = (By.XPATH, '(//*[@id="amount_try_zone"])[2]')
    nav_final = (By.XPATH, '//*[contains(text(), "Финал")]')
    title_setting_routes = (By.XPATH, '//th[contains(text(), "Настройка трасс для соревнования")]')
    nav_setting_routes = (By.XPATH, '//*[contains(text(), "Настройка трасс")]')
    title_semifinal = (By.XPATH, '//a[contains(text(), "Карточки для полуфиналистов")]')
    nav_semifinal = (By.XPATH, '//*[contains(text(), "Полуфинал")]')
    title_qualification = (By.XPATH, '//a[contains(text(), " Сгенерировать участников [beta](Ожидание до ~ 2 мин)")]')
    nav_qualification = (By.XPATH, '//*[contains(text(), "Квалификация")]')
    title_events = (By.XPATH, '//*[contains(text(), " Уведомить по почте всех юзеров")]')
    nav_events = (By.XPATH, '//*[contains(text(), "Соревнования")]')
    title_pay = (By.XPATH, '//*[contains(text(), "Соревнование")]')
    title_main = (By.XPATH, '//*[contains(text(), "Кол-во участников")]')
    nav_main = (By.XPATH, '//*[contains(text(), "Главная")]')
    user_name = (By.CSS_SELECTOR, 'input[name="username"]')
    password = (By.CSS_SELECTOR, 'input[name="password"]')
    btn_submit = (By.CSS_SELECTOR, '[type="submit"]')
    btn_enter = (By.CSS_SELECTOR, 'button[type="submit"]')
    btn_tab_control = (By.XPATH, '//button[contains(text(), "Управление")]')
    btn_tab_participant = (By.XPATH, '//button[contains(text(), "Участники")]')
    btn_tab_format = (By.XPATH, '//button[contains(text(), "Настройка формата")]')
    btn_tab_pay = (By.XPATH, '//button[contains(text(), "Настройка оплаты")]')
    btn_tab_doc = (By.XPATH, '//button[contains(text(), "Положение")]')
    btn_tab_afisha = (By.XPATH, '//button[contains(text(), "Афиша")]')
    title_admin = (By.XPATH, '//h1[contains(text(), "Главная")]')
    title_success_create = (By.XPATH, '//*[contains(text(), "Сохранено")]')
    image = (By.XPATH, '(//input[@type="file"])[1]')
    description_text_area = (By.XPATH, '//*[contains(@class, \'note-editable\')]')
    classic_radio_btn = (By.XPATH, '//*[contains(@class, "is_france_system_qualification0")]')
    france_system_radio_btn = (By.XPATH, '//*[contains(@class, "is_france_system_qualification1")]')
    all_route_radio_btn = (By.XPATH, '//div[contains(@class, \'mode2\')]')
    btn_add_category = (By.CSS_SELECTOR, '[data-field-block="categories[]"] a.btn.w-full')
    field_category_1 = (By.XPATH, "(//input[contains(@name, 'categories[values][]')])[1]")
    field_category_2 = (By.XPATH, "(//input[contains(@name, 'categories[values][]')])[2]")
