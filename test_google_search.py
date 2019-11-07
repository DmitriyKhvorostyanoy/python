from selenium.webdriver.chrome.webdriver import WebDriver


def test_google_search():
    driver = WebDriver(executable_path='C://Users//Dima//.m2//repository//webdriver//chromedriver//win32//78.0.3904.70/chromedriver.exe')
    driver.get('https://www.google.com/')
    print(None)

    ...