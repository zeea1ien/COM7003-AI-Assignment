def check_is_int(value):
    try:
        int(value)
        return True
    except:
        return False

def clean_drop(dt):
    dt = dt.drop_duplicates()
    dt = dt.drop(["Motivation_Level", "Teacher_Quality", "Peer_Influence"],axis=1)
    #dt = dt.dropna()
    dt = dt[~dt.isin(['[]']).any(axis=1)]
    #The dataset is equal to itself, but not rows that have blanks.
    #Tilde (~) represents "False" in Pandas (or "Not").
    #Literally, the above line means: dt is equal to itself but not blank rows.
    return dt

def normalise_boolean(dt):
    for column in dt:
        unique_vals = []
        if check_is_int(column[0]) != True: 
            for row in dt[column]:
                if row not in unique_vals and row != "":
                    unique_vals.append(row)
            row_index = 0
            for row in dt[column]:
                dt.loc[row_index, column] = [unique_vals.index(row)]
                row_index += 1
        else:
            row_index = 0
            for row in dt[column]:
                dt.loc[row_index, column] = [int(row)]
                row_index += 1
        map_file = open("./maps/" + str(column) + "_map.txt", "w")
        for value in unique_vals:
            map_file.write(str(value) + "\n")
        map_file.close()
    dt = dt.reset_index(drop=True)
    dt.to_csv("./test.csv")
    return dt

# map data returns us a number (ADD MORE DETAILS TO THIS COMMENT )