""" Store module """

# everything you'll need is imported:
import random
from model import data_manager

def generator():
    listA = ["A","B","C","D","E","F","G","H","I", 
    "J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]
    list1 = ["0","1","2","3","4","5","6","7","8","9"]
    listS = ["!","@","#","$","%","&"]
    initial_id = []
    inpA = random.sample(listA, k = 2)
    initial_id.append(inpA[0])
    initial_id.append(inpA[1])
    inpa = random.sample(listA, k = 2)
    initial_id.append(inpa[0].lower())
    initial_id.append(inpa[1].lower())
    inp1 = random.sample(list1, k = 2)
    initial_id.append(inp1[0])
    initial_id.append(inp1[1])
    inpS = random.sample(listS, k = 2)
    initial_id.append(inpS[0])
    initial_id.append(inpS[1])  
    final_id = []
    while len(final_id)<= 7:
        pick_element = random.choice(initial_id)
        final_id.append(pick_element)
        initial_id.remove(pick_element)
    id_key = ""
    for i in range(len(final_id)):
        id_key += final_id[i]
    return id_key


def generate_random(table):
    keys_set = set("")
    for i in range(len(table)):
        elem = table[i][0]
        keys_set.add(elem)
    gen_key = generator()
    gen_key_set = set("")

    gen_key_set.add(gen_key)
    while len(keys_set.intersection(gen_key_set)) != 0:
        gen_key = generator()
        gen_key_set.pop()
        gen_key_set.add(gen_key)
    return gen_key

   
def create(table, record):
    table.append(record)
    data_manager.write_table_to_file("model/store/games.csv", table)
    return table
    

def read(table, id_):
    print("/" + 122*"-" + "\\")
    size_lista = [10, 40, 40, 14, 14]
    for i in range(len(table[0])):
        if i < len(table[0])-1:
            k = len(table[0][i])
            ile_spac_przed = int((size_lista[i]-k)/2)
            ile_spac_po = size_lista[i] - (k + ile_spac_przed)
            print("|" + ile_spac_przed*" " + table[0][i] + ile_spac_po*" ", end = "")
        else:
            k = len(table[0][4])
            ile_spac_przed = int((size_lista[i]-k)/2)
            ile_spac_po = size_lista[i] - (k + ile_spac_przed)
            print("|" + ile_spac_przed*" " + table[0][i] + ile_spac_po*" " + "|")
    print("|" + size_lista[0]*"-" + "|" + size_lista[1]*"-" + "|"
             +size_lista[2]*"-" + "|" + size_lista[3]*"-" + "|" + size_lista[4]*"-" + "|")

    for i in range(len(table)):
        if table[i][0] == id_:
            for j in range(len(table[0])):
                if j < len(table[0])-1:
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
           

def update(table, id_, record):
    for i in range(len(table)):
        if table[i][0] == id_:
            for j in range(1,len(table[i])):
                if record[j] != "":
                    table[i][j] = record[j]
    data_manager.write_table_to_file("model/store/games.csv", table)
    return table
    

def delete(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            pointer = i
    del table[pointer]
    data_manager.write_table_to_file("model/store/games.csv", table)
    return table

# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    dictionary_of_manufacturers = {}
    set_of_manufacturers = set([])
    print(set_of_manufacturers)
    for i in range(1, len(table)):
        set_of_manufacturers.add(table[i][2])
    list_of_manufacturers = list(set_of_manufacturers)
    for item in list_of_manufacturers:
        counter = 0
        for j in range(1, len(table)):
            if table[j][2] == item:
                counter += 1
        dictionary_of_manufacturers[item] = counter
    return dictionary_of_manufacturers

def get_average_by_manufacturer(table, manufacturer):
    manufacture_str = manufacturer[0]
    counter = 0
    sum = 0.0
    for i in range(len(table)):

        if table[i][2] == manufacture_str:
            counter += 1
            sum += float(table[i][3])
            average_price = sum/counter
            result = str("{:04.2f}".format(average_price))
    return result

def calculate_age(born_str):
    import datetime
    born = datetime.datetime.strptime(born_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    return today.year - born.year -((today.month, today.day)<(born.month, born.day))

def get_oldest_game(table):
    list_of_oldest_games = []
    oldest_game = calculate_age(table[1][4])
    for i in range(2, len(table)):
        if  calculate_age(table[i][4]) > oldest_game:
            oldest_game = calculate_age(table[i][4])
    for j in range(1, len(table)):
        if calculate_age(table[j][4]) == oldest_game:
            list_of_oldest_games.append(table[j][1])
    list_of_oldest_games.sort()
    return list_of_oldest_games


def get_cheapest_game(table):
    title_price_list = []
    game_price = int(table[1][3])
    for i in range(1,len(table)):
        if int(table[i][3]) < game_price:
            game_price = int(table[i][3])
            game_title = table[i][1]
    title_price_list.append(game_price)
    title_price_list.append(game_title)
    return title_price_list


def get_age_by(title, table):
    print(title)
    for i in range(1, len(table)):
        if table[i][1] == title:
            age_game = calculate_age(table[i][4])
            return age_game


def get_game_by(keyword, table):
    keyword_str = keyword[0]
    list_of_games = []
    for i in range(1, len(table)):
        for j in range(len(table[0])):
            if table[i][j].find(keyword_str) != -1:
                list_of_games.append(table[i][1])
    return list_of_games
