# from flask import Flask, render_template, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # AWS RDS MySQL configuration
# db_config = {
#     "host": "myrds.chiae0kead3l.us-east-1.rds.amazonaws.com",
#     "user": "admin",
#     "password": "rds12345",
#     "database": "myrds",
# }

# @app.route("/", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]

#         # Connect to the database
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()

#         # Insert user data
#         insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#         cursor.execute(insert_query, (name, email))
#         connection.commit()

#         # Close the connection
#         cursor.close()
#         connection.close()

#         return redirect("/registered")

#     return render_template("register.html")

# @app.route("/registered")
# def registered():
#     # Fetch registered users from the database
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()

#     select_query = "SELECT name, email FROM users"
#     cursor.execute(select_query)
#     registered_users = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return render_template("registered.html", registered_users=registered_users)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

#  MySQL configuration
db_config = {
    "host": "database-1.cwogwgtpopiu.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "myrds12345",
    "database": "project",
}

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert user data
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, email))
        connection.commit()

        # Close the connection
        cursor.close()
        connection.close()

        return redirect("/view-registered")

    return render_template("register.html")

@app.route("/view-registered", methods=["GET"])
def view_registered():
    # Fetch registered users from the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    select_query = "SELECT name, email FROM users"
    cursor.execute(select_query)
    registered_users = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("registered_users.html", registered_users=registered_users)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # AWS RDS MySQL configuration
# db_config = {
#     "host": "test-db.cb0tfal8slh9.us-east-1.rds.amazonaws.com",
#     "user": "admin",
#     "password": "balu1234",
#     "database": "your_new_database",
# }

# registered_users = []  # To store registered users

# @app.route("/", methods=["GET", "POST"])
# def register():
#     global registered_users  # Use global variable

#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]

#         # Connect to the database
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()

#         # Insert user data
#         insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#         cursor.execute(insert_query, (name, email))
#         connection.commit()

#         # Update the list of registered users
#         registered_users.append((name, email))

#         # Close the connection
#         cursor.close()
#         connection.close()

#     return render_template("register.html", registered_users=registered_users)

# @app.route("/view-registered", methods=["GET"])
# def view_registered():
#     return render_template("registered_users.html", registered_users=registered_users)

# if __name__ == "__main__":
#     app.run(debug=True)
