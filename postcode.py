"""
<   This code postcode.py is to be used for learning purposes only and 
     should not be used a tool for any commercial purpose.

    All rights reserved ® 2018  David Craven

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Allows HTTP requests to be sent
import requests

# Function get details - GET /postcodes/{POSTCODE}
def get_details(postcode):
    # Return true if everything is ok, return false if an error occurred 
    try:
        # Create the url for this function
        postcode_url=main_api+postcode
        # Get the response from the URL
        json_data = requests.get(postcode_url).json()
        # Check the status of request
        if(json_data['status'] is 200):
            # Get the country and the region
            print("Country: %s, Region: %s." % (json_data['result']['country']
                                              ,json_data['result']['admin_district']))
            return True
        else:
            # If we don't have status 200, something went wrong
            raise ValueError('No response from the endpoint.')
    except Exception as e:
        print(e)

        
# Function validate - GET /postcodes/{POSTCODE}/validate
def validate(postcode):
    # Return true if valid, return false if invalid or if an error has occurred
    try:
        # Create the url for this function
        validate_url=main_api+postcode+'/validate'
        # Get the response from the URL
        json_data = requests.get(validate_url).json()
         # Check the status of request
        if(json_data['status'] is 200):
            # Check if the postcode exists
            if (json_data['result'] is False):
                # Raise the error if the postcode does not exist
                raise ValueError('The postcode %s is not valid.' % postcode)
            else:
                return True
        else: 
            # If we don't have status 200, something went wrong
            raise ValueError('No response from the endpoint.')
    except Exception as e:
        print(e)
        return False


# Function get nearest - GET /postcodes/{POSTCODE}/nearest
def get_nearest(postcode):
    # Return true if everything is ok, return false if an error occurred
    try:
        # Create the url for this function
        nearest_url=main_api+postcode+'/nearest'
         # Get the response from the URL
        json_data = requests.get(nearest_url).json()
          # Check the status of request
        if(json_data['status'] is 200):
            # Iterate over the list of results
            print("Nearest postcodes:")
            for val in json_data['result']:
                print("\tPostcode: %s, Country: %s, Region: %s." % (val['postcode']
                                                                   ,val['country']
                                                                   ,val['region']))
            return True
        else:
            # If we don't have status 200, something went wrong
            raise ValueError('No response from the endpoint.')
    except Exception as e:
        print(e)   
        return False


#### Main code ###
    
while True:
# Main URL to query
    main_api = 'https://api.postcodes.io/postcodes/';

# Prompt for user to enter a postcode 
    postcode = input('Enter Postcode: ')

# Step 1 : Validate the postcode    
    if(validate(postcode)):
    
    # Step 2 : Get the country and region  
        get_details(postcode)
    
    # Step 3 : Get the nearest postcodes
        get_nearest(postcode)
