# # File IO # #

# In order to get data into python, we need to learn how to read files.
# Thankfully, this is built into Python, and doesn't require too much code:

# We have sample csv with some data in it. It's all bogus data, so we don't need to worry about messing it up.
filename = 'sample.csv'

# It's a big file, so let's only print 5
limit = 5
count = 0
# This line opens up a file for reading. Rhe "r" means "read".
with open(filename, "r") as csv_file:
    # Anything inside this code block can access the file as the variable csv_file
    # Conveniently, as soon as we leave this block, the file will be closed and the connections cleaned up.
    for line in csv_file:
        # Make sure we don't exceed out limit
        if count > limit:
            break
        # Print the first 5 lines. The rstrip makes sure it doesn't print the extra line return at the end of the line.
        print(line.rstrip())
        # Make sure we're counting lines
        count += 1

# Ok, but we don't want to just print the file. How about getting the first five lines into a variable?
# That way we'll be able to manipulate the data:
# Let's set up something to keep the data in.
lines = []
# Ok, now lets pull that data in
limit = 5
count = 0
with open(filename, "r") as csv_file:
    for line in csv_file:
        # We don't want the first line -- header info
        if count == 0:
            count += 1
            continue
        if count > limit:
            break
        lines.append(line)
        count += 1

# Now we have the data, let's pull out the names and phone numbers.
# They're in the 2nd and 4th field (index 1 and 3, respectively), so we can do something like this:
people = {}
# loop through each line
for line in lines:
    # Split up the data on the commas (this yields a list of strings with no commas in it)
    data = line.split(',')
    people[data[1]] = data[3]

# Now lets look at our data! This loops through each (k)ey and (v)alue in our "people" dictionary
# (remember how methods can return 2 values? This is an example)
print("Output 1:")
for k, v in people.items():
    print(f"Name: {k}, Phone: {v}")


# Ok, making progress, but what if we want to write this reformatted data back out to a file?
# Turns out, it's almost the same as reading a file.
# Let's put it in a different filename:
out_filename = "output.csv"
# This time we use "w" for "write". This will overwrite any existing file with this name.
# We could also use "a" "append" which would add to an existing file.
with open(out_filename, "w") as out_file:
    # we need to add line returns so that each record is on its own line
    out_file.write("name,phone-number\n")
    for k, v in people.items():
        out_file.write(f"{k},{v}\n")

# Now, you can check out the output.csv file we've created by opening it in Excel.

# Now that you know how to do it the hard way, Python provides us a much easier way:
import csv

limit = 10
count = 0
data = []
with open(filename, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if count > limit:
            break
        # Doing it this way, each row is a dictionary, making a lot of things easier.
        data.append(row)
        count += 1

# Now we can get to the data we want more simply
print("Output 2:")
for record in data:
    print(f'Name: {record["name"]}, Phone: {record["phone-number"]}')

# If we want to, we can even transform the data
for record in data:
    name_split = record["name"].split(" ")
    phone_split = record["phone-number"].split('-')
    print(f'Name: {name_split[1]}, {name_split[0]}; Area Code: {phone_split[0]}')
