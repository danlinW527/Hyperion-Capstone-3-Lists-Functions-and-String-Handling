# Shoe Inventory Management System

This is a simple Python-based inventory management system that allows you to add, search, and manage a list of shoes. The program is written with Python 3.0+ and does not require any additional libraries to run.

## Usage

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the program: `python inventory.py`.
4. Once the program is running, follow the prompts to add, search, and manage shoes in your inventory.

## Functionality

The program includes the following functionality:

- Add shoes to the inventory
- View a list of all shoes in the inventory
- Search for a specific shoe by its product code
- Search  a shoes with the lowest or highest quantity and update the quantity
- Calculate the total value of each shoe in the inventory based on cost and quantity

## Code structure

The main code for the program is contained in the `inventory.py` file. The `Shoe` class defines the properties and methods for each shoe object, including the ability to get the cost and quantity of an object, print out all the elements of an object, and create an object with each element. The program reads data from a text file `inventory.txt` and writes data to the same file.

The `read_shoes_data()` function reads all the data from the text file and converts it into a list of `Shoe` objects. The `update_file()` function rewrites the text file with the updated data. The `capture_shoes()` function allows users to add a new shoe object to the list and write it to the text file. The `view_all()` function displays all the shoe objects in the list. The `re_stock()` function finds the shoe with the lowest quantity and allows users to add more shoes to it. The `seach_shoe(item_c)` function searches for a specific shoe by its product code. The `value_per_item()` function calculates the total value of each shoe in the inventory based on cost and quantity.