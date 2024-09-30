"""
TODO: improve the documentation of the module

This module contains the Transaction class.

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

class Transaction:
    def __init__(
        self, id_reference: str, wallet_id: str, amount: float, date: str, were: str
    ):
        self.id_reference = id_reference
        self.wallet_id = wallet_id
        self.amount = amount
        self.date = date
        self.were = were

    @staticmethod
    def add_transaction_to_movements():
        pass
