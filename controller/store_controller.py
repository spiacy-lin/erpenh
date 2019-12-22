# everything you'll need is imported:
from model.store import store
from view import terminal_view

def run():
    options = ["Show the whole games table",
               "Read the record of the ID",
               "Add new record to taable",
               "Update specified record",
               "Remove record of the ID",
               "Generate random ID/key",
               "Quantities by manufacture",
               "Average price by manufacture",
               "Oldest game in the store",
               "Cheapest game in the store",
               "Age of the specified title",
               "Games by specified keywords"]
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "0":
            break
        
        if choice == "1":
            # show whole store table
            row_table = []  
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "2":
            # show specified(ID) record
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            store.read(row_table, spec_id)

        elif choice == "3":
            # add new record to store table
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            new_record = []
            li_labels_temp = []
            id_generated = store.generate_random(row_table)   
            new_record.append(id_generated)
            li_labels_temp.append("Name")
            li_labels_temp.append("Manufacturer")
            li_labels_temp.append("Price($)")
            li_labels_temp.append("Realese(1999-06-21)")
            description = "Id is generated automaticly, input the rest of data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = store.create(row_table, new_record)
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "4":
            # show the record to be updated
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            store.read(row_table, spec_id)  
            # update process
            new_record = []
            li_labels_temp = []
            new_record.append(spec_id)
            li_labels_temp.append("New name")
            li_labels_temp.append("New manufacturer")
            li_labels_temp.append("New price($)")
            li_labels_temp.append("New realese(1999-06-21)")
            description = "Enter updated data"
            new_record_temp = terminal_view.get_inputs(li_labels_temp, description)
            for i in range(len(new_record_temp)):
                new_record.append(new_record_temp[i])
            row_table = store.update(row_table, spec_id, new_record)
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
        
        elif choice == "5":
            # show the record to be deleted
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            specified_id = terminal_view.get_inputs(["Please enter ID: "], "")
            spec_id = specified_id[0]
            store.read(row_table, spec_id)
            # deletion of record
            row_table = store.delete(row_table, spec_id) 
            # show updated table
            header = row_table[0] 
            del row_table[0]
            terminal_view.print_table(row_table, header)
            
        elif choice == "6":
            # generate uniquue id/key
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            unique_id = store.generate_random(row_table) 
            terminal_view.print_result(unique_id, "Generated unique id/key: ")
        
        elif choice == "7":
            # present quantities of games by manufactures
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            outcome = store.get_counts_by_manufacturers(row_table)
            terminal_view.print_result(str(outcome), "Quantities by manufacturers")
        
        elif choice == "8":
            # show the average
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            manufac = terminal_view.get_inputs(["Please enter manufacturer: "], "")
            outcome = store.get_average_by_manufacturer(row_table, manufac)
            terminal_view.print_result(outcome, "Average by specified manufacturer")
                
        elif choice == "9":
            # show the oldest game
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            outcome = store.get_oldest_game(row_table)
            terminal_view.print_result(outcome, "The oldest game: ")
        
        elif choice == "10":
            # show the cheapest game
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            outcome = store.get_cheapest_game(row_table)
            terminal_view.print_result(outcome, "The cheapest game: ")

        elif choice == "11":
            # show age of specified title
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            name = terminal_view.get_inputs(["Please enter title of game:"], "")
            name_str = name[0]
            outcome = store.get_age_by(name_str, row_table)
            terminal_view.print_result(outcome, "The age of specified title: ")

        elif choice == "12":
            # show game of specified keyword
            row_table = []
            row_table = store.data_manager.get_table_from_file("model/store/games.csv")
            k_word = terminal_view.get_inputs(["Please enter keyword: "], "")
            outcome = store.get_game_by(k_word, row_table)
            terminal_view.print_result(outcome, "The title of the game of specified keyword: ")
        
        else:
            terminal_view.print_error_message("There is no such choice.")
    
    