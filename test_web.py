import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import logging

from discord_webhook import DiscordWebhook
import os
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_web")

    

@allure.feature('Test Demo')
@allure.story("Test Web")
def test_web():
    # when run it locally update to Service()
    service = Service(executable_path="/usr/bin/chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.set_capability("browserName", "chromium")
	

    try:
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        driver = webdriver.Remote(
            command_executor='http://chromium:4444',
            options=chrome_options)
        
        driver.set_window_size(width=1920, height=1080)
        driver.maximize_window()

        logging.info("get to appworks website")
        driver.get("https://appworks.tw")
        
        logging.info("assert driver title has Home - AppWorks 之初加速器")
        assert "Home - AppWorks 之初加速器" in driver.title
   
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise e
    finally:
        if 'driver' in locals() and driver is not None:
            driver.quit()


