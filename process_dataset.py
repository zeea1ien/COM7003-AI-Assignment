import pandas as pd 



#checks if value can be converted into an integer
def check_is_int(value):
    try:
        int(value)
        return True
    except:
        return False
    
#removes duplicates and drops specified columns, handling empty lists properly
def clean_drop(dt):
    dt = dt.drop_duplicates()
    dt = dt.drop(["Motivation_Level", "Teacher_Quality", "Peer_Influence"],axis=1)

    dt['Hours_Studied'] = pd.to_numeric(dt['Hours_Studied'], errors='coerce')
    dt = dt.dropna(subset=['Hours_Studied'])

#removes rows where any column contains empty spaces
    dt = dt[~dt.isin(['[]']).any(axis=1)]
    #The dataset is equal to itself, but not rows that have blanks.
    #Tilde (~) represents "False" in Pandas (or "Not").
    #Literally, the above line means: dt is equal to itself but not blank rows.
    return dt

#should help converting categorical columns to numerical and save mapping files.
def normalise_boolean(dt):
    for column in dt.columns:
        unique_vals = []

        if not check_is_int(dt[column].iloc[0]):#check if first value is not an int
           unique_vals = dt[column].dropna().unique().tolist()
           dt[column] = dt[column].apply(lambda x: unique_vals.index(x)if x in unique_vals else None)
        else:
            dt[column] = dt[column].astype(int) #convert numeric columns properly

            #this section is just for experimenting purposes and maybe overkill 
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

                #saving the mapping file
    map_file = open("./maps/" + str(column) + "_map.txt", "w")
    for value in unique_vals:
            map_file.write(str(value) + "\n")
    map_file.close()

    dt = dt.reset_index(drop=True)
    dt.to_csv("./test.csv", index=False)

    return dt

# map data returns us a number (ADD MORE DETAILS TO THIS COMMENT )