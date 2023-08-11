from mysql.connector import connect, errors


class RegisterUser:
    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.username = username
        self.db_connection = connect(
            host="localhost",
            user="root",
            password="root",
            database="login_register_python"
        )

    def register(self):
        try:
            with self.db_connection as connection:
                register = f"""
                INSERT INTO users (first_name, last_name, username, password, email)
                VALUES ({self.firstname},{self.lastname}, {self.username}, {self.password}, {self.email});"""
                with connection.cursor() as cursor:
                    cursor.execute(register)
                    connection.commit()
                    return "Success"
        except errors as e:
            return e


firstname = input("First Name: ")
lastname = input("Last Name: ")
username = input("UserName: ")
email = input("Email: ")
password = input("Password: ")

user_registration = RegisterUser(firstname, lastname, username, email, password)
user_registration.register()