from smokeobserver.Listener import Listener


class TestListener(Listener):
    def __init__(self):
        self.is_called = None

    def update(self):
        print("TestListener was called")
        self.is_called = True
