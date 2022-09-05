import pytest
from pytest_bdd import scenario, given, when, then
from pages.cards import Cards
import uuid

card_title = str(uuid.uuid1())
card_title_addon = '-This title is edited-'


@pytest.fixture
def browser():
    cards = Cards()
    return cards



@scenario('../features/cards.feature', 'Check that user is able to create cards on Trello board')
def test_create_card():
    pass


@scenario('../features/cards.feature', 'Check that user can update card on Trello board')
def test_update_card():
    pass


@scenario('../features/cards.feature', 'Check that user can delete card from the Trello board')
def test_delete_card():
    pass


@given('that Im logged in to Trello')
def go_to_trello(browser):
    browser.go_to_homepage()
    browser.login()


@when('I go to the board')
def go_to_the_board(browser):
    browser.go_to_board()


@when('create card')
def create_card(browser):
    browser.create_card(card_title)


@then('newly created card is shown on the Trello board')
def card_is_on_board(browser):
    assert browser.get_card_title(card_title) == card_title


@when('update card')
def update_card(browser):
    browser.edit_card(card_title, card_title_addon)


@then('changes will be shown in the card')
def show_changes(browser):
    assert browser.get_card_title(card_title_addon + card_title) == card_title_addon + card_title


@when('I archive card and I delete archived card')
def delete_card(browser):
    browser.delete_card(card_title)


@then('deleted card wont be shown on the Trello board')
def check_card_is_deleted(browser):
    assert browser.card_deleted(card_title)
