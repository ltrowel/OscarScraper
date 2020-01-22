from OscarScraper import scraper
from Model import Ceremony
#
# Run the Oscar Scraper
#


# Take in the year from the user
# year = int(input("What year do you want to scrape? "))
# award = input("What award do you want to scrape? ")
#
# print("Getting nominees for {award} in {year}".format(award=award, year=year))
#
# nominees = scraper.get_nominees_for_award_by_year(year, award)
#
# for nominee in nominees:
#     print(nominee)

ceremony = Ceremony.Ceremony(92)
ceremony.get_awards()