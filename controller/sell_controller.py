from model.selling import selling
from view import terminal_view

def run():
    options = ["Show the whole selling table",
               "Read the record of the ID",
               "Add new record to table",
               "Transaction of specific employees",
               "Transaction by specific customer",
               "Transaction by manufacturer",
               "The best selling employee",
               "Ranking of the sold items",
               "Generate the flow report"]
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
            # transaction by specific employee
            row_table = []
            row_table = selling.data_manager.get_table_from_file("model/selling/sellflow.csv")
            emplo_transactions = []
            emplo_one_transaction = []
            spec_id_emplo = terminal_view.get_inputs(["Please enter employee ID: "], "")
            trans_emplo = selling.get_eplo_trans(row_table, spec_id_emplo)
            terminal_view.print_result(trans_emplo, "List of employee transaction:")
        
        elif choice == "5":
            # transaction by specyfic customer
            pass
        
        elif choice == "6":
            # transction by specyfic manufacture
            pass
                
        elif choice == "7":
            # the best selling employee
            pass

        elif choice == "8":
            # ranking of the sold action
            pass

        elif choice == "9":
            # 
            pass

        elif choice == "10":
            # generate the report
            pass
        
        else:
            terminal_view.print_error_message("There is no such choice.")
    
    