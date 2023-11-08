[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ES38PpdW)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12793451&assignment_repo_type=AssignmentRepo)
# Class Polymorphism

## Task
Create 3 classes:
* **OK**: Represents OK code error 200.
* **NotFound**: Represents Not Found code error 404.
* **ServerError**: Represents Server Error code 500.

- [ ] In each of the class, add attributes for the error code and the error message.


- [ ] Create a function **status(error_object)** That displays the error code and the error message of an object of any of the three classes above.


-[ ] Write a **main.py** to test your code: Create an object of each class, and run the function **status(error_object)** on them.


> The idea of this exercise is to see polymorphism in action:
> 
> The function **status(error_object)** changes its behaviour depending on the type (class) of the object it runs on.