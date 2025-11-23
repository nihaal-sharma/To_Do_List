# To_Do_List

#Overview of the Project

This is a minimalist, command-line To-Do List application built using core Python. It allows a user to manage a simple list of tasks stored in memory for the duration of the program's execution. Tasks are not saved permanently when the program quits. It serves as a practical, entry-level demonstration of fundamental Python concepts: functions, lists, basic loops, and user input handling.

# Features

The application provides the following core functions:

  * View Tasks (1): Displays all current tasks in the list.
  * Add Tasks (2): Prompts the user for the number of tasks they wish to add, then collects and appends them to the list.
  * Remove Task (3): Allows the user to delete a task by entering its numerical position in the list.
  * Quit (4): Exits the program.

# Technologies/Tools Used

  * Technology: Python 3.x
  * Tool: Any standard Terminal/Command Prompt (e.g., cmd, PowerShell, Bash, etc.)
  * Data Structure: Python List (`to_do_list`)

#Steps to Install & Run the Project

#Prerequisites

  * Ensure Python 3 is installed on your system. You can check by typing `python --version` or `python3 --version` in your terminal.

#Installation & Execution

1.  Save the Code: Copy the entire provided Python code into a text file and save it with a `.py` extension (e.g., `todo_app.py`).
2.  Open Terminal: Navigate to the directory where you saved the file using your terminal.
3.  Run the Script: Execute the file using the Python interpreter:
    ```bash
    python todo_app.py
    # OR
    python3 todo_app.py 
    ```
4.  The application will start, and the main menu will appear, prompting for input.

#Instructions for Testing

To confirm the application works correctly, follow these practical test steps:

| Test Case | Steps | Expected Outcome |
| :--- | :--- | :--- |
|Add Tasks| 1. Choose option 2. 2. Enter 2 tasks (e.g., "Buy milk", "Fix bug"). | Both "Buy milk" and "Fix bug" are added. The success message "task added sucessfully" is printed twice. |
|View Tasks| 1. Choose option 1. (After adding tasks). | A list containing all added tasks ("Buy milk", "Fix bug") is displayed. |
|Remove Task| 1. Choose option 3. 2. Enter the task number 1 (to remove "Buy milk"). | "Buy milk" is removed from the list. The message "task removed sucessfully" is printed. |
|Invalid Input| 1. Enter any number/character not listed (e.g., 5 or A). | The message `'enter a valid input'` is printed. The main menu reappears. |
|Quit| 1. Choose option 4. | The program loop terminates, and you return to the terminal prompt. |

-----

#Screenshots (Simulated Console Output)

#Initial Run & Adding Tasks

```
welcome to your to do list what do you want to do  
1 view your to do list  
2 add a new task  
3 remove a task  
4 quit
what do u want to do  2
how many task do you want to add
enter the number of task:  2
enter your task  Review Code
task added sucessfully  
enter your task  Send Email
task added sucessfully  
```

#Viewing and Removing a Task

```
welcome to your to do list what do you want to do  
... (menu options) ...
what do u want to do  1


Review Code


Send Email
welcome to your to do list what do you want to do  
... (menu options) ...
what do u want to do  3
enter the task number you want to remove:  1
task removed sucessfully  
```
