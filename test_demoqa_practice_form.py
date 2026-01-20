import pytest
from selene import browser, have
import os

def test_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivan_ivanov@yandex.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9481234587')
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element('option[value="8"]').click()
    browser.element(".react-datepicker__year-select").element('option[value="1950"]').click()
    browser.element(".react-datepicker__day.react-datepicker__day--013").click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('python.jpg'))
    browser.element('#currentAddress').type('John Doe 123 Main Street Anytown, CA 90210 USA')
    browser.element("#state").click()
    browser.element('#react-select-3-option-1').click()
    browser.element("#city").click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()


    browser.element('.table-responsive').should(have.text('Ivan Ivanov'))
    browser.element('.table-responsive').should(have.text('ivan_ivanov@yandex.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('9481234587'))
    browser.element('.table-responsive').should(have.text('13 September,1950'))
    browser.element('.table-responsive').should(have.text('Maths'))
    browser.element('.table-responsive').should(have.text('Reading'))
    browser.element('.table-responsive').should(have.text('python.jpg'))
    browser.element('.table-responsive').should(have.text('John Doe 123 Main Street Anytown, CA 90210 USA'))
    browser.element('.table-responsive').should(have.text('Uttar Pradesh Agra'))







