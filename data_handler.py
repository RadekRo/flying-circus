import bcrypt, database

def check_password(user_data, password):
    hashed_user_password = bytes.fromhex(user_data['password'])
    return bcrypt.checkpw(password.encode(encoding="utf-8"), hashed_user_password)

def check_password_repeat(password, password_repeat):
    return password == password_repeat

def hash_password(user_input):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(user_input.encode(encoding="utf-8"), salt)
    return hash.hex()

@database.connection_handler
def add_new_user(cursor, login:str, password:hex):
    query = """
          INSERT INTO sandbox (login, password) 
          VALUES (%(login)s, %(password)s); """
    data = {'login': login, 'password': password}
    cursor.execute(query, data)

@database.connection_handler
def get_user_data(cursor, login):
    query = """
          SELECT * FROM sandbox 
          WHERE login = %(login)s; """
    data = {'login': login}
    cursor.execute(query, data)
    return cursor.fetchone()