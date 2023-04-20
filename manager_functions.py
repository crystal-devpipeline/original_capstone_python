# Cap Stone COMPETENCY TRACKING TOOL
import datetime
from competency_tracker_database import cursor
import sqlite3
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


class Manager(User):
    
    def show_manager_menu():
        prompt = """Manager Menu
            (1) View All Users
            (2) Search for User by First or Last Name
            (3) View Competency Report for All Users 
            (4) View Competency Reports for a User 
            (5) View a List of Assessments for a User
            (6) Add a New Competency
            (7) Add an Assessment Result for a User 
            (8) Edit a User's Information
            (9) Edit a Competency
            (10) Edit an Assessment 
            (11) Edit an Assessment result
            (12) Delete an Assessment Result
            (13) Exit
                """
        prompt_choice = input(prompt)
        if prompt_choice == "1":
            view_all_users()
        elif prompt_choice == "2":
            search_user()
        elif prompt_choice == "3":
            view_comp_report_all_users()
        elif prompt_choice == "4":
            view_comp_report_for_a_user()
        elif prompt_choice == "5":
            view_list_of_assessment_for_a_user()
        elif prompt_choice == "6":
            add_new_competency()
        elif prompt_choice == "7":
            add_assessment_result_for_user()
        elif prompt_choice == "8":
            edit_user_info()
        elif prompt_choice == "9":
            edit_a_competency()
        elif prompt_choice == "10":
            edit_an_assesment()
        elif prompt_choice == "11":
            edit_an_assessment_result()
        elif prompt_choice == "12":
            delete_an_assessment_result()
        elif prompt_choice == "13":
            exit()


    # view all users in a list
        def view_all_users():
            select_sql= "SELECT * FROM Users"
            cursor.execute(select_sql)
            connection.commit()
            rows = cursor.fetchall()
            print(f"{'ID':<4}{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}{'Password':<20}{'Date Created':<20}{'Hire Date':<20}{'User Type':<8}{'Active':<10}")
            for row in rows:
                print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}{row[3]:<25}{row[4]:<20}{row[5]:<20}{row[6]:<20}{row[7]:<20}{row[8]:<8}{row[9]:<4}")



    # search for users by first name or last name
        def search_user():
            query = input("Enter first or last name: ")
            select_sql= "SELECT * FROM Users where first_name LIKE %?% or last_name LIKE %?%"
            cursor.execute(select_sql)
            connection.commit()
            rows = cursor.fetchall()
            print(query)
            select_sql= "SELECT * FROM Users"
            rows = cursor.fetchall()
            print(f"{'ID':<4}{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}{'Password':<20}{'Date Created':<20}{'Hire Date':<20}{'User Type':<8}{'Active':<4}")
            for row in rows:
                print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}{row[3]:<25}{row[4]:<20}{row[5]:<20}{row[6]:<20}{row[7]:<20}{row[8]:<8}{row[9]:<4}")



        # view a report of all users and their competency levels for a given competency
        def view_comp_report_all_users():
            select_sql= "SELECT * FROM Competencies"
            cursor.execute(select_sql)
            connection.commit()
            rows = cursor.fetchall()
            print(f"{'competency_id':<4}{'name':<15}{'date_created':<16}")
            for row in rows:
                print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}")

                

        # view a competency level report for an individual user
        def view_comp_report_for_a_user():
            query = input("Enter first or last name: ")
            select_sql = "SELECT * FROM Competencies WHERE first_name LIKE %?% or last_name LIKE %?%"
            cursor.execute(select_sql)
            connection.commit()
            rows = cursor.fetchone()
            print(query)
            print(f"{'competency_id':<4}{'name':<15}{'date_created':<16}")
            for row in rows:
                print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}")


        # view a list of assessments for a given user
        def view_list_of_assessment_for_a_user():
            query = input("Enter first or last name: ")
            select_sql = "SELECT name FROM Assessments where first_name LIKE %?% or last_name LIKE %?%"
            cursor.execute(select_sql)
            connection.commit()
            rows = cursor.fetchone()
            print(query)
            print(f"{'assessment_id':<4}{'competency_id':<4}{'name':<15}{'date_created':<16}")
            for row in rows:
                print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}{row[3]:<16}")


        # add a new competency INSERT???
        def add_new_competency():
            competency_id = input("Add new competency: ")
            name = input("Add new competency name")
            date_created =  datetime.date.today()
            values = (competency_id, name, date_created)
            insert_sql = "INSERT INTO Compentencies (competency_id, name, date_created) VALUES (?,?,?)"
            cursor.execute(insert_sql, values)
            connection.commit()
            return print('New Compentency added')



        # add an assessment result for a user for an assessment - INSERT???
        def add_assessment_result_for_user():
            score = input("Add Assessment score: ")
            date_taken  = input("Enter date assessment was taken on: ")
            manager_id = input("Add manager ID: ")
            values = (score, date_taken, manager_id)
            insert_sql = "INSERT INTO Assessment_results (score, date_taken, manager_id) VALUES (?, ?, ?)"
            cursor.execute(insert_sql, values)
            connection.commit()
            return print("Assessment results have been successfully added!")
            

            # Refactor this one
        def edit_user_info():
            query =  input("Enter User ID: ")
            select_sql = "SELECT * Users WHERE id = ? "
            update_sql = "UPDATE Customers SET first_name = ?, last_name = ?, email = ? , phone = ? , password = ?, date_created = ?, hire_date = ?, user_type = ?"
            cursor.execute(update_sql,( first_name, last_name, email, phone, password, date_created, hire_date, user_type,))
            values = (first_name, last_name, email, phone, password, date_created, hire_date, user_type,)      
            cursor.execute(select_sql,values)
            connection.commit
            row = cursor.fetchone()
            print(query)
            print(f"{'ID':<4}{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}{'Password':<20}{'Date Created':<20}{'Hire Date':<20}{'User Type':<8}{'Active':<10}")
            print(f"{row[0]:<4}{row[1]:<15}{row[2]:<16}{row[3]:<25}{row[4]:<20}{row[5]:<20}{row[6]:<20}{row[7]:<20}{row[8]:<8}{row[9]:<10}")
            
            while True:
                print("\n********* UPDATE*********\n")
                print("[1] Update First name")
                print("[2] Update Last name")
                print("[3] Update Email")
                print("[4] Update Phone Number")
                print("[5] Update Password")
                print("[6] Update Date Created")
                print("[7] Update Hire Date")
                print("[8] Update User Type")
                print("[9] Save Changes")
                prompt=input("").upper() 
                if prompt== "1":
                    first_name = input("Update First Name: ")
                    edit_user_info()   
                elif prompt=="2":
                    last_name = input("Updated Last Name: ")
                    edit_user_info()       
                elif prompt=="3":
                    email = input("Update Email: ")
                    edit_user_info()       
                elif prompt=="4":
                    phone = input("Update Phone Number: ")
                    edit_user_info()       
                elif prompt=="5":
                    password = input("Update Password: ")
                    edit_user_info()       
                elif prompt=="6":
                    date_created = input("Update Date Created: ")
                    edit_user_info()       
                elif prompt=="7":
                    hire_date= input("Update Hire Date: ")
                    edit_user_info() 
                elif prompt=="8":
                    user_type = input("Update User Type: ")
                    edit_user_info() 
                elif prompt=="9":
                    break


        # edit a competency
        def edit_a_competency():
            user_id =  input("Enter User ID: ")
            values = (user_id,)
            select_sql = "SELECT * Users WHERE id = ? "
            cursor.execute(select_sql, values)
            connection.commit()

            while True: 
                print("What would you like to update?")
                print("[1] Update a Competency")
                print("[2] Update Date Created")

                prompt=input("").upper() 
                if prompt== "1":
                    first_name = input("Update First Name: ")
                    edit_user_info()   
                elif prompt=="2":
                    last_name = input("Updated Last Name: ")
                    edit_user_info()  

            

        # edit an assessment
        def edit_an_assesment():
            user_id =  input("Enter User ID: ")
            select_sql = "SELECT * Users WHERE id = ? "
            values = (user_id,)
            cursor.execute(select_sql,values)
            row = cursor.fetchone()


        # edit an assessment result
        def edit_an_assessment_result():
            user_id =  input("Enter User ID: ")
            select_sql = "SELECT * Users WHERE id = ? "
            values = (user_id,)
            cursor.execute(select_sql,values)
            row = cursor.fetchone()

        # delete an assessment result
        def delete_an_assessment_result():
            user_id = int(input('Enter the user ID:  '))
            confirm = input("Are you sure? This is PERMANENT!:")
            if (confirm == 'yes' or confirm == 'y'):
                delete_user(id)
                
            input('Customer successfully deleted!  (press enter to continue. )')






            

        def search_users():
            query = input("Enter the query: ")
            select_sql= "SELECT * FROM Users where first_name like %?% or last_name like %?%"
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            print_user_rows(rows)


        def edit_user(User):
            user_id = int(input("Enter the ID of the user you want to update: "))
            select_sql = "SELECT * FROM Users WHERE user_id = ?"
            to_update = ("first_name","last_name","email","phone","password","date_created","hire_date","user_type","active")
            cursor.execute(select_sql)
            user_row = cursor.fetchone()
            print_user_rows([user_row])

            # for num, field in enumerate(to_update):
            #     print(f'{num}: {field}')

            # field_index = int(input('\n')) + 1
            # new_value = input("What would you like the new value to be? ")
            # user_row[field_index] = new_value
            
            # # * edit_options():
            # #         * edit a user's information
            # #         * edit a competency
            # #         * edit an assessment
            # #         * edit an assessment result

            # update_user((new_value,user_id), to_update[int(user_choice)])
            # print('Your update was successful. ')
            # print(search_name(cust_name))
            # input('press enter to continue. ')



        # add SQL to complete delete functionality
        def delete_user():
            user_id = int(input('Enter the user ID:  '))
            confirm = input("Are you sure? This is PERMANENT!:")
            if (confirm == 'yes' or confirm == 'y'):
                delete_user(user_id, first_name, last_name, email, phone, password, date_created, hire_date, user_type,) 
                
            input('Customer successfully deleted!  (press enter to continue. )')

    # Your application should allow for CSV export of at least two lists. 
        def expot_csv():
            pass


        def import_csv():
            pass


    # Competency Results Summary for all Users
        def view_competency_report():
            pass
