# If running python version earlier than 3.6 column order
# output will be random
import csv

f = open('license_trans.csv', errors="backslashreplace")
csv_f = csv.DictReader(f)

for row in csv_f:
    if row["Is valid match?"] == '?':
        print(row)
    if row["Is valid match?"] == 'N':
        print(row)

#    else:
#        print("null or unrecognized character")
print("Done")
