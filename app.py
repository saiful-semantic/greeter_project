from utils.helpers import greet

# app.py
def main():
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()