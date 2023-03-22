#====Function Section====
def reg_user():
    #read the user file so that all the user info can be added to the user_list list
    with open('user.txt', 'r') as user_file_d:
        users = user_file_d.readlines()
        users = [user.strip() for user in users]
        user_list = []
        for user in users:
            user_data = user.split(', ')
            user_list.append(user_data[0])
        while True:
            nusername = input('Enter a new username: ')
            #error check the new user information to see if it's already exist in the user file
            if nusername in user_list:
                print(f'Error: {nusername} already exists. Please choose a different username.')
            else:
                break
        while True:
            npassword1 = input('Set up your password: ')
            npassword2 = input('Please confirm your password: ')
            if npassword1 != npassword2:
                print(f'Error: passwords do not match. Try again.')
            else:
                break
        #open the user file with append mode and add the new user info to the file
        with open('user.txt', 'a') as user_file_d:
            user_file_d.write(f'\n{nusername}, {npassword2}')
            print(f'{nusername} has been added successfully')

def add_task():
    assigned_d = input('Enter the username of the person whom the task is assigned to: ')
    title_d = input('Title of the task: ')
    description_d = input('Please describe the task: ')
    due_d = input('Enter the due date of the task, please use the format xx(date) Month xxxx(year): ')
    from datetime import datetime
    # Get current Date and cast it to the required format
    current_date_d = datetime.now().strftime("%d %b %Y")
    # open the tasks text file in a+ mode so that
    # the information user entered can be added to the tasks file
    with open('tasks.txt', 'a+') as task_file:
        task_file.write(f'\n{assigned_d}, {title_d}, {description_d}, {current_date_d}, {due_d}, No')
        print('New task has been added successfully.')

def view_all():
    with open('tasks.txt', 'r') as tasks_read:
        data = tasks_read.readlines()
        for line in data:
            # split the data in each line
            split_data = line.split(', ')
            # create variable 'output' which store all the info and print them in one go#
            output = f'─────────────────────────────\n'
            output += '\n'
            # locate the data in the split_data list and assign it to it's category
            output += f'Task:\t\t\t\t{split_data[1]}\n'
            output += f'Assigned to: \t\t{split_data[0]}\n'
            output += f'Date assigned: \t\t{split_data[3]}\n'
            output += f'Due date:\t\t\t{split_data[4]}\n'
            output += f'Task complete?:\t\t{split_data[5]}'
            output += f'Task description:\t{split_data[2]}\n'
            output += '\n'
            output += f'─────────────────────────────\n'
            print(output)

def view_mine():
    tasks_read = open('tasks.txt', 'r')
    data = tasks_read.readlines()
    for pos, line in enumerate(data, 1):
        split_data = line.split(', ')
        # match the entered username with the 0 position in the splited data in the tasks file
        if username == split_data[0]:
            output = f'─────────────[{pos}]────────────────\n'
            output += '\n'
            output += f'Task:\t\t\t\t{split_data[1]}\n'
            output += f'Assigned to:\t\t{split_data[0]}\n'
            output += f'Date assigned:\t\t{split_data[3]}\n'
            output += f'Due date:\t\t\t{split_data[4]}\n'
            output += f'Task complete?:\t\t{split_data[5]}'
            output += f'Task description:\t{split_data[2]}\n'
            output += '\n'
            output += f'─────────────────────────────\n'
            print(output)
    while True:
        choice = int(input('Please select a task number(enter -1 to return to the main menu): ')) - 1
        #error checking in case user entered incorrect info
        if choice < -2 or choice > len(data) or choice == -1:
            print('You have selected an invalid option, try again.')
            continue
        #if user enter -1, choice = -2, return the user to the main menu
        elif choice == -2:
            print('Back to the main menu')
            break
        else:
            edit_data = data[choice]
            while True:
                output = f'──────────[Select an option]────────────────────────\n'
                output += '1- Edit due date \n'
                output += '2 - Mark task as completed \n'
                output += '────────────────────────────────────────────────────\n'
                # error checking in case user entered incorrect info
                option = int(input(output))
                if option <= 0 or option >= 3:
                    print('You have selected an invalid option, try again.')
                    continue
                elif option == 1:
                    split_data = edit_data.split(', ')
                    new_due = input('Enter a new due date, please use the format xx(date) Month xxxx(year): ')
                    import datetime
                    # cast the new due date into the required format
                    new_due_f = datetime.datetime.strptime(new_due, "%d %b %Y")
                    #cast the due date to a string so that it can be added to the list
                    new_due_f = new_due_f.strftime("%d %b %Y")
                    split_data[-2] = new_due_f
                    new_data = ', '.join(split_data)
                    data[choice] = new_data
                #locate the task status is in index -1, change it to 'yes'
                elif option == 2:
                    split_data = edit_data.split(', ')
                    split_data[-1] = 'Yes\n'
                    #cast the edited list back to a string and update it in the file
                    new_data = ', '.join(split_data)
                    data[choice] = new_data
                tasks_read.close()
                task_write = open('tasks.txt', 'w')
                for line in data:
                    task_write.write(line)
                task_write.close()
                break

def gen_report():
    #below code is to update the task_overview text file
    from datetime import datetime
    taskoverview_write = open('task_overview.txt', 'w')
    #open the task file in read mode and read each line
    tasks_read = open('tasks.txt', 'r')
    data = tasks_read.readlines()
    # The number of tasks is equal to the number of lines in tasks file
    task_number = len(data)
    output = f'The total number of the tasks is {task_number}.\n'
    #create empty lists for counting completed, uncompleted and overdue tasks
    completed_count = 0
    uncompleted_count = 0
    overdue_count = 0
    for line in data:
        split_data = line.strip().split(', ')
        due_date = datetime.strptime(split_data[-2], '%d %b %Y') # covert string to datetime object
        if split_data[-1] == 'No':
            uncompleted_count += 1
        else:
            completed_count += 1

        if split_data[-1] == 'No' and due_date < datetime.today():
            overdue_count += 1
    #workout the different percentages as requested.
    output += f'The total number of completed tasks is {completed_count}.\n'
    output += f'The total number of uncompleted tasks is {uncompleted_count}.\n'
    output += f'The total number of uncompleted task and are overdue is {overdue_count}.\n'
    output += f'The percentage of tasks that are incomplete is {uncompleted_count/(uncompleted_count + completed_count)*100}%.\n'
    output += f'The percentage of tasks that are ovedue is {overdue_count/(uncompleted_count + completed_count)*100}%.'
    taskoverview_write.write(f'{output}')

    taskoverview_write.close()
    tasks_read.close()

#below code is to update user_overview text file
    useroverview_write = open('user_overview.txt', 'w')
    user_file_d = open('user.txt', 'r')
    users = user_file_d.readlines()
    users_num = len(users) #the number of lines in the user file is equal to the number of users
    useroverview_write.write(f'The total number of users is {users_num}.\n')
    useroverview_write.write(f'The total number of the tasks is {task_number}.\n')

    import datetime
    # Create a dictionary to store the usernames from the users.txt file
    users = {}
    with open('user.txt', 'r') as user_file_d:
        for line in user_file_d:
            parts = line.strip().split(',')
            username = parts[0].strip()
            #add all users to the dictionary, the key is the username and value is true
            users[username] = True
    #use dictionary comprehension to go through keys in users dictionary and use it as it's own key
    # set 0 value for total, completed and overdue so that it can be incremented later
    tasks = {username: {'total': 0, 'completed': 0, 'overdue': 0} for username in users.keys()}
    # read the tasks file
    with open('tasks.txt', 'r') as tasks_read:
        for line in tasks_read:
            # split the line into parts
            parts = line.strip().split(',')
            # get the username and task details
            username = parts[0].strip()
            task_status = parts[-1].strip()
            end_date = parts[4].strip()
            if username in users:
                # increment the total tasks for the user
                tasks[username]['total'] += 1
                # check if the task is completed
                if task_status == 'Yes':
                    tasks[username]['completed'] += 1
                # check if the task is overdue
                if end_date < str(datetime.date.today()):
                    tasks[username]['overdue'] += 1

    # create the overview file
    with open('user_overview.txt', 'w') as userov_w:
        for user, data in tasks.items():
            # calculate the percentages and required data
            total_tasks = data['total']
            total_percent = total_tasks / task_number * 100
            completed_tasks = data['completed']
            overdue_tasks = data['overdue']
            completed_percent = (completed_tasks / total_tasks) * 100 if total_tasks != 0 else 0
            overdue_percent = (overdue_tasks / total_tasks) * 100 if total_tasks != 0 else 0
            still_needed_percent = 100 - completed_percent - overdue_percent
            # write the overview to the file
            userov_w.write(f'Username: {user}\n'
            f'Total tasks: {total_tasks}%\n'
            f'The percentage of the tasks have been assigned to {user} is {total_percent}%\n'
            f'Completed tasks: {completed_tasks} ({completed_percent:.2f}%)\n'
            f'Overdue tasks: {overdue_tasks} ({overdue_percent:.2f}%)\n'
            f'Still needed complete tasks: {still_needed_percent:.2f}%\n\n')

def display_sta():
    #the majority of the code in this function is similar to the one in gen_report()
    #the only difference is it prints out all the restuls rather than adding them to the text file as requested
    #I won't add as many comments as they are all highlighted in above function
    from datetime import datetime
    taskoverview_write = open('task_overview.txt', 'w')
    # open the task file in read mode and read each line
    tasks_read = open('tasks.txt', 'r')
    data = tasks_read.readlines()
    # The number of tasks is equal to the number of lines in tasks file
    task_number = len(data)
    completed_count = 0
    uncompleted_count = 0
    overdue_count = 0
    for line in data:
        split_data = line.strip().split(', ')
        due_date = datetime.strptime(split_data[-2], '%d %b %Y')  # covert string to datetime object
        if split_data[-1] == 'No':
            uncompleted_count += 1
        else:
            completed_count += 1

        if split_data[-1] == 'No' and due_date < datetime.today():
            overdue_count += 1
    tasks_read.close()
    print(
    f'The total number of the tasks is {task_number}\n'
    f'The total number of completed tasks is {completed_count}\n'
    f'The total number of uncompleted tasks is {uncompleted_count}\n'
    f'The total number of uncompleted task and are overdue is {overdue_count}\n'
    f'The percentage of tasks that are incomplete is {uncompleted_count / (uncompleted_count + completed_count) * 100}%\n'
    f'The percentage of tasks that are ovedue is {overdue_count / (uncompleted_count + completed_count) * 100}%')


    user_file_d = open('user.txt', 'r')
    users = user_file_d.readlines()
    users_num = len(users)
    print(f'The total number of users is {users_num}')

    import datetime
    # Create a dictionary to store the usernames from the users.txt file
    users = {}
    with open('user.txt', 'r') as user_file_d:
        for line in user_file_d:
            parts = line.strip().split(',')
            username = parts[0].strip()
            users[username] = True
    tasks = {username: {'total': 0, 'completed': 0, 'overdue': 0} for username in users.keys()}
    # read the tasks file
    with open('tasks.txt', 'r') as tasks_read:
        for line in tasks_read:
            # split the line into parts
            parts = line.strip().split(',')
            # get the username and task details
            username = parts[0].strip()
            task_status = parts[5].strip()
            start_date = parts[3].strip()
            end_date = parts[4].strip()
            if username in users:
                # increment the total tasks for the user
                tasks[username]['total'] += 1
                # check if the task is completed
                if task_status == 'Yes':
                    tasks[username]['completed'] += 1
                # check if the task is overdue
                if end_date < str(datetime.date.today()):
                    tasks[username]['overdue'] += 1

    # create the overview file
    with open('user_overview.txt', 'r') as userov_r:
        for user, data in tasks.items():
            # calculate the percentages
            total_tasks = data['total']
            total_percent = total_tasks / task_number * 100
            completed_tasks = data['completed']
            overdue_tasks = data['overdue']
            completed_percent = (completed_tasks / total_tasks) * 100 if total_tasks != 0 else 0
            overdue_percent = (overdue_tasks / total_tasks) * 100 if total_tasks != 0 else 0
            still_needed_percent = 100 - completed_percent - overdue_percent
            # write the overview to the file
            print(f'Username: {user}\n'
    f'Total tasks: {total_tasks}\n'
    f'The percentage of the tasks have been assigned to {user} is {total_percent}%\n'              
    f'Completed tasks: {completed_tasks} ({completed_percent:.2f}%)\n'
    f'Overdue tasks: {overdue_tasks} ({overdue_percent:.2f}%)\n'
    f'Still needed complete tasks: {still_needed_percent:.2f}%\n\n')
    tasks_read.close()
    user_file_d.close()
    userov_r.close()

#====Login Section====

#create empty lists to store user and password#
user_list = []
password_list = []
user_file = open('user.txt', 'r')
for line in user_file:
#after split data in each line, define the first one as user
#and the second one as password. Add each data to the relevant lists
    user, password = line.split(', ')
    user_list.append(user)
    password_list.append(password.strip("\n"))

username = input('Enter the username: ')
#if the username entered is not in the list, ask the user to re-enter the username#
while not username in user_list:
        print('Invalid username. ')
        username = input('Enter the username: ')
#define the position of the user in the list to help locate the same position in the password list#
position = user_list.index(username)
password = input('Enter the password: ')
#if the entered password isn't equal to the one in the list
#ask the user to re-enter the password. Alternatively login successfully
while password != password_list[position]:
    print('Invalid password.')
    password = input('Enter the password: ')
print(f'Welcome, {username}')
user_file.close()

#====Menu Section====
while True:
    if username == 'admin':

    #presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
s - view the total number of tasks and users
e - Exit
: ''').lower()

    if menu == 'r':

        reg_user()

    elif menu == 'a':

        #if user select 'a' for adding task, ask user to input below information.
        add_task()

    elif menu == 'va':
        view_all()


    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        gen_report()

    elif menu == 'e':
        print('Thank you for using the service, goodbye!!!')
        exit()
    elif menu == 'ds':
        display_sta()
    else:
        print("You entered an incorrect choice, please try again")
        continue


