# app.py is the main source, this file is for data access over the .txt file type for practice.
# This could be used in the future as a logger of some type, but needs to be further worked on and refactored, very messy.

from datetime import date, datetime

today = date.today()
now = datetime.now()

# Specify the file path
file_path = "user_data.json"


class DepositHandler:
    def __init__(self, dol, cts):
        self.dollars = dol
        self.cents = cts

    def __str__(self):
        return "You deposited ${}.{:02} to your total balance.".format(
            self.dollars, self.cents
        )


class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, user_data, tot_dollars):
        # Write file into txt file

        # open user_data file
        f = open(self.file_name, "a")
        # Write data_format Dictionary to file
        f.write(f"{user_data}\n")
        # write inputs to File
        f.write(f"Balance: ${tot_dollars}\n")
        f.close()

    def read_file(self):
        # Prompts the user to read the file and displays its contents if the user agrees.
        read_file = input(
            'Do you wish to read the saved file? "Yes" or "No" '
        ).capitalize()

        if read_file == "Yes":
            # Read file
            fr = open(self.file_name, "r")
            print()
            print(fr.read())
        elif read_file == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")

    def last_bal(self):
        # Prompts the user to read the last balance from the file and displays it if the user agrees.
        bal_input = input(
            'Do you wish to read the previous balance? "Yes" or "No" '
        ).capitalize()

        if bal_input == "Yes":
            fr = open(self.file_name, "r")
            lines = fr.readlines()
            last_bal = lines[-1]
            print("=" * 45)
            print(last_bal)
        elif bal_input == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")

    def bal_history(self):
        # Prompts the user to view balance history and displays it if the user agrees.
        bal_hist = input(
            'Do you want to view your balance history? "Yes" or "No" '
        ).capitalize()

        if bal_hist == "Yes":
            fr = open(self.file_name, "r")
            lines = fr.readlines()
            print("=" * 45)
            for i in range(1, len(lines), 2):
                print(lines[i].rstrip("\n"))
            print()
        elif bal_hist == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")


def sep_acct(val):
    # Function to create box around output
    print("=" * 45)
    print(val)
    print("=" * 45)


def date():
    # Todays date
    formatted_date = today.strftime("%m/%d/%Y")
    formatted_time = now.strftime("%I:%M:%S %p")
    print("Today is:", formatted_date)
    print("It is currently:", formatted_time)
    return date


def data_format(user_data):
    # Format data for file
    fname = input("Enter your First Name: ").capitalize()
    lname = input("Enter your Last Name: ").capitalize()
    age = int(input("Enter your age: "))
    date = today.strftime("%m/%d/%Y")
    curr_time = now.strftime("%I:%M:%S %p")

    # Set data with input variable
    user_data["first_name"] = fname
    user_data["last_name"] = lname
    user_data["age"] = age
    user_data["date"] = date
    user_data["time"] = curr_time
    return user_data


def main():

    # Print date
    date()

    # User Data Dictionary
    user_data = {}

    # Inputs
    dollars = int(input("How many dollars are you depositing? "))
    cents = int(input("How much change do you have to deposit? "))

    # Collect User Input as strings
    tot_dollars = str(dollars) + "." + str(cents)

    # Collect User Data
    data_format(user_data)

    # Define and print collected user_inputs
    acct = DepositHandler(dollars, cents)
    sep_acct(acct)

    # handler
    handler = FileHandler("user_data.txt")
    handler.write_file(user_data, tot_dollars)
    handler.read_file()
    handler.last_bal()
    handler.bal_history()


# Initiate the main file
if __name__ == "__main__":
    main()
