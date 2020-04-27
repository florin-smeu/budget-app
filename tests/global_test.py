import requests

token = 'INVALID TOKEN'

def test_auth(api_route_fragment, email):
    global token

    url = "http://localhost:8886/" + api_route_fragment
    params = {'email': email, 'password_hash': '41e2cbe589cb11ecdc9c82feb0710ff119fe36c018ab2bd0e93a7009f478a99c'}
    response = requests.post(url, params=params)

    print("\nTEST ==", api_route_fragment, "==")
    print(response.status_code)
    print(response.json())
    token = response.json()['token']


def generic_test(api_route_fragment):
    global token
    url = "http://localhost:8888/" + api_route_fragment
    params = {'token': token}
    response = requests.get(url, params=params)
    print("\nTEST ==", api_route_fragment, "==")
    print(response.status_code)
    print(response.json())


def generic_test_dates(api_route_fragment, date1, date2):
    global token
    url = "http://localhost:8888/" + api_route_fragment
    params = {'token': token, 'date1': date1, 'date2': date2}
    response = requests.get(url, params=params)
    print("\nTEST ==", api_route_fragment, "==")
    print(response.status_code)
    print(response.json())


def main():
    global token
    """ Test suite """
    test_auth("signup", "petrica@gmail.com")

    test_auth("signin", "fsmeu@gmail.com")
    generic_test("avg_daily_exp")
    generic_test("avg_daily_inc")
    generic_test("daily_detailed_exp")
    generic_test("daily_detailed_inc")

    generic_test_dates("exp_between_dates", '2020/01/01', '2020/05/05')
    generic_test_dates("inc_between_dates", '2020/01/01', '2020/05/05')

if __name__ == "__main__":
    main()
