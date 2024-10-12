# Import datetime library
import datetime

# Create a dictionary under variable 'users'
users = {}
with open('user.txt', 'r') as f: # Open file 'user.txt' to be read
    for line in f:
        # Split the lines in the file into the format 'username, password'
        username, password = line.strip().split(', ')
        users[username] = password # Add to dictionary in order to be searched

# Create a while loop for login 
while True:
    # Ask user to input username and password 
    username_input = input('\nEnter your username: ')
    password_input = input('Enter your password: ')

    # Search dictionary to ensure that username and password are valid
    if username_input in users and users[username_input] == password_input:
        print('Login successful')
        break
    else:
        print('Invalid username or password, try again')

while True:
    # Present the menu to the user  
    # make sure that the user input is converted to lower case.
    if username_input == 'admin':
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''\nSelect one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    
    if menu == 'r' and username_input == 'admin':
        # Ask user to input new username, password and confirm password
        new_username = input('Enter a new username: ')
        new_password = input('Enter a new password: ')
        confirm_password = input('Confirm new passowrd: ')

        # Use an if statement to check the password matches confirmed password
        if new_password == confirm_password:
            # Add new username and password to 'user.txt' file
            with open('user.txt', 'a') as f:
                f.write(f'{new_username}, {new_password}\n')
            users[new_username] = new_password # Add to users dictionary
            print('New user added')
        else:
            print('Passwords do not match, please try again')

            
    elif menu == 'a':
# Ask user to input required task information
        task_username = input('Enter username of the person this task is assigned to: ')
        task_title = input('Enter title of the task: ')
        task_description = input('Enter description of task: ')
        task_due = input('Enter date when the task is due: ')
        task_date = datetime.datetime.now().strftime('%Y-%m-%d')
        task_completed = 'No' # Set task completion to no 

# Add the information inputed to the 'tasks.txt' file
        with open('tasks.txt', 'a') as f:
            f.write(f'{task_username}, {task_title}, {task_description}, {task_due}, {task_date}, {task_completed}\n')
        print('Task has been added')

   
    elif menu == 'va':
        print('\nAll tasks:')
        # Open 'tasks.txt' file and print contents in required format' 
        with open('tasks.txt', 'r') as f:
            for line in f:
                # Split the line
                task_username, task_title, task_description, task_date, task_due, task_completed = line.strip().split(', ')
                print(f'''
Assigned to: {task_username}
Task title: {task_title}
Task description: {task_description}
Date assigned: {task_date}
Date due: {task_due}
Task completed: {task_completed}''')

   
    elif menu == 'vm':
        print('\nYour tasks:')
        with open('tasks.txt', 'r') as f:
            for line in f:
                task_username, task_title, task_description, task_date, task_due, task_completed = line.strip().split(', ')
                # Use an if statement to see if inputed username matches any usernames in the file
                if username_input == task_username:
                    print(f'''
Assigned to: {task_username}
Task title: {task_title}
Task description: {task_description}
Date assigned: {task_date}
Date due: {task_due}
Task completed: {task_completed}''')
                else:
                    print('No tasks found')


    elif menu == 'ds' and username_input == 'admin':
        # Open 'tasks.txt' and count number of lines in file
        with open('tasks.txt', 'r') as f:
            task_count = sum(1 for line in f)

        # Open 'user.txt' and count number of lines in file
        with open('user.txt', 'r') as f:
            users_count = sum(1 for line in f)

        print(f'''
Statistics:
Total number of tasks: {task_count}
Total number of users: {users_count}''')


    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have entered an invalid input. Please try again")
