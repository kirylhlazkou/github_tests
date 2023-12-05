import logging

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.mark.smoke
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('wewewe@wrerte.com', 'sdkfjshdkfjshdf')
    LOGGER.info('User logged in')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )
    LOGGER.info('Test result is Ok')


@pytest.mark.regression
def test_correct_email_with_incorrect_pass(login_page):
    login_page.open_page()
    login_page.fill_login_form('existint@email.com', 'non-existing-pass')
    LOGGER.info('User logged in')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )
    LOGGER.info('Test result is Ok')