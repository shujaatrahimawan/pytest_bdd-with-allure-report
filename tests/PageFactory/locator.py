from selenium.webdriver.common.by import By

# --------------------------------------------- Adactin Hotel -------------------------------------------#

LoginSubmitButton = {'type': By.ID, 'locator': 'login'}

LoginEmailField = {'type': By.ID, 'locator': 'username'}

LoginPasswordField = {'type': By.ID, 'locator': 'password'}

ServerButtonAdd = {'type': By.XPATH, 'locator': '//button/b[text()="Add Server"]'}

LoginToast = {'type': By.CLASS_NAME, 'locator': 'welcome_menu'}

LocationDropDown = {'type': By.ID, 'locator': 'location'}

LocationDropDownOption = {'type': By.XPATH, 'locator': '//*[@id="location"]/option[@value="Sydney"]'}

HotelDropDown = {'type': By.ID, 'locator': 'hotels'}

HotelDropDownOption = {'type': By.XPATH, 'locator': '//*[@id="hotels"]/option[@value="Hotel Creek"]'}

RoomsDropDown = {'type': By.ID, 'locator': 'room_type'}

RoomsDropDownOption = {'type': By.XPATH, 'locator': '//*[@id="room_type"]/option[@value="Standard"]'}

RoomsNoDropDown = {'type': By.ID, 'locator': 'room_nos'}

RoomsNoDropDownOption = {'type': By.XPATH, 'locator': '//*[@id="room_nos"]/option[@value="2"]'}

SearchButton = {'type': By.ID, 'locator': 'Submit'}

RadioButtonFirstRecord = {'type': By.ID, 'locator': 'radiobutton_0'}

ContinueButton = {'type': By.ID, 'locator': 'continue'}

FirstName = {'type': By.ID, 'locator': 'first_name'}
LastName = {'type': By.ID, 'locator': 'last_name'}
Address = {'type': By.ID, 'locator': 'address'}
CC_Num = {'type': By.ID, 'locator': 'cc_num'}
CC_Type = {'type': By.ID, 'locator': 'cc_type'}
cc_exp_month = {'type': By.ID, 'locator': 'cc_exp_month'}
cc_exp_year = {'type': By.ID, 'locator': 'cc_exp_year'}
cc_cvv = {'type': By.ID, 'locator': 'cc_cvv'}
book_now = {'type': By.ID, 'locator': 'book_now'}
