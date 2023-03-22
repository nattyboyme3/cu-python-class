# # API Authentication
# In this final lesson, we'll learn some of the ways that are common to do authentication with APIs.
# Unfortunately, this is both the hardest part of using any API, and the hardest to teach, because there are so many
#  ways of doing authentication between all the different API implementations out there. Your best bet is to read the
#  documentation of the specific API you're working with. Given the terms you are now familiar with, and the experience
#  you've had making API calls, you should be able to figure it out.
import requests
import pprint

# First, we'll do a simple example using the training API from last lesson. I don't publish the key on GitHub, so check
# the email I sent out before class for a key to copy in. Paste it here.
code = ''

# First, as an example, we will call the widgets api with no authentication to see what happens
base_url = 'https://cuapitraining.azurewebsites.net/api'
bad_request = requests.get(f"{base_url}/auth/widgets")
# We do not get a 200 (OK) status code:
print(bad_request.status_code)
# For reference: http://http.cat/401

# Now let's put the code in there as a URL parameter
# This should produce a list of "widget" objects. Remember, add a '?' to the path, then key-value pairs separated by '&'
widgets = requests.get(f'{base_url}/auth/widgets?code={code}')
# now we get our data:
if widgets.status_code == 200:
    widgets_data = widgets.json()
    print(f"Got Response: {widgets.status_code} with {len(widgets_data)} widgets")

# Some APIs use Basic Authentication. I couldn't easily find one that we could use to test this out, so this is just an
# example. Requests has similar support for all the common Authentication methods, like Digest and Proxy.
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth(username='joe',  password='password')
fake_data = requests.get('https://some.big.url/api/test', auth=auth)

# If you don't want to specify this every time, you can set up a session with requests to use the same authentication
#  over and over again:
session = requests.Session()
# We add the authentication, as from above.
session.auth = auth
# then, use the session to make the GET, and it will automatically use the specified authentication info.
more_fake_data = session.get('https://some.big.url/api/test')

# Some APIs use header authentication. For testing this one, we'll use Canvas.
# Go to https://cedarville.instructure.com/profile/settings, and scroll down until you see the "New Access Token"
#  button. Click it, and give it a name like "api testing" and make it expire tomorrow. Copy the string they give you,
#  and paste it in as "token" below.
#  For this authentication method, we will use an Authorization header, and the word "Bearer" Headers in requests are
#  just a dictionary of keys & values. The keys will vary between API implementations, but this is a common format:
token = 'your-token-here'
canvas_headers = {'Authorization': f'Bearer {token}'}
base_url = 'https://cedarville.instructure.com/api/v1'
canvas_data = requests.get(f'{base_url}/users/self', headers=canvas_headers)
# This should be your user info from Canvas!
if canvas_data.status_code == 200:
    pprint.pprint(canvas_data.json())

# Many APIs will have you log in the first time using something like Basic Auth, and then require the token afterwards.
# You can keep common headers around in a session, too, like this:
canvas_session = requests.Session()
canvas_session.headers.update(canvas_headers)

# Now, each request from this session will send the Authorization header along.
canvas_data_2 = canvas_session.get(f'{base_url}/users/self/activity_stream')
if canvas_data_2.status_code == 200:
    pprint.pprint(canvas_data_2.json())
