# everything you'll need is imported:
from view import terminal_view
from model.crm import crm

def run():
    options = ["Show the whole CRM table",
               "Read record of the specify ID",
               "Add the new record to table",
               "Update the specified record",
               "Remove record of specified ID",
               "Generate random ID/key",
               "ID of the longest name ",
               "Email:name of subscribers",
               "Show the youngest customer",
               "Age of specified customer",
               "Email of specified customer",
               "First name of specified customer"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "0":
            break
        
        if choice == "1":
            # show whole CRM table
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "2":
            # show specified(ID) record
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            crm.read(row_table, spec_id)
        
        
        elif choice == "3":
            # add new record to CRM table
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            new_record = []
            li_labels_temp = []
            id_generated = crm.generate_random(row_table)   
            new_record.append(id_generated)
            li_labels_temp.append("Name")
            li_labels_temp.append("E-mail")
            li_labels_temp.append("Birth of date")
            li_labels_temp.append("Subscribed")
            description = "Id is generated automaticly, input the rest of data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = crm.create(row_table, new_record)
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "4":
            # show the record to be updated
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            crm.read(row_table, spec_id)  
            # update process
            new_record = []
            li_labels_temp = []
            new_record.append(spec_id)
            li_labels_temp.append("New name")
            li_labels_temp.append("New e-mail")
            li_labels_temp.append("New birthday")
            li_labels_temp.append("New subscribed")
            description = "Enter updated data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = crm.update(row_table, spec_id, new_record)
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "5":
            # show the record to be deleted
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            crm.read(row_table, spec_id)
            # deletion of record
            row_table = crm.delete(row_table, spec_id) 
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "6":
            # generate uniquue id/key
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            unique_id = crm.generate_random(row_table) 
            terminal_view.print_result(unique_id, "Generated unique id/key: ")

        elif choice == "7":
            # show ID of customer with longest name
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            id_longest_name = crm.get_longest_name_id(row_table)
            terminal_view.print_result(id_longest_name, "IDs of the customers with the longest name")
        
        elif choice == "8":
            # show list of mail;name subscribers
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            list_of_subs = crm.get_subscribed_emails(row_table)
            terminal_view.print_result(list_of_subs, "List of subscribers:")
        
        elif choice == "9":
            # show list of the youngest customers
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            list_of_youngest = crm.get_youngest_customer(row_table)
            terminal_view.print_result(list_of_youngest, "List of the youngest customers:")
        
        elif choice == "10":
            # show age of specified customer
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            cust_surname = terminal_view.get_inputs(["Please enter surname of customer"], "")
            customer_age = crm.get_age_by(cust_surname, row_table)
            terminal_view.print_result(customer_age, "The age of the specified customer:")
        
        elif choice == "11":
            # show e-mail of specified customer
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            cust_surname = terminal_view.get_inputs(["Please enter surname of customer"], "")
            customer_mail = crm.get_email_by(cust_surname, row_table)
            terminal_view.print_result(customer_mail, "The e-mail of the specified customer:")

        elif choice == "12":
            # show first name of specified customer
            row_table = []
            row_table = crm.data_manager.get_table_from_file("model/crm/customers.csv")
            cust_surname = terminal_view.get_inputs(["Please enter surname of customer"], "")
            customer_first_name = crm.get_first_name_by(cust_surname, row_table)
            terminal_view.print_result(customer_first_name, "The e-mail of the specified customer:")   
        
        else:
            terminal_view.print_error_message("There is no such choice.")
    pass

