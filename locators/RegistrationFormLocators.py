from selenium.webdriver.common.by import By


class RegistrationForm:
    first_name = (By.ID, 'firstname')
    last_name = (By.ID, 'lastname')
    team = (By.ID, 'team')
    password = (By.ID, 'password')
    confirm_password = (By.ID, 'password_confirmation')
    terms_checkbox = (By.ID, 'acceptTerms')
    birthday = (By.ID, 'birthday')
    gender = (By.ID, 'gender')
    male = (By.ID, 'male')
    female = (By.ID, 'female')
    email = (By.ID, 'email')
    gender_checkbox_1 = (By.XPATH, '//*[contains(text(), "Male")]')
    user_mobile_number = (By.ID, 'userNumber')
    data_of_birth = (By.ID, 'dateOfBirthInput')
    hobbies_checkbox_1 = (By.XPATH, '//*[contains(text(), "Sports")]')
    picture = (By.ID, 'uploadPicture')
    current_address = (By.ID, 'currentAddress')
    state = (By.ID, 'state')
    select_state = (By.ID, 'state')
    NCR = (By.XPATH, '//*[contains(text(), "NCR")]')
    city = (By.ID, 'city')
    DELHI = (By.XPATH, '//*[contains(text(), "Delhi")]')
    btn_submit = (By.ID, 'submit')
    nav_profile = (By.XPATH, '//*[@id="overview"]/span')
    nav_header_profile_image = (By.CSS_SELECTOR, '.profile-user-img-header.rounded-circle')
    modal_submitting_form = (By.CSS_SELECTOR, '.modal-body')
    modal_name = (By.XPATH, '(//*[contains(text(), "Student Name")]/../td)[2]')
    modal_email = (By.XPATH, '(//*[contains(text(), "Student Email")]/../td)[2]')
    modal_gender_male = (By.XPATH, '(//*[contains(text(), "Gender")]/../td)[2]')
    modal_mobile_number = (By.XPATH, '(//*[contains(text(), "Mobile")]/../td)[2]')
    modal_date_of_birth = (By.XPATH, '(//*[contains(text(), "Date Of Birth")]/../td)[2]')
    modal_hobbies = (By.XPATH, '(//*[contains(text(), "Hobbies")]/../td)[2]')
    modal_picture = (By.XPATH, '(//*[contains(text(), "Picture")]/../td)[2]')
    modal_current_address = (By.XPATH, '(//*[contains(text(), "Address")]/../td)[2]')
    modal_state_and_city = (By.XPATH, '(//*[contains(text(), "State and City")]/../td)[2]')