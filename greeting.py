def greet(name):
    print(f"Hello, {name}!")

def capitalize_string(s):
    return s.upper()

def main():
    person = "Alice"
    greeting = greet(person)

    message = "this is a test"
    # pylint: disable=unused-variable
    capitalized_message = capitalize_string(message)

    print(greeting)

if __name__ == "__main__":
    main()

