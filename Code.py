class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self._name = name
        self._employee_id = employee_id
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._date_of_birth = date_of_birth
        self._passport_details = passport_details

    # Getters
    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    def get_age(self):
        return self._age

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_passport_details(self):
        return self._passport_details

    # Setters
    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_age(self, age):
        self._age = age

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget

    # Getters
    def get_client_id(self):
        return self._client_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    def get_budget(self):
        return self._budget

    # Setters
    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def set_budget(self, budget):
        self._budget = budget


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self._guest_id = guest_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getters
    def get_guest_id(self):
        return self._guest_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details


class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, catering_company,
                 cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):
        self._event_id = event_id
        self._event_type = event_type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venue_address = venue_address
        self._catering_company = catering_company
        self._cleaning_company = cleaning_company
        self._decorations_company = decorations_company
        self._entertainment_company = entertainment_company
        self._furniture_supply_company = furniture_supply_company
        self._invoice = invoice

    # Getters
    def get_event_id(self):
        return self._event_id

    def get_event_type(self):
        return self._event_type

    def get_theme(self):
        return self._theme

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_duration(self):
        return self._duration

    def get_venue_address(self):
        return self._venue_address

    def get_catering_company(self):
        return self._catering_company

    def get_cleaning_company(self):
        return self._cleaning_company

    def get_decorations_company(self):
        return self._decorations_company

    def get_entertainment_company(self):
        return self._entertainment_company

    def get_furniture_supply_company(self):
        return self._furniture_supply_company

    def get_invoice(self):
        return self._invoice

    # Setters
    def set_theme(self, theme):
        self._theme = theme

    def set_date(self, date):
        self._date = date

    def set_time(self, time):
        self._time = time

    def set_duration(self, duration):
        self._duration = duration

    def set_venue_address(self, venue_address):
        self._venue_address = venue_address

    def set_invoice(self, invoice):
        self._invoice = invoice


class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self._venue_id = venue_id
        self._name = name
        self._address = address
        self._contact = contact
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Getters
    def get_venue_id(self):
        return self._venue_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact(self):
        return self._contact

    def get_min_guests(self):
        return self._min_guests

    def get_max_guests(self):
        return self._max_guests

    # Setters
    def set_address(self, address):
        self._address = address

    def set_contact(self, contact):
        self._contact = contact


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self._supplier_id = supplier_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getters
    def get_supplier_id(self):
        return self._supplier_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details


class Caterer:
    def __init__(self, caterer_id, name, address, contact_details, menu, min_guests, max_guests):
        self._caterer_id = caterer_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._menu = menu
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Getters
    def get_caterer_id(self):
        return self._caterer_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    def get_menu(self):
        return self._menu

    def get_min_guests(self):
        return self._min_guests

    def get_max_guests(self):
        return self._max_guests

    # Setters
    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def set_menu(self, menu):
        self._menu = menu

import tkinter as tk
from tkinter import ttk, messagebox
import pickle


class EmployeeManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        self.create_employee_frame = ttk.Frame(master)
        self.create_employee_frame.pack(pady=10)

        self.search_employee_frame = ttk.Frame(master)
        self.search_employee_frame.pack(pady=10)

        ttk.Label(self.create_employee_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.create_employee_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5)
        self.emp_id_entry = ttk.Entry(self.create_employee_frame)
        self.emp_id_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        self.department_entry = ttk.Entry(self.create_employee_frame)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Job Title:").grid(row=3, column=0, padx=5, pady=5)
        self.job_title_entry = ttk.Entry(self.create_employee_frame)
        self.job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Basic Salary:").grid(row=4, column=0, padx=5, pady=5)
        self.basic_salary_entry = ttk.Entry(self.create_employee_frame)
        self.basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Age:").grid(row=5, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(self.create_employee_frame)
        self.age_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        self.dob_entry = ttk.Entry(self.create_employee_frame)
        self.dob_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(self.create_employee_frame, text="Passport Details:").grid(row=7, column=0, padx=5, pady=5)
        self.passport_entry = ttk.Entry(self.create_employee_frame)
        self.passport_entry.grid(row=7, column=1, padx=5, pady=5)

        self.create_employee_button = ttk.Button(self.create_employee_frame, text="Create Employee", command=self.create_employee)
        self.create_employee_button.grid(row=8, columnspan=2, padx=5, pady=5)

        ttk.Label(self.search_employee_frame, text="Search Employee by ID:").grid(row=0, column=0, padx=5, pady=5)
        self.search_emp_id_entry = ttk.Entry(self.search_employee_frame)
        self.search_emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_employee_button = ttk.Button(self.search_employee_frame, text="Search", command=self.search_employee)
        self.search_employee_button.grid(row=1, columnspan=2, padx=5, pady=5)

    def create_employee(self):
        name = self.name_entry.get()
        employee_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.dob_entry.get()
        passport_details = self.passport_entry.get()

        employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.save_employee(employee)

    def save_employee(self, employee):
        try:
            with open('employees.pkl', 'ab') as file:
                pickle.dump(employee, file)
            print("Employee saved successfully!")
        except Exception as e:
            print("Error saving employee:", e)

    def search_employee(self):
        employee_id = self.search_emp_id_entry.get()
        try:
            with open('employees.pkl', 'rb') as file:
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee.get_employee_id() == employee_id:
                            message = "Employee found!\n"
                            message += f"Name: {employee.get_name()}\n"
                            message += f"Employee ID: {employee.get_employee_id()}\n"
                            message += f"Department: {employee.get_department()}\n"
                            message += f"Job Title: {employee.get_job_title()}\n"
                            message += f"Basic Salary: {employee.get_basic_salary()}\n"
                            message += f"Age: {employee.get_age()}\n"
                            message += f"Date of Birth: {employee.get_date_of_birth()}\n"
                            message += f"Passport Details: {employee.get_passport_details()}"
                            messagebox.showinfo("Employee Details", message)
                            return
                    except EOFError:
                        break
            messagebox.showerror("Employee not found!")
        except Exception as e:
            messagebox.showerror("Error searching for employee:", e)
class ClientManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Client Management System")

        self.create_client_frame = ttk.Frame(master)
        self.create_client_frame.pack(pady=10)

        self.search_client_frame = ttk.Frame(master)
        self.search_client_frame.pack(pady=10)

        ttk.Label(self.create_client_frame, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = ttk.Entry(self.create_client_frame)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.create_client_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.create_client_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.create_client_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(self.create_client_frame)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.create_client_frame, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = ttk.Entry(self.create_client_frame)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.create_client_frame, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = ttk.Entry(self.create_client_frame)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        self.create_client_button = ttk.Button(self.create_client_frame, text="Create Client", command=self.create_client)
        self.create_client_button.grid(row=5, columnspan=2, padx=5, pady=5)

        ttk.Label(self.search_client_frame, text="Search Client by ID:").grid(row=0, column=0, padx=5, pady=5)
        self.search_client_id_entry = ttk.Entry(self.search_client_frame)
        self.search_client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_client_button = ttk.Button(self.search_client_frame, text="Search", command=self.search_client)
        self.search_client_button.grid(row=1, columnspan=2, padx=5, pady=5)

    def create_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        budget = self.budget_entry.get()

        client = Client(client_id, name, address, contact_details, budget)
        self.save_client(client)

    def save_client(self, client):
        try:
            with open('clients.pkl', 'ab') as file:
                pickle.dump(client, file)
            messagebox.showinfo("Success", "Client saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving client: {e}")

    def search_client(self):
        client_id = self.search_client_id_entry.get()
        try:
            with open('clients.pkl', 'rb') as file:
                while True:
                    try:
                        client = pickle.load(file)
                        if client.get_client_id() == client_id:
                            message = f"Client found!\nName: {client.get_name()}\nClient ID: {client.get_client_id()}\nAddress: {client.get_address()}\nContact Details: {client.get_contact_details()}\nBudget: {client.get_budget()}"
                            messagebox.showinfo("Client Details", message)
                            return
                    except EOFError:
                        break
            messagebox.showinfo("Client Details", "Client not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Error searching for client: {e}")


class GuestManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Guest Management System")

        self.create_guest_frame = ttk.Frame(master)
        self.create_guest_frame.pack(pady=10)

        self.search_guest_frame = ttk.Frame(master)
        self.search_guest_frame.pack(pady=10)

        ttk.Label(self.create_guest_frame, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = ttk.Entry(self.create_guest_frame)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.create_guest_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.create_guest_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.create_guest_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(self.create_guest_frame)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.create_guest_frame, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = ttk.Entry(self.create_guest_frame)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        self.create_guest_button = ttk.Button(self.create_guest_frame, text="Create Guest", command=self.create_guest)
        self.create_guest_button.grid(row=4, columnspan=2, padx=5, pady=5)

        ttk.Label(self.search_guest_frame, text="Search Guest by ID:").grid(row=0, column=0, padx=5, pady=5)
        self.search_guest_id_entry = ttk.Entry(self.search_guest_frame)
        self.search_guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_guest_button = ttk.Button(self.search_guest_frame, text="Search", command=self.search_guest)
        self.search_guest_button.grid(row=1, columnspan=2, padx=5, pady=5)

    def create_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)
        self.save_guest(guest)

    def save_guest(self, guest):
        try:
            with open('guests.pkl', 'ab') as file:
                pickle.dump(guest, file)
            messagebox.showinfo("Success", "Guest saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving guest: {e}")

    def search_guest(self):
        guest_id = self.search_guest_id_entry.get()
        try:
            with open('guests.pkl', 'rb') as file:
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.get_guest_id() == guest_id:
                            message = f"Guest found!\nName: {guest.get_name()}\nGuest ID: {guest.get_guest_id()}\nAddress: {guest.get_address()}\nContact Details: {guest.get_contact_details()}"
                            messagebox.showinfo("Guest Details", message)
                            return
                    except EOFError:
                        break
            messagebox.showinfo("Guest Details", "Guest not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Error searching for guest: {e}")

class EventManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")
        # Create style for buttons
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 14), background='#4CAF50', foreground='white')

        # Create buttons for each option
        self.employee_button = ttk.Button(master, text="Employee", command=self.show_employee_options)
        self.employee_button.pack(pady=5)


        self.client_button = ttk.Button(master, text="Client", command=self.show_client_options)
        self.client_button.pack(pady=5)


        self.guest_button = ttk.Button(master, text="Guest", command=self.show_guest_options)
        self.guest_button.pack(pady=5)


    def show_employee_options(self):
        root = tk.Tk()
        app = EmployeeManagement(root)
        root.mainloop()
    def show_client_options(self):
        root = tk.Tk()
        app = ClientManagementApp(root)
        root.mainloop()

    def show_guest_options(self):
        root = tk.Tk()
        root.title("Guest Management System")
        app = GuestManagementApp(root)
        root.mainloop()

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = EventManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

