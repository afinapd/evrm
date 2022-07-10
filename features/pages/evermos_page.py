import time

from features.core.reusable_page import ReusablePage
from features.locators.locator import Locator
from features.locators.locator import LocatorDashboardPage
from features.locators.locator import LocatorSignInPage
from features.locators.locator import LocatorHomePage

from selenium.webdriver.common.by import By

class EvermosPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = EvermosPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def clickSignInPage(self):
        super().perform_action_on_element(LocatorDashboardPage.SIGNIN_BUTTON, "click")
        super().wait_for_page_load()

    def verifySignInPage(self):
        super().verify_url("https://evermos.com/login")

    def inputNoHpPassword(self, noHP, password):
        super().perform_action_on_element(LocatorSignInPage.NOHP_TEXTFIELD, "type", noHP)
        super().perform_action_on_element(LocatorSignInPage.PASSWORD_TEXTFIELD, "type", password)

    def clickSignInButton(self):
        super().perform_action_on_element(LocatorSignInPage.SIGNIN_BUTTON, "click")

    def verifyHomePage(self):
        super().element_exists(LocatorHomePage.BERANDA_NAVBAR)

evermosPage = EvermosPage.get_instance()
