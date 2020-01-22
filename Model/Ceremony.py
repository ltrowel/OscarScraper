from DAO import OscarDAO


class Ceremony:

    def __init__(self, ceremony):
        self.dao = OscarDAO.OscarDAO()
        self.ceremony = ceremony
        self.awards = []

    def get_awards(self):
        awards = self.dao.get_awards()

        for x in awards:
            print(x)
