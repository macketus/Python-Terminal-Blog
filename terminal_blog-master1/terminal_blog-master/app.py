from database import Database
from menu import Menu

__author__ = 'Ian Tetteh'

Database.initialize()

menu = Menu()

menu.run_menu()