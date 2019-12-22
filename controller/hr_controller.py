# everything you'll need is imported:
from view import terminal_view
from model.hr import hr

def run():
    options = ["Show the whole HR table",
               "Record of specified ID",
               "Add new record to the table",
               "Update specified record",
               "Remove the record (ID)",
               "Generate random ID/key",
               "Show  the oldest person",
               "Person closest average",
               "Person of shortest surname",
               "Age of specified employee",
               "Email of the employee",
               "First name of the employee"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "0":
            break
        
        if choice == "1":
            # show whole store table
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "2":
            # show specified(ID) record
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            hr.read(row_table, spec_id)
        
        elif choice == "3":
            # add new record to HR table
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            new_record = []
            li_labels_temp = []
            id_generated = hr.generate_random(row_table)   
            new_record.append(id_generated)
            li_labels_temp.append("Name")
            li_labels_temp.append("E-mail")
            li_labels_temp.append("Birth of date")
            li_labels_temp.append("Salery")
            description = "Id is generated automaticly, input the rest of data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = hr.create(row_table, new_record)
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "4":
            # show the record to be updated
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            hr.read(row_table, spec_id)  
            # update process
            new_record = []
            li_labels_temp = []
            new_record.append(spec_id)
            li_labels_temp.append("New name")
            li_labels_temp.append("New e-mail")
            li_labels_temp.append("New birthday")
            li_labels_temp.append("New salery")
            description = "Enter updated data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = hr.update(row_table, spec_id, new_record)
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "5":
            # show the record to be deleted
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            hr.read(row_table, spec_id)
            # deletion of record
            row_table = hr.delete(row_table, spec_id) 
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "6":
            # generate uniquue id/key
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            unique_id = hr.generate_random(row_table) 
            terminal_view.print_result(unique_id, "Generated unique id/key: ")
        
        elif choice == "7":
            # show list of the oldest employee
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            list_of_oldest = hr.get_oldest_person(row_table)
            terminal_view.print_result(list_of_oldest, "List of the oldest employee:")
        
        elif choice == "8":
            # show names of employees with salery closest to average
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            list_of_avg_salery = hr.get_persons_closest_to_average_salary(row_table)
            terminal_view.print_result(list_of_avg_salery, "List of employees closest to average salery:")
        
        elif choice == "9":
            # list of employee of shortest surname
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            list_of_shortest_surname = hr.get_shortest_surname(row_table)
            terminal_view.print_result(list_of_shortest_surname, "List of employees with shortest surname")

        elif choice == "10":
            # show age of specified customer
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            emp_surname = terminal_view.get_inputs(["Please enter surname of employee"], "")
            employee_age = hr.get_age_by(emp_surname, row_table)
            terminal_view.print_result(employee_age, "The age of the specified employee:")
        
        elif choice == "11":
            # show e-mail of specified customer
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            emp_surname = terminal_view.get_inputs(["Please enter surname of employee"], "")
            emp_mail = hr.get_email_by(emp_surname, row_table)
            terminal_view.print_result(emp_mail, "The e-mail of the specified employee:")

        elif choice == "12":
            # show first name of specified customer
            row_table = []
            row_table = hr.data_manager.get_table_from_file("model/hr/persons.csv")
            emp_surname = terminal_view.get_inputs(["Please enter surname of employee"], "")
            emp_first_name = hr.get_first_name_by(emp_surname, row_table)
            terminal_view.print_result(emp_first_name, "The e-mail of the specified employee:") 

        else:
            terminal_view.print_error_message("There is no such choice.")
    pass
