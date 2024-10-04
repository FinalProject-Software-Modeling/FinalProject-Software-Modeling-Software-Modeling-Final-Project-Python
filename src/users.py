"""
TODO: improve the documentation of the module

This module has class definition for User and Customer. 

Authors: 
    Cristian Santiago Lopez Cadena <crslopezc@udistrital.edu.co>
    Carlos Alberto Barriga Gamez <>

This file is part of Walle-et project.

Walle-et project. is free software: you can redistribute it and/or modify it under the terms of 
the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

Walle-et project. is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Walle-et project. 
If not, see <https://www.gnu.org/licenses/>. """

users = {"id": "Customer"}
class User:
    def __init__(self, id_type: str, id_: str, password: str, grants: dict):
        self._id_type = id_type
        self._id_ = id_
        self._password = password
        self.grants = grants

    def create_account(id_type: str, id_: str, password: str, grants: dict, firstname: str, lastname: str, email: str):
        customer = Customer(id_type, id_, password, grants, firstname, lastname, email)
        users[id_] = customer
        return print(f"Account created successfully")

    def login(username, password):
        i = 0
        while i != 2:
            for user in users:
                if user["id"] == username and user["Customer.password"] == password:
                    return print("Login successful"), username
                else: 
                    print("The username or password is not correct")
                    i += 1
            
class Customer(User):
    def __init__(
        self,
        id_type: str,
        owner_id: str,
        password: str,
        grants: dict,
        firstname: str,
        lastname: str,
        email: str,
    ):
        super().__init__(id_type, owner_id, password, grants)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def add_address(street: str, apartment: str, city: str, country: str, zipcode: str):
        
        address = Address(street, apartment, city, country, zipcode)
        return print(f"address added successfully")

class Address:
    def __init__(self, street: str, apartment: str, city: str, country: str, zipcode: str):
        self._street = street
        self._apartment = apartment
        self._city = city
        self._country = country
        self._zipcode = zipcode

    def __str__(self) -> str:
        return f"Street, P.O. box: {self._street},\n Apartment, suite, unit: {self._apartment},\n\s
         City: {self._city}, Country/Region: {self._country},\n Postal/Zip code: {self._zipcode}\n"