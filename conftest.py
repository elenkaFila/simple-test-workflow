from selenium import webdriver
import pytest
import logging
from datetime import datetime
import os


# Configure logging
logging.basicConfig(filename=os.path.join("./logs", 'test_log.log'),
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--log_level", action="store", default="INFO")
    
# задаем браузер через cli
@pytest.fixture(autouse=True)
def driver(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":        
        options = webdriver.ChromeOptions()
        options.page_load_strategy= 'eager'
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    request.cls.driver = driver
    request.addfinalizer(driver.close)

    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger('driver')
    test_name = request.node.name
    if "\\" in test_name:
        test_name = test_name.split("\\")[0]
    log_path = f"logs/{test_name}_{datetime.now().strftime('%d-%m-%Y_%H.%M.%S')}.log"

    logger.addHandler(logging.FileHandler(log_path))
    logger.setLevel(level=log_level)
    logger.info(f"{logger.name} ===> Test {test_name} started at {datetime.now()}")

    driver.test_name = test_name
    driver.log_level = log_level
    driver.log_path = log_path
    logger.info(f"Browser: {request.config.getoption('--browser')} ")