"""

"""


def logic_1000(login_generator, password_generator, query):
    for i in range(1000):
        login = login_generator.generate()
        if login is None:
            return

        password_generator.reset()
        for j in range(1000):
            password = password_generator.generate()
            if password is None:
                break

            if query(login, password):
                print('SUCCESS!', login, password)
                return


def logic_1000_reversed(login_generator, password_generator, query):
    for i in range(1000):
        password = password_generator.generate()
        if password is None:
            return

        login_generator.reset()
        for j in range(1000):
            login = login_generator.generate()
            if login is None:
                break

            if query(login, password):
                print('SUCCESS!', login, password)
                return
