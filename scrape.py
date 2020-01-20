#
# Run the Oscar Scraper
#


# Get the ceremony name give the year
def get_ceremony_from_year(year):
    # First Oscar's was in 1929, but there were two ceremonies in 1930
    # TODO: Figure out how to scrape the 2nd and 3rd ceremonies better
    ceremony_number = year - 1928
    # The modulo of 10 will return the last digit of any number
    ceremony_last_digit = ceremony_number % 10
    ordinal_indicator = 'th'
    if ceremony_last_digit == 1:
        ordinal_indicator = 'st'
    elif ceremony_last_digit == 2:
        ordinal_indicator = 'nd'
    elif ceremony_last_digit == 3:
        ordinal_indicator = 'rd'

    return '{number}{ordinal_indicator} Academy Awards'.format(
        number=ceremony_number,
        ordinal_indicator=ordinal_indicator
    )


# Take in the year from the user
year = int(input("What year do you want to scrape? "))

# Calculate the award ceremony based on the year
ceremony = get_ceremony_from_year(year)

print ("Finding results for {ceremony}".format(ceremony=ceremony))