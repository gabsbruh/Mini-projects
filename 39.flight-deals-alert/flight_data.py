import requests
import constants as c
import datetime as dt

class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, max_price: float, destination_code: str):
        self.max_price = max_price
        self.origin_code = c.DEFAULT_ORIGIN_CODE
        self.destination_code = destination_code
        self.max_period_months = c.MAX_PERIOD_MONTHS
        self.no_adults = c.ADULTS
        self.dates_span = self._get_all_dates()
    
    def _get_all_dates(self):
        """Function creates strings for every date in ISO 8601 YYYY-MM-DD format, beggining from tommorow
        and ends in self.max_period (in months) date, e.g. for 6 months period in 180 days (6*30).
        
        Return (list): List of dates over the next 6 months
        """
        today = dt.datetime.today().date()
        dates = ['' for i in range(self.max_period_months*30)]
        for no_day in range(len(dates)):
            dates[no_day] = today + dt.timedelta(days=no_day+1) 
        return dates
    
    def get_cheapest_flight(self):
        pass
