#!/usr/bin/env python3
# ------------------------------------------------------------------------------#
# Author: Rachit Rastogi <rrastogi@tcd.ie>
# ------------------------------------------------------------------------------

import json
import dist

# Location of Dublin Office
lat_office = 53.339428
long_office = -6.257664

# Library containing the calculation for ascertaining the separation between two 
# areas on the world's surface indicated by scope and longitude.
def customer_list(file_path):
    customers_list = []
    with open(file_path) as data:
        for line in data:
            customers_list.append(json.loads(line))
    return customers_list


# Printing the Id along with the name of the customers after the search
def print_list(customers_list):
    print(' -----   ------')
    print('   ID  |  NAME ')
    print(' -----   ------')
    for client in customers_list:
        print('%4s  |  %s' % (client['user_id'], client['name']))


def main():
    office_pos = dist.Location(lat_office, long_office)
    local_customers = []

    for client in customer_list('data.json'):
        lati = float(client['latitude'])
        longi = float(client['longitude'])
        customer_pos = dist.Location(lati, longi)
        if dist.distance_cal(office_pos, customer_pos) <= 100:
            local_customers.append(client)

    local_customers.sort(key=lambda c: c['user_id'])
    print_list(local_customers)


if __name__ == '__main__':
    main()
