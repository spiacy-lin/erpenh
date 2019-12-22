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
    data_manager.write_table_to_file("model/selling/sellflow.csv", table)
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


def get_eplo_trans(table, id_emplo):
    strtym = id_emplo[0]
    emplo_tab = []
    for i in range(1,len(table)):
        if table[i][1] == strtym:
            emplo_tab.append(table[i])
    return emplo_tab    