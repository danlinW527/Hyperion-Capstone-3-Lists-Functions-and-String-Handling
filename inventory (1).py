#========The beginning of the class==========
class Shoe:

#initialis the parameter of the class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#use class to get cost of each object
    def get_cost(self):
        for shoe in shoe_list:
            return shoe.cost

#use class to get the quantity of each object
    def get_quantity(self):
        for shoe in shoe_list:
            return shoe.quantity

#create an object with each elements
    def to_file(self):
        return f'{self.country },{self.code},{self.product},{self.cost},{self.quantity}'

#print out all the elements of an object
    def __str__(self):
        return f'''────────────────────────────────────────
Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}
────────────────────────────────────────
'''

#==========Functions outside the class==============

#This function read all the data from the text file. It's to make the rest of the functions and coding easy
def read_shoes_data():

    try:
        #open the text file in read mode
        with open('inventory.txt', 'r') as inventory_read:
            #skip the first line of the text file
            inventory_read.readline()

            #use for loop to start reading data from the 2nd line of the text file
            for line in inventory_read:
                #define the name for each element
                conty, cod, produ, cos, quant = line.strip('\n').split(',')

                #use Shoe clas to create new object
                info = Shoe(conty, cod, produ, float(cos), int(quant))

                #add the object to the list.
                shoe_list.append(info)
    except FileNotFoundError:
        print('The file that you are trying to open does not exist.')

def update_file():
    #rewrite the file
    with open('inventory.txt', 'w') as file_update:
        #write the headline of the product
        file_update.write('Country,Code,Product,Cost,Quantity')

        #add all the info of the list into the file
        for shoe in shoe_list:
            file_update.write(f'\n {shoe.to_file()}')

def capture_shoes():

    #ask the user to input new information of each elements of the object
    country = input('Enter the product country: ')
    code = input('Enter the product code: ')
    name = input('Enter the product name: ')
    cost = float(input('Enter the product cost: '))
    quantity = int(input('Enter the quantity of the product: '))

    #use class to create a new shoe object
    new_shoe = Shoe(country,code,name,cost,quantity)
    #add the new shoe to the list
    shoe_list.append(new_shoe)

    #use the update function to add all the information to the file
    update_file()
    print(f'The product {name} has been successfully added to the list.')


#use for loop and the function in the class to print out each object
def view_all():

    for obj in shoe_list:
        print(obj)

def re_stock():

#use the key = lambda and min function to find the lowest quantity amoung the list
    min_quantity_shoe = min(shoe_list, key=lambda shoe:shoe.quantity)

#use the index function to find out the index of the objec tin the shoe_list list
    min_quantity_index = shoe_list.index(min_quantity_shoe)

#use class to identify the object's quantity
    min_quantity = min_quantity_shoe.quantity

    # ask the user if they want to add more shoes
    response = input(
        f"The shoe with SKU {min_quantity_shoe.code} has the lowest quantity of {min_quantity}. Do you want to add more shoes? (y/n)")

    if response.lower() == 'y':
        # update the quantity and write back to the file
        add_quantity = int(input("How many shoes do you want to add? "))

        #new quantity is equal to previous quantity plus added quantity
        updated_quantity = min_quantity + add_quantity

        #update the quantity number in the list
        shoe_list[min_quantity_index].quantity = updated_quantity

        #update the information from the list to the file
        update_file()
        print('Quantity updated.')

    #if the answer is no, exit the programme
    if response.lower() == 'n':
        print('Goodbye')
        exit()

#define the search function with object's code
def seach_shoe(item_c):


    shoe_pos = -1

#use enumerate to find the index and object in the list
    for index, obj in enumerate(shoe_list):
        #if the ojb's code is equal to user's input
        if obj.code == item_c:

            #shoe's position is equal to the index
            shoe_pos = index

    if shoe_pos == -1:
        print(f'The {item_c} can not be found.')
    else:
        print('Below is the product information:')
        print(shoe_list[shoe_pos])


def value_per_item():

#use the class to find the cost and the quantity of each object
    for obj in shoe_list:

#value = cost * quantity
        value =obj.cost * obj.quantity
        print(f'{obj.product} value is {value}\n')

def highest_qty():

#sort the list by quantity, reverse = True means the sorted list starts from the hightest number
    sorted_shoes = sorted(shoe_list, key=lambda shoes:shoes.quantity, reverse = True)
    print(f'''The shoe with the highest quantity, which will be put for sale is:
{sorted_shoes[0]}''')

#The list will be used to store a list of objects of shoes.
shoe_list = []

#read all the shoe data from the file so that all the below functions can work.
read_shoes_data()

#==========Main Menu=============
while True:
    menu = input(f'''\nSelect one of the following options below:
capture - add new shoe data into the inventory
view - view all the data from the inventory file
restock - find the shoes with the lowest quantity. You will have the option to add more quantity
search - search a shoes from the list by using a code
value - display the total value of each shoe
highest - search the shoe with highest quantity for sale 
exit - exit the menu

''')
#use if, elif and else to display the results of all the functions.
    if menu.lower() == 'capture':
        capture_shoes()

    elif menu.lower() == 'view':
        view_all()

    elif menu.lower() == 'restock':
        re_stock()

    elif menu.lower() == 'search':
        seach_shoe(input('Enter the code: '))

    elif menu.lower() == 'value':
        value_per_item()

    elif menu.lower() == 'highest':
        highest_qty()

#if user choose 'exit', leave the programme
    elif menu.lower() =='exit':
        print('Goodbye.')
        exit()
#if the entru is invalid, back to the menu.
    else:
        print('Invalid entry, try again.')
