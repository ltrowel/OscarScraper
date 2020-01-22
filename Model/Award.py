from OscarScraper import scraper

class Award:

    def __init__(self, dao, id, name, has_nominee):
        self.dao = dao
        self.id = id
        self.name = name
        self.has_nominee = has_nominee

    def get_nominees_for_ceremony(self, ceremony):
        nominees = scraper.get_nominees_for_award_by_ceremony(ceremony, self.name)

        for x in nominees:
            print(x)
