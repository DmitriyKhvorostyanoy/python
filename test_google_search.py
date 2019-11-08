from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_google_search():
    driver = WebDriver(executable_path='C://Users//Dima//.m2//repository//webdriver//chromedriver//win32//78.0.3904.70/chromedriver.exe')
    driver.get('https://www.xt.ht/')
    enter = driver.find_element_by_xpath("//a[contains(text(),'Вход')]")
    enter.click()
    inputUsername=driver.find_element_by_name("username")
    inputUsername.send_keys("negdan4ik")
    inputPass = driver.find_element_by_name("password")
    inputPass.send_keys("246800")
    loginBtn=driver.find_element_by_name("login")
    loginBtn.click()
   # assert driver.title=="ХТ - сообщество туристов и велосипедистов"
    exitBtn=driver.find_element_by_xpath("//*[contains(text(),'Выход')]").is_displayed()


    ...