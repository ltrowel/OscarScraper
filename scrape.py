from bs4 import BeautifulSoup
import requests

#
# Run the Oscar Scraper
#


# Get the ceremony name give the year
# TODO: This can probably be in a helper file or something
def get_ceremony_from_year(year):
    # TODO: Validation Cases:
    # - Before 1929
    # - After current year
    # - 1930 two ceremonies

    # First Oscar's was in 1929, but there were two ceremonies in 1930
    ceremony_number = year - 1928

    # Find the ordinal indicator based on the last digits of the number
    # Anything that is a 'teen' breaks the usual rules of 1st, 2nd, 3rd
    last_digit = ceremony_number % 10
    second_to_last_digit = int((ceremony_number/10)) % 10

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


def get_wiki_for_ceremony(ceremony):
    # Scrape wikipedia page
    url = "https://en.wikipedia.org/wiki/{ceremony}".format(ceremony=ceremony).replace(' ', '_')

    print(url)

    request = requests.get(url)
    content = request.content
    return BeautifulSoup(content, 'html.parser')


def get_nominees_for_award(award, html_content):
    award_html = html_content.find('a', text=award)

    return map(
        lambda x: x.text,
        award_html.find_parent('td').find_all('i')
    )


def get_nominees_for_award_by_year(year, award):
    # Calculate the award ceremony based on the year
    ceremony = get_ceremony_from_year(year)

    # Get the Wiki Page Content to Parse
    wiki_content = get_wiki_for_ceremony(ceremony)

    # Get the nominees for the given award
    return get_nominees_for_award(award, wiki_content)


# Take in the year from the user
year = int(input("What year do you want to scrape? "))
award = input("What award do you want to scrape? ")

print("Getting nominees for {award} in {year}".format(award=award, year=year))

nominees = get_nominees_for_award_by_year(year, award)

for nominee in nominees:
    print(nominee)
