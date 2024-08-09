from datetime import datetime


def check_status(date: datetime):
    return date.date() <= datetime.today().date()
