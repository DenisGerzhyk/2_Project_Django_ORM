# 2_Project_Django_ORM

This is a Django code that defines a model for tasks with attributes such as title, description, created_at, completed_at, and completed. It also includes a form for creating new tasks, which uses the Tasks model. The form includes fields for the title, description, and whether the task is completed.

The views defined in this code include an index view that handles the creation of new tasks and a display view that shows all completed tasks. The index view checks whether the form has been submitted via POST, and if it has, it validates the form and saves the new task. If the completed field is True, it sets the completed_at attribute to the current time. The view then redirects to the display view. If the form is not valid, or if the request method is not POST, the index view renders the index.html template with the form as context.

The display view retrieves all completed tasks from the Tasks model and renders them using the display.html template, with the completed_tasks as context.
