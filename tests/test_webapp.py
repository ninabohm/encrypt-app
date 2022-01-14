import unittest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webapp import app
from webapp import check_if_user_exists
from sqlalchemy.orm.exc import NoResultFound
from models import User

logger = logging.getLogger(__name__)


class TestWebapp(unittest.TestCase):

    def setUp(self):
        ser = Service("./chromedriver")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(service=ser, options=options)
        self.driver.get("http://localhost:5000")


    def tearDown(self):
        self.driver.quit()

    def test_given_app_running_index_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.get("/")
            assert response._status_code == 200

    def test_given_index_browser_title_contains_welcome(self):
        self.assertIn("Welcome", self.driver.title)

    def test_index_has_input_for_login(self):
        input_element = self.driver.find_element(By.CSS_SELECTOR, f'[id="user_name"]')
        self.assertIsNotNone(input_element)

    def test_given_get_login_returns_200(self):
        with app.test_client() as client:
            response = client.get("/login")
            assert response._status_code == 200

    def test_given_user_exists_return_user_as_obj(self):
        # requirement: no user with use_name = "xyz" in data.db
        with app.app_context():
            with self.assertRaises(NoResultFound):
                check_if_user_exists("xyz")



