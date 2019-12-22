from model.selling import selling
from view import terminal_view

def run():
    options = ["Show the whole selling table",
               "Read the record of the ID",
               "Add new record to taable",
               "Transaction of specific employees",
               "Transaction by specific customer",
               "Transaction by manufacturer",
               "The best selling employee",
               "Ranking of the sold items",
               "Generate the flow report",
               "Additional feature"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "0":
            break
        
        if choice == "1":
            # show whole selling table
            row_table = []  
            row_table = selling.data_manager.get_table_from_file("model/selling/sellflow.csv")
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "2":
            # show specified(ID) record
            row_table = []
            row_table = selling.data_manager.get_table_from_file("model/selling/sellflow.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            store.read(row_table, spec_id)

        elif choice == "3":
            # add new record to selling table
            row_table = []
            row_table = selling.data_manager.get_table_from_file("model/selling/sellflow.csv")
            new_record = []
            li_labels_temp = []
            id_generated = selling.generate_random(row_table)   
            new_record.append(id_generated)
            li_labels_temp.append("employee id")
            li_labels_temp.append("customer id")
            li_labels_temp.append("product id")
            li_labels_temp.append("number of items")
            description = "Id of selling processs is generated automaticly, input the rest of data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = selling.create(row_table, new_record)
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "4":
            # show the record to be deleted
            
            pass
        
        elif choice == "5":
            pass
        
        elif choice == "6":
            pass
                
        elif choice == "7":
            pass

        elif choice == "8":
            pass

        elif choice == "9":
            pass

        elif choice == "10":
            pass
        
        else:
            terminal_view.print_error_message("There is no such choice.")
    
    