# # # Using Python with the Internet # # #
# # Web API 101 # #
# 1. Web APIs are web pages for computer to read. They're similar to regular web pages -- they can require authentication,
#    allow input, downloads, etc. But the styling and formatting of the webpage is stripped away, leaving only structured
#    data in a format that computers can ingest and parse (in a process called "serialization"). Web APIs use the HTTP
#    standard, which is the same one that web browsers to us
# 2. Most web APIs (and the ones we'll be learning about) represent data in a notation called JavaScript
#    Object Notation, or JSON. For am example, check out the following webpage: https://pokeapi.co/api/v2/type
#    This page is from the unofficial Pokemon API, and it can be used to extract all sorts of useful information
#    about Pokemon.
# 3. What you're looking at on that page is JSON. What you'll notice is that it's actually very similar to the Python
#    dictionary notation. A few differences:
#    - JSON uses null instead of None
#    - JSON uses true & false instead of True and False
#    - Valid JSON can only use double quotes, no single quotes.
#    - Last, this is just text. Web APIs are text-only, so when Python reads or writes to the API it must do so as text.

# Here's a portion of what is returned on that page, as a long string in python.

json_text = '{"count":3,"next":null,"previous":null,"results":['\
            '{"name":"normal","url":"https://pokeapi.co/api/v2/type/1/"},'\
            '{"name":"fighting","url":"https://pokeapi.co/api/v2/type/2/"},'\
            '{"name":"flying","url":"https://pokeapi.co/api/v2/type/3/"}]}'

# Let's import some additional code that will help us deal with JSON.
import json, pprint

# Now we can convert this structured data to a real Python object
json_object = json.loads(json_text)

# Let's look. This uses a method from a library called Pretty Print -- it print out the JSON, nicely formatted
pprint.pprint(json_object)

# You can see that this is now a python dictionary. This particular api returns some summary data at the front,
#   including things like "count" and "results". As review, we can get to any object inside the dict by using the
#   following notation: json_object['key'], where 'key' is the string on the left of one of the colons in the dict.
print(json_object['count'])

# Let's quickly use a loop to print out name of the pokemon types we have here.
for t in json_object['results']:
    print(t['name'])

# One last JSON thing. If we want to create JSON from python objects we can do something like this:
new_type = {}
new_type['name'] = 'space'
new_type['url'] = 'https://pokeapi.co/api/v2/type/44/'
new_json_text = json.dumps(new_type)
# The variable new_json_text now has a string with the JSON version of our data. This is important if we want to
#   send this data along to a web API.

# # Talking to the Internet # #
# Now that we know what JSON is, we can use library called "requests" to actually get this data from the internet.
#  This is the first one we will use that isn't part of the standard python libraries that come with installation.
#  If you haven't already, go to the "Python Packages" and search for and install "requests".
import requests

# The HTTP standard has a few different verbs that can be used to send requests. The simplest one is "GET".
#  The requests.get() function will initiate a request to the URL specified in the arguments.
#  There are a lot of other arguments we can use, but this is the bare minimum.
response = requests.get(
    url='https://pokeapi.co/api/v2/type'
)

# Let's walk through what we got back.
#  - First, there's a response code.
print(response.status_code)
# 200 means OK. Check out more status codes at http://http.cat
# In general:
# - 300's mean you're being redirected
# - 400's mean you messed up
# - 500's means that the server messed up

# If we want metadata about ths requests, we can check the headers:
pprint.pprint(response.headers)

# if we want the raw text of the response, it's here:
print(response.text)

# But back to the good stuff. This method parses the text of the response, and converts it to a python object.
all_types = response.json()

# Now we can do our loop, like earlier.
for t in all_types['results']:
    print(t['name'])

# All of this we could easily have done in Excel. Let's have a little more fun.
# Set up an empty list
counts = []
# looping through all of the types again
for t in all_types['results']:
    # This time, we call the URL to get the details of the types
    type_response = requests.get(url=t['url'])
    # Just in case we hit an error
    if type_response.status_code != 200:
        print("ERROR!")
        continue
    # Parse the JSON
    json_obj = type_response.json()
    # Take the data (name, url, and count of pokemon in that type), and add it to the list.
    counts.append({'name': t['name'], 'url': t['url'], 'count':len(json_obj['pokemon'])})
    # Print something out so we can see how long each one takes.
    print(f"fetched {t['name']}")

# Quick as that, we have a count of the Pokemon by type:
pprint.pprint(counts)

# # Exercises:
# - Using this page documenting the "abilities" API endpoint:  https://pokeapi.co/docs/v2#abilities
#   Figure out which ability can be used by the fewest and most pokemon  (note that the abilities object has a
#   ['pokemon'] list just like the type does.
# - Using the documentation here: https://pokeapi.co/docs/v2#pokemon figure out which pokemon has access to the most
#   abilities.


