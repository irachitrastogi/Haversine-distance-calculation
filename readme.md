
# Assignment

We have some customer records in a text file (customers.txt) -- one customer per line, 
JSON lines formatted. We want to invite any customer within 100km of our Dublin office for 
some food and drinks on us. Write a program that will read the full list of customers and output t
he names and user ids of matching customers (within 100km), sorted by User ID (ascending).

## Run to starts one-time search execution from the source directory as:

### `$ python3 main.py`

## Haversine 

[Haversin Wiki](https://en.wikipedia.org/wiki/Haversine_formula)

Basically, It calculates the arc length of the great circle with the giving points in-fly.

<img width="251" alt="Screenshot 2019-11-22 at 7 50 10 PM" src="https://user-images.githubusercontent.com/22388218/87174070-4a257900-c2f4-11ea-8ae7-cb133785dda3.png">

## Testing

For testing
Unit tests should be run using `pytest`.


### Better data fetching

A major issues was getting pieces of information from records, from large documents! For creation use we may pick some stockpiling and getting figures by record keys.

