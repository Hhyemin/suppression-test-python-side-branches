def greet(name):
    print(f"Hello, {name}!")

def capitalize_string(s):
    return s.upper()

def main():
    person = "Alice"
    greeting = greet(person)

    # pylint: disable=unused-variable
    capitalized_message = capitalize_string(greeting)

    print(greeting)
    print(capitalized_message)

if __name__ == "__main__":
    main()

