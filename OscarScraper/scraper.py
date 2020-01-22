from bs4 import BeautifulSoup
import requests


def __get_ceremony_name(ceremony_number):
    # Find the ordinal indicator based on the last digits of the number
    # Anything that is a 'teen' breaks the usual rules of 1st, 2nd, 3rd
    last_digit = ceremony_number % 10
    second_to_last_digit = int((ceremony_number / 10)) % 10

    ordinal_indicator = 'th'
    if last_digit == 1 and second_to_last_digit != 1:
        ordinal_indicator = 'st'
    elif last_digit == 2 and second_to_last_digit != 1:
        ordinal_indicator = 'nd'
    elif last_digit == 3 and second_to_last_digit != 1:
        ordinal_indicator = 'rd'

    return '{number}{ordinal_indicator} Academy Awards'.format(
        number=ceremony_number,
        ordinal_indicator=ordinal_indicator
    )


def __get_wiki_for_ceremony(ceremony):
    # Scrape wikipedia page
    url = "https://en.wikipedia.org/wiki/{ceremony}".format(ceremony=ceremony).replace(' ', '_')

    request = requests.get(url)
    content = request.content
    return BeautifulSoup(content, 'html.parser')


def __get_nominees_for_award(award, html_content):
    award_html = html_content.find('a', text=award)

    return map(
        lambda x: x.text,
        award_html.find_parent('td').find_all('i')
    )


def get_nominees_for_award_by_ceremony(ceremony_number, award):
    # Calculate the award ceremony based on the year
    ceremony = __get_ceremony_name(ceremony_number)

    # Get the Wiki Page Content to Parse
    wiki_content = __get_wiki_for_ceremony(ceremony)

    # Get the nominees for the given award
    return __get_nominees_for_award(award, wiki_content)
