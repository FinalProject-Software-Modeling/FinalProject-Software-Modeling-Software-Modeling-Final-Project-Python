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

from transactions import Transaction

class Wallet:
    def __init__(self, wallet_id: str, owner_id: str, balance: float, movements: dict):
        self._wallet_id = wallet_id
        self._owner_id = owner_id
        self._balance = balance
        self._movements = movements

    def add_founds(self, walletorigen_id:str, amount: float):
        current_balance = self._balance
        new_balance = current_balance + amount
        self._balance = new_balance
        transaction = Transaction(Transaction.transaction_reference(walletorigen_id), walletorigen_id, amount, "2021-10-10", "add")
        Transaction.add_transaction_to_movements(transaction)
        return print(f"{transaction}")

    def outflow_founds(self, origen_id: str, destination_id:str, amount: float):
        current_balance = self._balance
        if amount > current_balance:
            return print("Insufficient funds")
        else:
            new_balance = current_balance - amount

        self._balance = new_balance
        transaction = Transaction(Transaction.transaction_reference(origen_id), origen_id, amount, "2021-10-10", "outflow")
        Transaction.add_transaction_to_movements(transaction)
        return print(f"{transaction}")

    def send_founds(self, origen_id: str, destination_id:str, amount: float):
        pass
    
    def request_founds(self, origen_id: str, destination_id:str, amount: float):
        pass

    def show_movements(self, wallet_id: str):
        pass

    def add_credit_card(self, wallet_id: str):
        pass