"""A simple checker for types of functions in bridge_functions.py"""

import pytest
import checker_generic
import bike_share as bikes

FILENAME = 'bike_share.py'
PYTA_CONFIG = 'a2_pythonta.json'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {
    'ID': 0,
    'NAME': 1,
    'CAPACITY': 2,
    'BIKES_AVAILABLE': 3,
    'DOCKS_AVAILABLE': 4,
    'LATITUDE': 5,
    'LONGITUDE': 6,
    'NO_KIOSK': 'SMART',
    'EARTH_RADIUS': 6371
}


def _check(func: callable, args: list, expected: type) -> tuple[bool, object]:
    """Check if a call to func(args) returns a result with type expected.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.
    """
    try:
        returned = func(*args)
    except Exception as exn:
        return False, _error_message(func, args, exn)

    if isinstance(returned, expected):
        return True, returned

    return False, _type_error_message(func, expected.__name__, returned)


def _check_nested_type(func: callable, args: list, tp: type):
    """Check if func(args) returns a list of elements of type tp.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.

    """

    success, result = _check(func, args, list)
    if not success:
        return False, result

    msg = _type_error_message(func, 'list of {}s'.format(tp.__name__), result)

    for item in result:
        if not isinstance(item, tp):
            return False, msg

    return True, result


def _type_error_message(func: callable, expected: str, got: object) -> str:
    """Return an error message for function func returning got, where the
    correct return type is expected.
    """
    return f'{func.__name__} should return a {expected}, but ' \
           f'instead it returned {got}.'


def _error_message(func: callable, args: list, error: Exception) -> str:
    """Return an error message: func(args) raised an error."""
    args = str.join(',', map(str, args))
    return f'The call {func.__name__}({args}) caused an error: {error}'


class TestChecker:
    """Sanity checker for assignment functions."""
    module = bikes

    def create_sample_stations(self) -> list:
        return [
            [7090, 'Danforth Ave / Lamb Ave', 15, 4, 10,
             43.681991, -79.329455],
            [7486, 'Gerrard St E / Ted Reeve Dr', 24, 5, 19,
             43.684261, -79.299332],
            [7571, 'Highfield Rd / Gerrard St E - SMART', 19, 14, 5,
             43.671685, -79.325176]]

    def test_convert_data(self) -> None:
        d = [['abc', '123', '45.6', 'car', 'Bike']]
        original = [['abc', '123', '45.6', 'car', 'Bike']]
        self._check(bikes.convert_data, [d], type(None))
        self._check_mutation(bikes.convert_data, d, original)

    def test_has_kiosk(self) -> None:
        stations = self.create_sample_stations()
        self._check(bikes.has_kiosk, [stations[0]], bool)

    def test_get_station_info(self) -> None:
        stations = self.create_sample_stations()
        self._check_list_of_Ts(bikes.get_station_info, [7090, stations],
                               [str, int, int, bool])

    def test_get_column_sum(self) -> None:
        stations = self.create_sample_stations()
        self._check(bikes.get_column_sum, [4, stations], int)

    def test_get_stations_with_kiosks(self) -> None:
        stations = self.create_sample_stations()
        self._check_list_of_Ts(bikes.get_stations_with_kiosks, [stations],
                               int)

    def test_get_nearest_station(self) -> None:
        stations = self.create_sample_stations()
        self._check(bikes.get_nearest_station, [43.7, -79.3, stations], int)

    def test_rent_bike(self) -> None:
        stations = self.create_sample_stations()
        original = self.create_sample_stations()
        self._check(bikes.rent_bike, [7090, stations], bool)
        self._check_mutation(bikes.rent_bike, stations, original)

    def test_return_bike(self) -> None:
        stations = self.create_sample_stations()
        original = self.create_sample_stations()
        self._check(bikes.return_bike, [7090, stations], bool)
        self._check_mutation(bikes.return_bike, stations, original)

    def test_upgrade_stations(self) -> None:
        stations = self.create_sample_stations()
        original = self.create_sample_stations()
        self._check(bikes.upgrade_stations, [20, 10, stations], int)
        self._check_mutation(bikes.upgrade_stations, stations, original)

    def _check(self, func: callable, args: list, desired_type: type,
               nested: bool = False) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.
        """
        if not nested:
            result, message = _check(func, args, desired_type)
        else:
            result, message = _check_nested_type(func, args, desired_type)

        print(message)
        assert result is True, message

    def _check_list_of_Ts(self, func: callable, args: list, types: list) -> None:
        """Check that func called with arguments args returns a list of type
        types.
        """
        result, message = checker_generic.returns_list_of_Ts(func, args, types)
        print(message)
        assert result is True, message

    def _check_no_mutation(self, func: callable, actual, expected) -> None:
        """Check that func does not mutate the argument actual so that it still
        matches expected.
        """
        assert expected == actual, '{0} should not mutate its arguments'.format(
            func.__name__)

    def _check_mutation(self, func: callable, actual, expected) -> None:
        """Check that func mutates the argument actual so that it is different
        from expected.
        """
        assert expected != actual, '{0} should mutate its list argument'.format(
            func.__name__)

    def test_check_constants(self) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in CONSTANTS.items():
            actual = getattr(self.module, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            assert expected == actual, msg


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
pytest.main(['--show-capture', 'no', '--disable-warnings', '--tb=short',
             'a2_checker.py'])
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contract\n')
