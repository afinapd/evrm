from behave import *

from features.core.base_page import basePage
from features.pages.evermos_page import evermosPage


@given('launch chrome browser')
def lauchBrowser(self):
    basePage.get_driver()

@step('user open evermos page')
def openEvermosPage(self):
    basePage.navigate("https://evermos.com/")

@step('user go to sign in page')
def goToSignInPage(self):
    evermosPage.clickSignInPage()
    evermosPage.verifySignInPage()

@step('user login with no HP "{noHP}" and password "{password}"')
def signIn(self, noHP, password):
    evermosPage.inputNoHpPassword(noHP, password)
    evermosPage.clickSignInButton()

@step('user successfully login to the homepage')
def successSignIn(self):
    evermosPage.verifyHomePage()

@step('close browser')
def closeBrowser(self):
    basePage.close_browser()
