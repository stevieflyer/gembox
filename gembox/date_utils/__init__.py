from .date_utils import (
    split_date_evenly,
)
'''
def split_date_evenly(start: datetime.date, end: datetime.date, n_periods: int) -> list[tuple[datetime.date, datetime.date]]:
    """
    Split the date range evenly into n periods.

    e.g.
    start = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 1, 10)
    n_periods = 3

    return [(datetime.date(2021, 1, 1), datetime.date(2021, 1, 3)), (datetime.date(2021, 1, 4), datetime.date(2021, 1, 6)), (datetime.date(2021, 1, 7), datetime.date(2021, 1, 10))]

    :param start: (datetime.date) the start date
    :param end: (datetime.date) the end date
    :param n_periods: (int) the number of periods
    :return: (list[tuple[datetime.date]]) a list of tuples, each tuple contains two `datetime.date` objects
    """
    pass
'''