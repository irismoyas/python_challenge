import os
import csv

print(os.path.abspath(__file__))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath=os.path.join("resources","election_data.csv")

total_votes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    cvs_header=next(csvreader)

    for row in csvreader:
        total_votes+=1
        if (row[2]=="Khan"):
            khan_votes +=1
        elif (row[2]=="Correy"):
            correy_votes +=1
        elif(row[2]=="Li"):
            li_votes +=1
        else:
            otooley_votes +=1
        
    kahn_percent=round((khan_votes/total_votes)*100,3)
    correy_percent=round((correy_votes/total_votes)*100,3)
    li_percent=round((li_votes/total_votes)*100,3)
    otooley_percent=round((otooley_votes/total_votes)*100,3)

winner=max(khan_votes,correy_votes,li_votes,otooley_votes)
if winner==khan_votes:
    winner_name="Khan"
elif winner==correy_votes:
    winner_name="Correy"
elif winner==li_votes:
    winner_name="Li"
else:
    winner_name="O'Tooley"

print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Kahn: {kahn_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print("---------------------------")
print(f"Winner: {winner_name}")
print("---------------------------")

f = open("election_results.txt", "w")
f.write("Election Results\n")
f.write("----------------------------\n")        
f.write(f"Total Votes:{total_votes} \n")
f.write("-----------------------------\n")
f.write(f"Kahn: {kahn_percent}% ({khan_votes})\n")
f.write(f"Correy: {correy_percent}% ({correy_votes})\n")
f.write(f"Li: {li_percent}% ({li_votes})\n")
f.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})\n")
f.write("----------------------------\n")
f.write(f"Winner: {winner_name}\n")
f.write("-----------------------------\n")
f.close()
