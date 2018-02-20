president_list=open("YearOfPresidentsCSV.csv", "r")

president_json={}
for line in president_list:
    split_line=line.split(",")
    president_json[split_line[0]]=split_line[1]

print president_json