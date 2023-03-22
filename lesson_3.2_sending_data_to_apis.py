# # Sending Data
# Up until now, we have used only HTTP *GET requests to pull data down from an API.
# Now, we will learn the POST HTTP verb, which allows us to send data up to the API.

# Requests handles this for us too.
import requests
import json
import pprint

# To start off, we'll use some example data to make a post call to a handy testing API run by a company called PostMan.
# The purpose of this api is echo back data submitted in different ways.
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
#  too). The format for query string data is to append a question mark after the path, then key=value, separated by
#  ampersand characters. You can specify something more than once (usually results in that variable being a list).
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
# Let's do something a little more fun. About 6 months ago, I wrote a little API app, backed by a simple database, that
#  allows you to get and store information about little things called Widgets.
# Some APIs have special programmatic pages that can help you learn how to use them. The link below is to a Swagger API
#  documentation page, which is a very common one.
# Documentation:  https://cuapitraining.azurewebsites.net/api/swagger/ui

# Based on the documentation, let's make a call to get all the widgets:
# Sometimes, it's helpful to store the base path of an API that you're going to call a few times:
base_url = 'https://cuapitraining.azurewebsites.net/api'
# This should produce a list of "widget" objects.
widgets = requests.get(f'{base_url}/widgets')

# Quick detour. The for loop below uses a list comprehension. It's basically a for loop in square brackets that creates
#  a list: the x is the local iteration variable that will store the values of each item in widgets.json().
#  The list will be composed of a tuple, made up of what is returned from x['sn'] and x['name'] for each of the items.
#  It's not the clearest syntax, but it's very handy for retrieving just one or two pieces of data inside dictionaries.
# Another quick note. See the ":20" in the curly braces? That will add spaces to the inserted string until it is 20
#  characters long. This is how the resulting text comes out as 2 columns. Not super important perhaps, but satisfying.
for i in [(x['sn'], x['name']) for x in widgets.json()]:
    print(f"SN: {i[0]:20}\t\t Name: {i[1]}")

# Back to the mission. There are two possible POST calls we can make here:
#  1. Make a new Widget
#  2. Filter a Widget

# Let's try the first one. First, we need some data that will fit the description of a Widget. If you scroll all the way
# to the bottom of the documentation, you can see what that looks like. I have copied it here for convenience.
#   sn*	        string
#   name	    string
#     nullable: true
#   size	    integer($int32)
#     nullable: true
#   features	[...]
#   modules	    [...]
# Based on this, we know that the SN part of the object is required, and everything else is optional.
#  Since we'll all be adding to the same database, customize the object below, so it doesn't overlap with anyone else's
new_widget = {
    'sn': 'widget-<your initials>',
    'name': 'Special Widget of <your name>',
    'size': 43,
    # Features is just a list of strings.
    'features': ['Antique', 'Makes Julian Fries', 'Will Not Break'],
    # Note that modules have a schema of their own near the bottom of the page. Very simple, just a dict of name & size.
    'modules': [{'name':'fry maker', 'size': 5},{'name':'non-breaker', 'size': 2}]
}

# Now let's make the actual POST.
new_widget_resp = requests.post(
    # Note here that we need to put the SN of the new widget in the path. Different APIs do this different ways, but
    #  this is the way this one works. Based on the documentation, you should also have the SN in the body.
    url=f"{base_url}/widgets/{new_widget['sn']}",
    # Once again, we use the json.dumps() method to convert our python Dictionary to a JSON string before sending it.
    data=json.dumps(new_widget)
)

# When we make new things, you might notice a new response code:
print(new_widget_resp.status_code)
# see: http://http.cat/201

# looks like this API returned a json object. Let's see it.
pprint.pprint(new_widget_resp.json())

# Now let's use our second POST to see if our object has been stored in the database, and if we can get it back.
#  Remember to change this to the same value as above.
filter_widget = {'sn': 'widget-nsb'}
filtered_widgets = requests.post(
    url=f"{base_url}/widgets/filter",
    data=json.dumps(filter_widget)
)
pprint.pprint(filtered_widgets.json())

# Now let's do one more thing -- let's find all the widgets of a specific size:
filter_widget_by_size = {'size': 3}
filtered_widgets_by_size = requests.post(
    url=f"{base_url}/widgets/filter",
    data=json.dumps(filter_widget_by_size)
)
pprint.pprint(filtered_widgets_by_size.json())

# Exercise: Based on the API documentation, see if you can get all the widgets with a specific module using the
#  widgets/filter endpoint on the training API.