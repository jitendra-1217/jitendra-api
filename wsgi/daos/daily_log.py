

from base import Base

class DailyLog(Base):

    daily_log_schema = {
        'is_private': {
            'type': 'boolean',
            'required': True
            # 'defaults': False
        },
        'tags': {
            'type': 'list',
            'allowed': [
                'work-life',
                'personal-life'
            ],
            'required': False,
            'empty': True
        },
        'text': {
            'type': 'string',
            'required': True,
            'minlength': 5
        }
    }

    def __init__(self):
        Base.__init__(
            self,
            'daily_logs',
            DailyLog.daily_log_schema)
