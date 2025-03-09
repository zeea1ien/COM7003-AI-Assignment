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
        if type(column[0]) != int: 
            for row in dt[column]:
                if row not in unique_vals and row != "":
                    unique_vals.append(row)
            row_index = 0
            #print(unique_vals)
            for row in dt[column]:
                dt.loc[row_index, column] = unique_vals.index(row)
                row_index += 1
    dt.to_csv("./test.csv")
    return dt