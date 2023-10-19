import server


if __name__ == "__main__":
    con = server.init_database_connection(database="testing", password="admin")

    app = server.create_app(con)
    app.run()
