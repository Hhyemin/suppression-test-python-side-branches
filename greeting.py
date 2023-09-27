def greet(name):
    print(f"Hello, {name}!")
    return f"Bye, {name}!"

def capitalize_string(s):
    return s.upper()

def main():
    person1 = "Alice"
    greeting1 = greet(person1)

    capitalized_message = capitalize_string(greeting1)

    print(capitalized_message)

    person2 = "Lucy"
    greet(person2)

if __name__ == "__main__":
    main()
