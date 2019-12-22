def get_table_from_file(file_name):
    row_line = []
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            row_line.append(line)
    all_table = []
    for i in range(len(row_line)):
        li = list(row_line[i].split(","))
        all_table.append(li)
    return all_table


def write_table_to_file(file_name, table):
    with open(file_name, "w") as f:
        for i in range(len(table)):
            for j in range(len(table[0])):
                if j < len(table[0])-1:
                    f.write(table[i][j] + ",")
                else:
                    f.write(table[i][j] + "\n")
    
    