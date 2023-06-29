# Open Browser
# Go to webpage
# selenium 4
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#to run only a certain batch: pytest -v -m math   
#pytest looks for 'test' in the file name and 'test' in the functions to run

class TestPositiveScenarios:

    @pytest.mark.login  #will help us to group tests
    @pytest.mark.positive
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://practicetestautomation.com/practice-test-login")
        # time.sleep(3)
        # button=driver.find_element(By.XPATH,"//button[@class='btn']")
        username_locator=driver.find_element(By.XPATH,"//*[@id='username']")
        username_locator.send_keys("student")

        password_locator=driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # alt x path= "//button[@class='btn']"
        submit_button=driver.find_element(By.XPATH,"//*[@id='submit']")
        submit_button.click()
        time.sleep(2)

        actual_url= driver.current_url
        assert actual_url== "https://practicetestautomation.com/logged-in-successfully/"


        log_success=driver.find_element(By.CSS_SELECTOR,".post-title")
        actual_text=log_success.text
        assert actual_text=="Logged In Successfully"

        lout_button=driver.find_element(By.LINK_TEXT,"Log out")
        assert lout_button.is_displayed()

        """Test case 1: Positive LogIn test
        Open page
        Type username student into Username field
        Type password Password123 into Password field
        Puch Submit button
        Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        Verify button Log out is displayed on the new page"""