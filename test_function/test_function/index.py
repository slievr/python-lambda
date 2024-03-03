from test_function.business_logic.index import call_something

def lambda_handler(event = None, context = None):
    return call_something()

if __name__ == "__main__":
    res = lambda_handler()
    print(res)