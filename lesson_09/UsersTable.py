from sqlalchemy import create_engine, text

class UsersTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def add_new_user(self, my_params):
        with self.db.begin() as connection:
            sql_statement = text("INSERT INTO users (user_email, subject_id) VALUES (:user_email, :subject_id)")
            connection.execute(sql_statement, my_params)

    def get_all_users(self):
        with self.db.connect() as connection:
            result = connection.execute(text("SELECT * FROM users")).mappings().all()
            return result
    
    def get_user_by_id(self, id):
        with self.db.connect() as connection:
            sql_statement = text("select * from users where user_id = :user_id")
            result = connection.execute(sql_statement, id).mappings().all()
            return result

    def get_user_with_max_id(self):
        with self.db.connect() as connection:
            max_id = connection.execute(text("SELECT MAX(user_id) as user_id FROM users")).mappings().all()[0]["user_id"]
            return max_id

    def change_user_data(self, new_params):
        with self.db.begin() as connection:
            sql_statement = text("UPDATE users SET user_email = :user_email, subject_id = :subject_id WHERE user_id = :user_id")
            connection.execute(sql_statement, new_params)

    def delete_user_by_id(self, id):
        with self.db.begin() as connection:
            sql_statement = text("DELETE FROM users WHERE user_id = :user_id")
            connection.execute(sql_statement, id)