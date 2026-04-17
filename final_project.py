
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "grievances.csv"

class Grievance:
    def __init__(self, name, reg_no, category, description):
        self.name = name
        self.reg_no = reg_no
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.status = "Submitted"

    def to_list(self):
        return [
            self.name,
            self.reg_no,
            self.category,
            self.description,
            self.date,
            self.status
        ]


def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "RegNo", "Category", "Description", "Date", "Status"])


def add_grievance():
    print("\nEnter Grievance Details")
    name = input("Student Name: ")
    reg = input("Register Number: ")
    category = input("Category (Academic/Exam/Hostel/etc): ")
    desc = input("Description: ")

    g = Grievance(name, reg, category, desc)

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(g.to_list())

    print("Grievance submitted successfully!")


def view_grievances():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        print("\n--- All Grievances ---")
        for row in reader:
            print(row)


def search_grievance():
    reg = input("\nEnter Register Number: ")
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == reg:
                print("\nGrievance Found:")
                print(row)
                found = True

    if not found:
        print("No grievance found.")

def update_status():
    reg = input("\nEnter Register Number: ")
    updated = False
    rows = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == reg:
                print("Current Status:", row[5])
                row[5] = input("Enter new status: ")
                updated = True
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if updated:
        print("Status updated successfully!")
    else:
        print("Grievance not found.")

def show_reports():
    total = 0
    status_count = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            total += 1
            status = row[5]
            status_count[status] = status_count.get(status, 0) + 1

    print("\n--- Report ---")
    print("Total Grievances:", total)
    print("Status Distribution:", status_count)

def show_charts():
    categories = {}
    statuses = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cat = row[2]
            stat = row[5]

            categories[cat] = categories.get(cat, 0) + 1
            statuses[stat] = statuses.get(stat, 0) + 1

    plt.bar(categories.keys(), categories.values())
    plt.title("Grievances by Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

    plt.pie(statuses.values(), labels=statuses.keys(), autopct="%1.1f%%")
    plt.title("Grievance Status Distribution")
    plt.show()

def menu():
    init_file()

    while True:
        print("\n===== SGRS MENU =====")
        print("1. Submit Grievance")
        print("2. View All Grievances")
        print("3. Search Grievance")
        print("4. Update Status (Admin)")
        print("5. Reports")
        print("6. Charts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_grievance()

        elif choice == "2":
            view_grievances()

        elif choice == "3":
            search_grievance()

        elif choice == "4":
            update_status()

        elif choice == "5":
            show_reports()

        elif choice == "6":
            show_charts()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()