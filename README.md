# Wishlist
[![Build Status](https://travis-ci.org/andela-jmuli/wishlist.svg?branch=api-endpoints)](https://travis-ci.org/andela-jmuli/wishlist)
[![Code Health](https://landscape.io/github/andela-jmuli/wishlist/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-jmuli/wishlist/develop)


## Introduction:
Wishlist is a Django powered bucketlist application that allows creating and editing of bucket lists -- These are a number of experiences or achievements that a person hopes to have or accomplish during their lifetime.  
A quick demo can be viewed [here](https://youtu.be/Lida5BWogj4)

## Installation and Setup:


* Clone the repository:
 * Using SSH:  
    ``` git@github.com:andela-jmuli/wishlist.git ```

 * Using HTTP  
    ``` https://github.com/andela-jmuli/wishlist.git ```
* Setup a virtualenvironment for dependencies:
    * virtualenv {{ desired name }}
    * Activate your environment
* ``` cd ``` into environment folder and run ``` source bin/activate ``` to activate the virtual environment

* ```cd ``` back to the project root

* Install the dependencies:
    * ``` pip install -r reqiuirements.txt ```


* Setup the database tables and migrations:  

    * python manage.py makemigrations
    * python manage.py migrate

* NOTE: if you do not have Postgres installed follow [this](https://github.com/josephmuli/Django-Notes/blob/master/Postgress-Nginx-Gunicorn-Django.md) tutorial

* Run the server via:
    * python manage.py runserver




## Scope:  
 

| Endpoint        | Purpose           | Requires Authentication |
| ------------- |:-------------:| -------------:|
| POST auth/login    | Log a user in | False |
| POST auth/register     | Register a new user | False |
| POST /bucketlists/ | Create a new bucketlist   | True |
| GET /bucketlists/      | List all created bucketlists | True |
| GET /bucketlists/id     | get single bucketlist | True |
| PUT /bucketlists/id | update single bucketlist | True |
| DELETE bucketlists/id      | Delete a single bucketlist | True |
| POST bucketlists/id/items/      | Create a new item in a bucketlist | True |
| PUT bucketlists/id/items/item_id | Update an item in a bucketlist | True |
| DELETE bucketlists/id/items/item_id      | Delete an item in a bucketlist | True |

## Usage:
**Registering a new user:**  
Ensure the URL points to **https://secret-ridge-68835.herokuapp.com/api/v1/auth/register/** as a POST request:  
This is a parameterized request thus you need to provide a name and password

![Alt text](./source/register.png?raw=true "Optional Title") .

**Authenticating a user (Login)**
Ensure the URL points to **https://secret-ridge-68835.herokuapp.com/api/v1/auth/login/** as a POST request:  
This is a parameterized request thus you need to provide a name and password

![Alt text](./source/login.png?raw=true "Optional Title")

**Creating a Bucketlist:**
Ensure the URL points to **https://secret-ridge-68835.herokuapp.com/api/v1/bucketlists/** as a POST request.
This is a parameterized request thus you need to provide a name and optionally description
This is also a secure request thus make sure you include the token as a header during this request as below:  
The key should be Authorization and the value should be prefixed with Token then [token]: i.e.  
``` Authorization : Token sdvbjsdvnskdvna;scma;scma;cfskvbjrv ```  



**Listing all bucketlists:**  
Ensure the URL points to **https://secret-ridge-68835.herokuapp.com/api/v1/bucketlists/** as a GET request.  
This is also a secure request thus make sure you include the token as a header during this request.  

![Alt text](./source/get_bucketlists.png?raw=true "Optional Title")

**Creating a bucketlist item:**  
Ensure the URL points to **https://secret-ridge-68835.herokuapp.com/api/v1/bucketlists/bucketlist_id/items** as a POST request.
You have to ensure you have a bucketlist in order to create an item in it.
This is also a parameterized request thus you need to provide an item name and optionally description
This is also a secure request thus make sure you include the token as a header during this request.

![Alt text](./source/create_items.png?raw=true "Optional Title")



## Testing:  
 To test, run:  
     ``` python manage.py test ```

## Licence:
Check out the License file for more information

## Credits:
* [Joseph Muli](github.com/andela-jmuli)