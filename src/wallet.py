"""
TODO: improve the documentation of the module

This module has class definition for Wallet. 

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

from creditcard import Creditcard

class Wallet:
    def __init__(self, wallet_id: str, owner_id: str, balance: float, movements: dict):
        self.wallet_id = wallet_id
        self.owner_id = owner_id
        self.balance = balance
        self.movements = movements

    def add_founds(self, origen_id:str, amount: float):
        pass

    def outflow_founds(self, origen_id: str, destination_id:str, amount: float):
        pass

    def send_founds(self, origen_id: str, destination_id:str, amount: float):
        pass
    
    def request_founds(self, origen_id: str, destination_id:str, amount: float):
        pass

    def show_movements(self, wallet_id: str):
        pass

    def add_credit_card(self, wallet_id: str):
        pass