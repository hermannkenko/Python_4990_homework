import json

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        """Convert instance attributes to a dictionary"""
        return {"name": self.name, "age": self.age, "email": self.email}

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def to_dict(self):
        """Convert instance attributes (including student_id) to a dictionary"""
        data = super().to_dict()
        data["student_id"] = self.student_id
        return data

class Saver:
    @staticmethod
    def save_to_json(obj, filename="data.json"):
        """Save object data to JSON file"""
        with open(filename, "w") as file:
            json.dump(obj.to_dict(), file, indent=4)
        print(f"Data saved to {filename}")

    @staticmethod
    def display_json(filename="data.json"):
        """Read and display JSON file content"""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                print(json.dumps(data, indent=4))
        except FileNotFoundError:
            print(f"{filename} not found.")
