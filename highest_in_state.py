import csv


def highest_in_state(state):
    """
    Returns the name and cost of the most expensive university in state

    We're using the TUITIONFEE_IN field as cost and INSTNM as the school
    name.

    Be careful on data types on this one. 
    """

    with open('university-data.csv', newline='') as csvfile:
        csv_file = csv.DictReader(csvfile)
        highestTuition = 0
        highestSchool = ""
        for row in csv_file:
            if(row['STABBR']==state):
                if(row['TUITIONFEE_IN']!="-"):
                    if(int(row['TUITIONFEE_IN'])>highestTuition):
                        highestTuition = int(row['TUITIONFEE_IN'])
                        highestSchool = row['INSTNM']
        return highestTuition,highestSchool
    return None
