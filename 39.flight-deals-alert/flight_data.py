import requests
import constants as c
import datetime as dt
from ratelimit import limits, sleep_and_retry
from flight_search import FlightSearch

class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, max_price: float, destination_code: str,
                 currency: str='PLN'):
        self.max_price = max_price
        self.origin_code = c.DEFAULT_ORIGIN_CODE
        self.destination_code = destination_code
        self.max_period_months = c.MAX_PERIOD_MONTHS
        self.no_adults = c.ADULTS
        self.currency = currency
        self.dates_span = self._get_all_dates()
    
    def _get_all_dates(self):
        """Function creates strings for every date in ISO 8601 YYYY-MM-DD format, beggining from tommorow
        and ends in self.max_period (in months) date, e.g. for 6 months period in 180 days (6*30).
        
        Return (list): List of dates over the next 6 months
        """
        today = dt.datetime.today().date()
        dates = ['' for i in range(self.max_period_months*30)]
        for no_day in range(len(dates)):
            day = today + dt.timedelta(days=no_day+1)
            dates[no_day] = day.strftime(r'%Y-%m-%d')
        return dates
    
    def get_cheapest_flight(self, min_days: int=4, max_days: int=4) -> dict:
        """This method uses FlightSearch.checkflight() method for finding flights and
        look for cheapest flight in specified date span
        
        Args:
            min_days(int): minimum duration of days between departure date and arrival
                           on origin location
            max_days(int): maximum duration of days between departure date and arrival
                           on origin location
        Returns:
            dict: Information about cheapest flight
        """
        @sleep_and_retry
        @limits(calls=c.RATE, period=c.PERIOD)
        def check_flight(date, duration):
            """Wrapped single operation of retrieving data from API, in order to
            impose limit on number of calls

            Args:
                date (str): date to analyze
                duration (int): duration of getaway

            Returns:
                json: data about avaiable flights which met defined circumstances
            """
            flights = FlightSearch()
            flight_data = flights.check_flight(olc=self.origin_code,
                                                dlc=self.destination_code,
                                                dep_date=self.dates_span[date],
                                                ret_date=self.dates_span[date+duration],
                                                adults=self.no_adults,
                                                max_price=self.max_price
                                                )
            return flight_data
        
        data_about_cheapest_flight = {'price': float('inf'),
                                      'departureDate': None, 
                                      'departureCarrier': None,
                                      'arrivalDate': None,
                                      'arrivalCarrier': None}
        # range is for number of dates limited by max_days (to not exceed iteration)
        for date in range(len(self.dates_span)-max_days):
            # checks all variations of visit duration specified by method arguments
            for duration in range(min_days, max_days+1):
                flight_data = check_flight(date, duration)
                try:
                    total_price = float(flight_data['data'][0]['price']['grandTotal']) # for all passengers back and forth
                except (KeyError, TypeError, IndexError):
                    continue
                else:
                    if total_price < data_about_cheapest_flight['price']:
                        data_about_cheapest_flight['price'] = total_price
                        data_about_cheapest_flight['departureDate'] = flight_data['data'][0]['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
                        dep_carrier_code = flight_data['data'][0]['itineraries'][0]['segments'][0]['carrierCode']
                        data_about_cheapest_flight['departureCarrier'] = flight_data['dictionaries']['carriers'][dep_carrier_code]
                        data_about_cheapest_flight['arrivalDate'] = flight_data['data'][0]['itineraries'][1]['segments'][0]['arrival']['at'].split("T")[0]
                        arr_carrier_code = flight_data['data'][0]['itineraries'][1]['segments'][0]['carrierCode']
                        data_about_cheapest_flight['arrivalCarrier'] = flight_data['dictionaries']['carriers'][arr_carrier_code]
                finally:
                    print(f'{flight_data}\n\n\n')
                    del flight_data
        print(data_about_cheapest_flight)
f = FlightData(max_price=2000, destination_code='PAR')
f.get_cheapest_flight()     
