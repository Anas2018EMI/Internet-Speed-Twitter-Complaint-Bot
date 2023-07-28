from selenium import webdriver
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/home/msi/Ma formation/100 Days of Code - The Complete Python Pro Bootcamp for 2021/C) Intermediate +/Course/Web Scraping & Automation/7) Selenium Webdriver Browser and Game Playing Bot/Chrome Driver 115/chromedriver-linux64/chromedriver"
brave_browser_path = '/usr/bin/brave-browser'

URL_SPEED_TEST = "https://www.speedtest.net/"
TWITTER_LOGIN_PAGE = "https://twitter.com/i/flow/login"

EMAIL = "Type your email "
PASSWORD = "Type your password"
USERNAME = "Type your username"
ISP_name="Type your ISP name"
min_intenet_speed_down = 12  # Type your internet download speed in Mb/s
min_intenet_speed_up = 2  # Type your internet upload speed in Mb/s



class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.up = 0
        self.down = 0
        chrome_service = Service(executable_path=chrome_driver_path)
        chrome_options = Options()
        chrome_options.binary_location = brave_browser_path
        self.driver = webdriver.Chrome(
            service=chrome_service, options=chrome_options)

    def get_internet_speed(self):
        """Gets internet speeds for download and upload from a website and store them in 
        two properties
        """
        self.driver.get(url=URL_SPEED_TEST)
        time.sleep(2)

        go_btn = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(60)

        download_speed_el = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(download_speed_el.text)
        print(self.down)

        upload_speed_el = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(upload_speed_el.text)
        print(self.up)

    def tweet_at_provider(self):
        """Logins in your Twitter account and tweets a complaint about internet speed
        """
        self.driver.get(url=TWITTER_LOGIN_PAGE)
        time.sleep(5)

        email = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)
        time.sleep(2)

        login_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, 'div[role="button"]')
        next_btn = login_buttons[2]
        next_btn.click()
        time.sleep(2)

        # Phone or username webpage:
        try:

            h1 = self.driver.find_element(By.TAG_NAME, 'h1')
            span = h1.find_element(By.CSS_SELECTOR, 'span>span')
            if span.text == "Enter your phone number or username":
                username = self.driver.find_element(By.TAG_NAME, 'input')
                username.send_keys(USERNAME)
                time.sleep(2)

                # next_btn_1 = self.driver.find_element(
                #     By.CSS_SELECTOR, 'div[role="button"]')
                # next_btn_1.click()

                #####
                # I will click on Next by myself since twitter blocks my bot!!!!!!
                ########
                time.sleep(10)
                # self.driver.implicitly_wait(5)

        finally:

            password = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)
            time.sleep(2)

            login_btn = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            login_btn.click()
            time.sleep(4)

            # Get rid of any popup message
            # header = self.driver.find_element(
            #     By.CSS_SELECTOR, 'header[role="banner"]')
            # header.click()
            # time.sleep(2)

            if self.down < min_intenet_speed_down or self.up < min_intenet_speed_up:

                msg = f"Hey {ISP_name}, why is my internet speed {self.down} Mbps down/ {self.up} Mbps up, when I paid for 12 Mbps down and at least 2 Mbps up????????"
                txt_el = self.driver.find_element(
                    By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
                txt_el.send_keys(msg)
                time.sleep(1)
                tweet = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
                tweet.click()


##############################################################################################
iam_bot = InternetSpeedTwitterBot()

iam_bot.get_internet_speed()
iam_bot.tweet_at_provider()
