""" Terminal view module """


def print_table(table, title_list):
    print("/" + 122*"-" + "\\")
    size_lista = [10, 40, 40, 14, 14]
    for i in range(len(title_list)):
        if i < len(title_list)-1:
            k = len(title_list[i])
            ile_spac_przed = int((size_lista[i]-k)/2)
            ile_spac_po = size_lista[i] - (k + ile_spac_przed)
            print("|" + ile_spac_przed*" " + title_list[i] + ile_spac_po*" ", end = "")
        else:
            k = len(title_list[4])
            ile_spac_przed = int((size_lista[i]-k)/2)
            ile_spac_po = size_lista[i] - (k + ile_spac_przed)
            print("|" + ile_spac_przed*" " + title_list[i] + ile_spac_po*" " + "|")
    print("|" + size_lista[0]*"-" + "|" + size_lista[1]*"-" + "|"
             +size_lista[2]*"-" + "|" + size_lista[3]*"-" + "|" + size_lista[4]*"-" + "|")
    for i in range(len(table)):
        for j in range(len(title_list)):
            if j < len(title_list)-1:
                k = len(table[i][j])
                ile_spac_przed = int((size_lista[j]-k)/2)
                ile_spac_po = size_lista[j] - (k + ile_spac_przed)
                print("|" + ile_spac_przed*" " + table[i][j] + ile_spac_po*" ", end = "")
            else:
                k = len(table[i][j])
                ile_spac_przed = int((size_lista[j]-k)/2)
                ile_spac_po = size_lista[j] - (k + ile_spac_przed)
                print("|" + ile_spac_przed*" " + table[i][j] + ile_spac_po*" " + "|")
    print("\\" + 122*"-" + "/")


def print_result(result, label):
    print(label)
    try:
        for i in range(len(result)):
            print(result[i])
    except:
        print(str(result))

def print_menu(title, list_options, exit_message):
    print("")
    print(title + ": ")
    for i in range(len(list_options)):
        if i == 2 or i == 5 or i == 8 or i == 11:
            print("\t(" + str(i+1) + ") " + list_options[i])
        else:
            print("\t(" + str(i+1) + ") " + list_options[i] + "     ", end = "")
    print("\t(0) " + exit_message)


def get_inputs(list_labels, title):
    answer_list = []
    print(title)
    for i in range(len(list_labels)):
        user_input = input("\t" + list_labels[i] + "\t<user_input_" + str(i+1) + "> ")
        answer_list. append(user_input)
    return answer_list


def get_choice(options):
    print_menu("Menu of choices",options, "Exit")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    print("ERROR: " + message)
