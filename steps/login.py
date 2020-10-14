from behave import given, when, then
from framework.Main import main
from pages.login import login


@given(u'Go to https://clarity.dexcom.com/')
def step_impl_load_website(context):
    main.load_website()


@when(u'Click on the Home Page')
def step_impl_home_page(context, page):
    login.verify_Dexcom()


@when(u' Enter the "{Username}" and "{Password}"')
def step_impl_verify_username(context, Username, Password):
    verify_Login(Username,Password)
    
@then(u'Click on Login Page')
def step_impl_login_button(context):
    login.verify_Click()    