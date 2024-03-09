# Checklist Website Project

This project involves creating a basic checklist website that performs CRUD (Create, Read, Update, Delete) operations on an SQLite database. The website displays tasks sequentially and allows users to interact with them by checking them off or deleting them.

## Overview

The checklist website is designed to manage tasks using a simple interface. Users can view existing tasks, add new tasks, mark tasks as completed, and delete tasks as needed. The project uses SQLite as the database to store task information.

## Features

- View existing tasks in a sequential order.
- Add new tasks with or without specifying an ID.
- Mark tasks as completed by checking off a corresponding checkbox.
- Delete tasks individually using a delete button.
- Perform basic CRUD operations on the SQLite database.

## Implementation Details

- The main functionality is implemented in the `index.html` file, where tasks are fetched from the SQLite database and displayed using Jinja templating.
- Tasks are displayed sequentially with corresponding checkboxes and delete buttons.
- Users can add new tasks by entering task details in the provided text boxes. If the ID text box is left empty, the task is added with the next available ID.
- Task completion status is stored in the database and updated dynamically when checkboxes are toggled.
- Deleting a task removes it from the database permanently.
- The project uses CSS for styling to ensure a visually appealing user interface.

## Getting Started

### Running Locally

To run this project locally, follow these steps:

1. Clone the project repository to your local machine.
  ```bash
    git clone https://github.com/sarcoding/CheckBox.git
  ```
2. Navigate to the project directory.
3. Install the required dependencies
  ```bash
  pip install -r requirements.txt
  ```
4. Open the backend.py file
```bash
python backend.py
```

## Dependencies

- Flask (for server-side operations)
- SQLite (for database management)
- Jinja (for template rendering)

## Project Structure

- `index.html`: Main HTML file containing the checklist interface.
- `backend.py`: SQLite database setup and CRUD operations.
- `templates/`: Directory containing Jinja templates for rendering HTML content.
- `instance/` : Directory containing the database.
- `ToDo.db`   : Database storing table user_db
