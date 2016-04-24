

from base import Base

class DailyLog(Base):
    def __init__(self):
        Base.__init__(self)
        self.collection = self.db['daily_logs']
