# # Sending Data
# Up until now, we have used only HTTP *GET requests to pull data down from an API.
# Now, we will learn the POST HTTP verb, which allows us to send data up to the API.

# Requests handles this for us too.
import requests
import json
import pprint

# To start off, we'll use some example data to make a post call to a handy testing API run by a company called PostMan.
# The purpose of this api is echo back data submitted in several different ways.
# We'll store the main bulk of the data in this variable
data = {'name': 'Cedarville University', 'Undergrad Population': 5000,
        'Motto': 'For the Word of God and the Testimony of Jesus Christ',
        'Divisions':[
            'Business',
            'Academic',
            'Athletic',
            'Enrollment Management',
            'Marketing and Communication'
        ]}

# We will also put two variables in the query string arguments. Query string arguments are not part of the path to the
#  web page, but they allow you to send key/value pairs along with your request (this actually works with GET requests,
#  too. The format for query string data is to append a question mark after the path, then key=value, separated by
#  ampersand characters. You can specify something more than once (usually results in that variable being a list)
resp = requests.post(
    url = 'https://postman-echo.com/post?query_arg=1&something=this&something=that',
    data = json.dumps(data)
)

# Let's see what we got.
pprint.pprint(resp.json())
# Notice the first line, where it has returned our args as a JSON object.
#   'Something' is set to a list of 'this and 'that'
#   Lots of other data in here too -- we could have sent files, form data, and altered our headers if we wanted to.

## More POSTing
# Let's do something a little more fun.