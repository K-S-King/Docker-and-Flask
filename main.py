from flask import Flask
from pack import hii



app = Flask(__name__)
@app.route("/")
def f_test():
    return "f_tested"


def main():
    print("hello from main")
    print(hii())


if __name__=="__main__":
    app.run(debug=True, port= 8000)
    main()