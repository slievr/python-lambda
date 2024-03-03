from test_function.business_logic.index import call_something

class IndexTest:
    def test_call():
        assert call_something() == "test"