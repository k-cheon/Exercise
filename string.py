name = "Eric"
first_name = "Eric"
last_name = "Idle"
age = 36
profession = "comedian"
affiliation = "Monty Python"

print("Hello, %s %s. You are %s." % (first_name, last_name, age))
print("Hello, {}. You are {}." .format(first_name, age))
print("Hello, {1}. You are {0}." .format(age, first_name))

person = {'name': 'Eric', 'age': 36}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))

# f-Strings: A new and Improved way to format Strings in Python
print(f"Hello, {name}. You are {age}.")
print(F"Hello, {name}. You are {age}.")

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(F"{to_lowercase(name)} is funny.")

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "48")
print(f"{new_comedian}")
print(f"{new_comedian!r}")

name = "Eric"
profession = "comedian"
affiliation = "Monty Pytho"

message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

message = f"Hi {name}. " \
        f"You are a {profession}. " \
        f"You were in {affiliation}."
print(message)

message = f"""
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
"""
print(message)