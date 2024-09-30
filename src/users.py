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

class User:
    def __init__(self, id_type: str, owner_id: str, password: str, grants: dict):
        self.id_type = id_type
        self.owner_id = owner_id
        self.password = password
        self.grants = grants

    def create_account():
        pass

    def login():
        pass


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
        documentpicture: str,
    ):
        super().__init__(id_type, owner_id, password, grants)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.documentpicture = documentpicture

    def add_address():
        pass
