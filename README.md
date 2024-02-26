# CS361-S2.6
A. Simply perform you need to make an HTTP GET request at the root of https://valid-url.adaptable.app/.

Example using Python:
import requests
response = requests.get(https://valid-url.adaptable.app/)
data = response.json()

B. The microservice is set up to handle incoming GET requests. It will return a URL as JSON data. Receive the response (see 'data = response.json()' above) and parse the JSON from this format: {"url":"https://example.com"}. For further clarification, see test-call.py.

C. UML sequence diagram: ![UML sequence diagram](https://github.com/davidkrigbaum/CS361-S2.6/blob/main/UML.jpg)