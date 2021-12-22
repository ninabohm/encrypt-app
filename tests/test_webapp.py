import unittest
from flask import url_for
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

from webapp import app

logger = logging.getLogger(__name__)


class TestWebapp(unittest.TestCase):

    def setUp(self):
        ser = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=ser)
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
        input_element = self.driver.find_element_by_css_selector(f'[id="username"]')
        self.assertIsNotNone(input_element)

    def test_given_post_to_encryption_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.get("/encryption")
            assert response._status_code == 200

    def test_given_post_to_result_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.post("/result")
            assert response._status_code == 200

