class MyException(Exception):
    def __init__(self, message="Es werden nur Positive Zahlen akzeptiert"):
        self.message = message
        super().__init__(self.message)

def run():
    try:
        userInput = input("geben sie ihr alter an")
        if int(userInput) < 0:
            raise MyException
        print("(>^.^)> Es wurden keine Exceptions erhoben <(^.^<)")
    except MyException as e:
        print(e)
        run()
    except Exception as e:
        print(e)


run()
