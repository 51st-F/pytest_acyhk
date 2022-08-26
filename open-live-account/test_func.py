import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

### fixture will move to conftest.py
@pytest.fixture(scope="module")
def chrome_driver_init(): # # use chrome for example
    chromedriver_autoinstaller.install() # can also test in other version of chrome to test
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    chrome_driver = driver
    url = 'https://acyhk.com/en/open-live-account'
    chrome_driver.get(url)
    yield chrome_driver
    driver.close()


def test_open_url(chrome_driver_init):    
    xpath_btn1 = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[1]/div'
    WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.XPATH,xpath_btn1)))
    chrome_driver_init.find_element(By.XPATH,xpath_btn1).click()
    
    WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.open-live-acc-form-wrapper')))
    assert "Open A Live Trading Account | Forex Trading | CFDs Trading" in chrome_driver_init.title

def test_autofill_register_step1(chrome_driver_init):
    input_click = [
        '//div[@data-testid="entity"]', # Account type
        '//div[@data-testid="country"]', # Country
        '//div[@data-testid="title"]', # Title
        '//input[@data-testid="firstname"]', # First Name
        '//input[@data-testid="middlename"]', # Middle Name (optional)
        '//input[@data-testid="lastname"]', # Last Name
        '//input[@data-testid="email"]', # Email
        '//input[@data-testid="phone"]', # Phone
    ]

    input_keys = [
        [
            '//li[@data-testid="entity0"]', # Personal
            '//li[@data-testid="country7"]', # Taiwan
            '//li[@data-testid="title0"]', # Mr
            'WU',
            '',
            'Ivan',
            'fgma51f@gmail.com',
            '0987602036',
        ],
    ]

    for i in range(1):
        WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.open-live-acc-form-wrapper')))
        chrome_driver_init.find_element(By.CSS_SELECTOR,'.open-live-acc-form-wrapper').click()
        for j in range(8):
            WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.XPATH, input_click[j])))
            if j < 3 :
                chrome_driver_init.find_element(By.XPATH,input_click[j]).click()

                WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.XPATH, input_keys[i][j])))
                chrome_driver_init.find_element(By.XPATH,input_keys[i][j]).click()
            elif j < 8 :
                chrome_driver_init.find_element(By.XPATH,input_click[j]).clear()
                chrome_driver_init.find_element(By.XPATH,input_click[j]).send_keys(input_keys[i][j])

        assert WebDriverWait(chrome_driver_init,3).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="basicInfo"]')))