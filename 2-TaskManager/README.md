# Hyperion Capstone 2 TaskManager

A simple command line based task manager that I was tasked to refactor and expand upon. Users can create tasks with given deadlines, descriptions, and assign users. There is an admin user that is able to generate general statistics about the tasks on the system as well as write automatic reports about the tasks.

The original task manager is `task_manager.py`. The refactored and expanded manager is `task_manager_modified.py`.

## Usage

When first running this program using:

```sh
python task_manager_modified.py
```

There will be no users on the system. This means that the program will first initialise an admin account with the username `admin` and a password `password`. A user is only given admin permissions if the username is `admin`.

This user and future users are stored in a `user.txt` file. The users will be in the format:

```txt
username1;password1
username2;password2
username2;password3
...
```

If needed, this is where user passwords can be changed. However, there is a feature to register new users.

Once the program is running and have logged in using the generated admin account you will be shown a menu:

```sh
Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    :
```

To select an option, simply enter the abbreviation given in the menu.

### r - Registering user

When registering a user, you need to be on an admin account. If not, you will be given a warning and taken back to the main menu.

If the user is an admin, you will be asked to give a username and password for the new user. Note that the username or password cannot have the `;` character. If user is valid, the user is added to `user.txt`.

### a - Adding a task

Admin and non-admin users can add tasks to any other user in the system. Once the user who is meant to complete the test is given, a task title, description, and due date is also given:

```console
Please assign the task to a user
Username: test-user
Title of Task: example task
Description of Task: This is an example task
Due date of task (YYYY-MM-DD): 2023-02-10
Task successfully added.
```

This task is then added to a file named `tasks.txt`, which is first generated when the program is initially run.

### va - View all tasks

This is a feature that just prints out a list of all the tasks on the system along with the information about the task. When a task is printed into the terminal it follows this format:

```console
-----------------------------------
Task:            example task
Assigned to:     test-user
Date Assigned:   2023-01-10
Due Date:        2023-02-10
Task Description:
 This is an example task

-----------------------------------
```

### vm - View my tasks

This feature is very similar to `va` however, this will only list the tasks that have been assigned to the user that logged in to begin with.

### gr - Generate reports

This is a feature only available to the admin user. The purpose of this feature is to generate two file containing information on the users (`user_overview.txt`) in the system and the tasks (`task_overview.txt`) in the system.

`user_overview.txt` will show statistics for each user, such as the number of tasks assigned to them; the number of completed tasks; the number of uncompleted tasks, and the number of overdue tasks. This is given in the format:

```txt
Test-user: INFORMATION=======================
Tasks_____________1/12    (8.33%)
Completed_________0/1     (0.0%)
Incompleted_______1/1     (100.0%)
Overdue___________0/1     (0.0%)
```

`task_overview.txt` given the statistics about the tasks in the system, such as; the total number of tasks; the number of completed and uncompleted tasks, and the number of overdue tasks. This is given in a similar format:

```txt
TASK OVERVIEW REPORT==================
Total tasks-----------12
Completed tasks-------2/12
Incompleted tasks-----10/12   (83.33%)
Overdue tasks---------6/10    (50.0%)
```

### ds - Display Statistics

This is a feature that will simply print the reports generated using `gr` to the terminal for easier viewing. It will follow the same format as the `txt` files.
