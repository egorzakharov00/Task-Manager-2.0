# Python program for a small business that can help it to manage tasks assigned to each member of the team

# import datetime and date from datetime package in order to work with task dates
# https://docs.python.org/3/library/datetime.html
from datetime import datetime, date
# import path from os package in order to check if path/text file exists
# https://www.guru99.com/python-check-if-file-exists.html
from os import path


# Function for displaying menu and executing choice by calling other methods
def menu(user_type):
    # Output menu and get choice depending on type of user
    if user_type == 'admin':
        choice = input("Please select one of the following options:\n"
                       "r - register user\n"
                       "a - add task\n"
                       "va - view all tasks\n"
                       "vm - view my tasks\n"
                       "gr - generate reports\n"
                       "ds - display statistics\n"
                       "e - exit\n")
    else:
        choice = input("Please select one of the following options:\n"
                       "a - add task\n"
                       "va - view all tasks\n"
                       "vm - view my tasks\n"
                       "e - exit\n")

    # if else chain to call other methods depending on choice (and username in some cases)
    if choice == 'r' and username == 'admin':
        reg_user()

    elif choice == 'a':
        add_task()

    elif choice == 'va':
        view_all()

    elif choice == 'vm':
        view_mine()

    elif choice == 'gr' and username == 'admin':
        gen_report()

    elif choice == 'ds' and username == 'admin':
        display_stats()

    elif choice == 'e':
        exit(0)
    # if invalid choice is entered show menu recursively until valid choice is entered
    else:
        menu(user_type)


# Function for registering user
def reg_user():
    # get new username
    new_user = input("Enter a new username:\n")
    # if new user exists loop until new user is entered
    while new_user in usernames:
        new_user = input("The username entered already exists, please enter a new username:\n")
    # get new password
    new_password = input("Enter a new password:\n")
    # ask to confirm password
    confirm_password = input("Confirm new password:\n")
    # if confirmed password is wrong loop until right password is entered
    while new_password != confirm_password:
        confirm_password = input("Invalid confirmation please confirm new password again:\n")
    # create result string to add to user_file
    result = "\n" + new_user + ", " + new_password
    # open text file and append result
    with open('user.txt', 'a') as user_file:
        user_file.write(result)


# Function for adding tasks
def add_task():
    # get user who task is assigned to
    task_user = input("Enter the username of the person the task is assigned to:\n")
    # if assigned user does not exist loop until existing user is entered
    while task_user not in usernames:
        task_user = input("The username entered does not exist please try again:\n")
    # get task title, task description and due date
    task_title = input("Enter the title of the task:\n")
    task_description = input("Enter a description of the task:\n")
    due_date = input("Enter the due date of the task:\n")
    # Store today's date in a variable and format in same way as dates in tasks text file
    # https://docs.python.org/3/library/datetime.html
    date_assigned = date.today().strftime('%d %b %Y')
    # create result string to add to tasks_file
    result = "\n" + task_user + ", " + task_title + ", " + task_description \
             + ", " + date_assigned + ", " + due_date + ", No"
    # open text file and append result
    with open('tasks.txt', 'a') as tasks_file:
        tasks_file.write(result)


# Function for viewing all tasks
def view_all():
    # loop over each element in tasks
    for task in tasks:
        # output task data accordingly
        print("Assigned to:         " + task[0])
        print("Task:                " + task[1])
        print("Task description:    " + task[2])
        print("Date assigned:       " + task[3])
        print("Due date:            " + task[4])
        print("Task complete:       " + task[5] + "\n")


# Function for viewing [signed in user's] tasks
def view_mine():
    # task counter for allocating task number
    count = 0
    # list storing index's of the signed in user's tasks
    targets = []
    # loop over each element in tasks
    for task in tasks:
        # check if task is assigned to signed in user
        if username == task[0]:
            # add index of task to targets
            targets.append(tasks.index(task))
            # increment count
            count += 1
            # output task and its number
            print("Task", count)
            # output task data accordingly
            print("Assigned to:         " + task[0])
            print("Task:                " + task[1])
            print("Task description:    " + task[2])
            print("Date assigned:       " + task[3])
            print("Due date:            " + task[4])
            print("Task complete:       " + task[5] + "\n")

    # if user has no tasks
    if count == 0:
        print("You have no tasks")

    # is user has tasks proceed to next step
    else:
        # get choice
        choice_vm = int(
            input("Enter task number to select a specific task or enter '-1' to return to the main menu:\n"))
        # display menu if input is -1
        if choice_vm == -1:
            menu(username)
        # proceed to edit task
        else:
            # store task index
            task_index = targets[choice_vm - 1]
            # get type of operation from user
            operation = int(input("Enter '1' to mark the task as complete\nEnter '2' to edit the task\n"))
            # get task status (yes/no)
            status = tasks[task_index][5]
            # mark task as complete
            if operation == 1:
                # change task status to yes
                tasks[task_index][5] = 'Yes'
            # edit task
            elif operation == 2:
                # check if task is complete and output relevant message
                if status == 'Yes':
                    print("Permission to edit denied as the task has already been completed.")
                # else proceed to edit task
                else:
                    # get edit choice type
                    edit_type = int(input("Enter '1' to edit the username of the person to whom the task is assigned\n"
                                          "Enter '2' to edit the due date of the task\n"))
                    # edit username
                    if edit_type == 1:
                        # output current username
                        print("Current username of the peron to whom the task is assigned to: " + tasks[task_index][0])
                        # get new username
                        new_username = input("Enter a new username to assign the task to:\n")
                        # loop to make sure username entered exists
                        while new_username not in usernames:
                            new_username = input("The username entered does not exist please try again:\n")
                        # change username
                        tasks[task_index][0] = new_username
                        print(tasks[task_index][0])
                    # edit due date
                    elif edit_type == 2:
                        # output current due date
                        print("Current due date of the task: " + tasks[task_index][4])
                        # get new due date
                        new_due_date = input("Enter the new due date of the task in the format '1 Jan 2000':\n")
                        # change due date
                        tasks[task_index][4] = new_due_date

            # open tasks text file for overwriting
            with open('tasks.txt', 'w') as tasks_file:
                # add each task to text file
                for task in tasks:
                    # joining task data and adding next line
                    string_task = ", ".join(task) + "\n"
                    # writing string task to text file
                    tasks_file.write(string_task)


# Function for generating report
def gen_report():
    # get number of tasks
    num_tasks = len(tasks)
    # set number of complete, incomplete and overdue tasks to zero and store in variable
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    # get today's date and store in a variable
    current_date = (datetime.today()).date()
    # loop over each task
    for task in tasks:
        # store due date in date format
        due_date = (datetime.strptime(task[4], '%d %b %Y')).date()
        # store task completion status (yes or no) in variable
        status = task[5]
        # if status is yes increment complete tasks
        if status == 'Yes':
            complete_tasks += 1
        # if status is no increment incomplete tasks
        elif status == 'No':
            incomplete_tasks += 1
        # is status is no and current date has passed due date increment overdue tasks
        if status == 'No' and (current_date > due_date):
            overdue_tasks += 1
    # get percent of incomplete tasks to 2 decimal places
    percent_incomplete = round((incomplete_tasks / num_tasks) * 100, 2)
    # get percent of overdue tasks to 2 decimal places
    percent_overdue = round((overdue_tasks / num_tasks) * 100, 2)
    # store result in variable
    tasks_result = "Total number of tasks that have been generated and tracked using task_manager.py: " \
                   + str(num_tasks) + "\nTotal number of completed tasks: " + str(complete_tasks) \
                   + "\nTotal number of uncompleted tasks: " + str(incomplete_tasks) \
                   + "\nTotal number of tasks that haven’t been completed and that are overdue: " + str(overdue_tasks) \
                   + "\nPercentage of tasks that are incomplete: " + str(percent_incomplete) + "%" \
                   + "\nPercentage of tasks that are overdue: " + str(percent_overdue) + "%"

    with open('task_overview.txt', 'w') as task_overview:
        # write result to text file
        task_overview.write(tasks_result)

    # get number of users and store in variable
    num_users = len(usernames)
    # create result variable and store string with number of users
    user_result = "Total number of users registered with task_manager.py: " + str(num_users) + \
                  "\nTotal number of tasks that have been generated and tracked using the task_manager.py: " \
                  + str(num_tasks) + "\n"
    # for every user
    for user in usernames:
        # create variables of tasks, complete, incomplete and overdue and set to zero
        user_tasks = 0
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0

        for task in tasks:
            # store due date in variable in specified format
            due_date = (datetime.strptime(task[4], '%d %b %Y')).date()
            # increment user tasks for user
            if task[0] == user:
                user_tasks += 1
            # increment user complete for user
            if task[0] == user and task[5] == 'Yes':
                user_complete += 1
            # increment user incomplete for user
            if task[0] == user and task[5] == 'No':
                user_incomplete += 1
            # increment user overdue for user
            if task[0] == user and task[5] == 'No' and current_date > due_date:
                user_overdue += 1
        # calculate and store percentage of tasks assigned to user
        task_percent = round((user_tasks / num_tasks) * 100, 2)
        # calculate and store percentage of completed tasks by user
        complete_percent = round((user_complete / user_tasks) * 100, 2)
        # calculate and store percentage of incomplete tasks by user
        incomplete_percent = round((user_incomplete / user_tasks) * 100, 2)
        # calculate and store percentage of incomplete tasks by user
        incomplete_overdue = round((user_overdue / user_tasks) * 100, 2)
        # add details to result
        user_result += "\n" + user + ":\n" \
                       + "\nTotal number of tasks assigned: " + str(user_tasks) \
                       + "\nPercentage of the total number of tasks assigned: " + str(task_percent) + "%" \
                       + "\nPercentage of the tasks assigned that have been completed: " \
                       + str(complete_percent) + "%" \
                       + "\nPercentage of the tasks assigned that must still be completed: " \
                       + str(incomplete_percent) + "%" \
                       + "\nPercentage of the tasks assigned that have not yet been completed and are overdue: " \
                       + str(incomplete_overdue) + "%\n"

        # open text file, write result and close
        with open('user_overview.txt', 'w') as user_overview:
            user_overview.write(user_result)


# Function for displaying statistics
def display_stats():
    # integer variable adding boolean variables from checking if text files exist using path.exists()
    files_exist = path.exists('user_overview.txt') + path.exists('task_overview.txt')
    # if both text files exist
    if files_exist == 2:
        # open user text file and print out every line in text file
        with open('user_overview.txt', 'r') as user_stats:
            for line in user_stats:
                if line != '\n':
                    print(line)
        # print separating line for ease of reading
        print("----------------------------------------------------------------------------------------------------\n")
        # open task text file and print out every line in text file
        with open('task_overview.txt', 'r') as task_stats:
            for line in task_stats:
                if line != '\n':
                    print(line)
    # if none, one or both text files don't exist
    else:
        # call method to generate report
        gen_report()
        # open user text file and print out every line in text file
        with open('user_overview.txt', 'r') as user_stats:
            for line in user_stats:
                if line != '\n':
                    print(line)
        # print separating line for ease of reading
        print("----------------------------------------------------------------------------------------------------\n")
        # open task text file and print out every line in text file
        with open('task_overview.txt', 'r') as task_stats:
            for line in task_stats:
                if line != '\n':
                    print(line)


# function for storing data is lists by passing through three lists (usernames, passwords and tasks) as parameters
def data_store(usernames_list, passwords_list, tasks_list):
    # open text file to read from
    with open("user.txt", "r") as user_file:
        # loop over each line in user_file
        for line in user_file:
            # create a temporary list with two elements being username and password
            temp = line.strip().split(", ")
            # add username and password to their according list
            usernames_list.append(temp[0])
            passwords_list.append(temp[1])
    # open text file to read from
    with open("tasks.txt", "r") as tasks_file:
        # loop over each line in tasks_file
        for line in tasks_file:
            # add task to tasks
            # 2 dimensional list with tasks in outer list and task details in inner list for each task
            tasks_list.append(line.strip().split(", "))


# function for logging in by passing through username as a parameter
def log_in(user_name):
    # check if username passed exists and if not loop until valid username is entered
    while user_name not in usernames:
        user_name = input("Invalid username please try again:\n")

    # set target for usernames password index
    target = usernames.index(user_name)

    # get password input from user
    password = input("Enter your password:\n")

    # if password is invalid loop until user enters a valid password
    while password != passwords[target]:
        password = input("Invalid password please try again:\n")


# get username input from user
username = input("Enter your username:\n")
# Create list for usernames
usernames = []
# Create list for passwords
passwords = []
# Create list for tasks
tasks = []
# call method to create and store data by passing through empty lists usernames, passwords and tasks as parameters
data_store(usernames, passwords, tasks)
# call log in method and pass through username as parameter
log_in(username)
# call menu method and pass through username as parameter
menu(username)
