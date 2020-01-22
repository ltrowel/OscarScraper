from DAO import OscarDAO
from Model import Award

class Ceremony:

    def __init__(self, ceremony):
        self.dao = OscarDAO.OscarDAO()
        self.ceremony = ceremony
        self.awards = []

    def get_awards(self):
        awards = self.dao.get_awards()

        for x in awards:
            self.awards.append(Award.Award(self.dao, x[0], x[1], x[2]))
