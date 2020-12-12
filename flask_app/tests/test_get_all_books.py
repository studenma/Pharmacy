import pytest
import requests
import json

# HOW TO RUN TESTS
	# pytest								- run all tests in current folder
	# pytest test_get_all_books.py 			- run only this test file
	# py.test
	# py.test test_get_all_books_method -v 	- run a specific method in all test files, -v do something with duplicite names of methods
	# py.test -m firstTest					- run a test with firstTest mark on it
		# needs registering of mark to avoid warnings -> create pytest.ini file

@pytest.mark.firstTest # TODO: warning
def test_get_all_books_method():
	url = "http://127.0.0.1:5000//api/v1/resources/books/all"

	payload={}
	files={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload, files=files)

	assert response.status_code == 200
	# resp_body = response.json()
	# assert resp_body['ulr'] == url

# https://requests.readthedocs.io/en/master/_modules/requests/models/#Response
# print(response)
# print(response.headers)
# print(response.text)
# print(response.ok)
# print(response.status_code)
 