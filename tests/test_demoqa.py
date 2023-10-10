import os
from selene import browser, have, command


def test_demoqa_complete_form():
    browser.open("/automation-practice-form")

    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')
    browser.element('#userEmail').type('mymail@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9171234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().type('June')
    browser.element('.react-datepicker__year-select').click().type('1985')
    browser.element('.react-datepicker__day--025').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/sample.jpg'))
    browser.element('#currentAddress').type('My current address')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()

    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'FirstName LastName',
        'mymail@test.ru',
        'Male',
        '9171234567',
        '23 June,1985',
        'Maths',
        'Reading',
        'sample.jpg',
        'My current address',
        'NCR Delhi'))
