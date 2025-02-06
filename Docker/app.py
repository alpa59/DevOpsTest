<<<<<<< Updated upstream
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevOps World! Your CI/CD pipeline is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
print("ligma")

import unittest

def add(a, b):
    return a + b

def testadd():
    assert 1 + 1 == 2

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

>>>>>>> Stashed changes
