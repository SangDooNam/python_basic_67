from server_errors import OK, NotFound, ServerError

# Write code to test your classes

errors = [OK().status(200), NotFound().status(404), ServerError().status(500)]


for error in errors:
    if error:
        print(error)