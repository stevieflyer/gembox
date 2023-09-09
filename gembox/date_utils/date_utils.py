import datetime


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
    assert isinstance(start, datetime.date) and isinstance(end,
                                                           datetime.date), f"start and end should be datetime.date objects, got {type(start)} and {type(end)}."
    assert start <= end, f"start should be earlier or the same as end, got start: {start}, end: {end}."
    assert isinstance(n_periods, int) and n_periods > 0, f"n_periods should be a positive integer, got {n_periods}."
    total_days = (end - start).days + 1
    assert total_days >= n_periods, f"n_days: {total_days} should be no less than n_periods: {n_periods}."

    days_per_period = total_days // n_periods
    extra_days = total_days % n_periods

    result = []
    current_date = start

    for i in range(n_periods):
        period_days = days_per_period + (1 if i < extra_days else 0)
        period_end = current_date + datetime.timedelta(
            days=period_days - 1)  # Subtract 1 because the start date is included
        result.append((current_date, period_end))
        current_date = period_end + datetime.timedelta(
            days=1)  # Start the next period the day after the previous one ends

    return result
