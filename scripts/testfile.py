import sys

#File input
fileInput = open('RawSequences_training.csv', "r")
#Seq count
count = 0
#sent count
sent = 1
#Output
fileOutput = open("Rawsequences_training{0}.fatsa".format(sent),"w")
#Loop through each line in the input file
print("Converting to FASTA...")
for strLine in fileInput:
    if(count>1000):
        fileOutput.close()
        count=1
        fileOutput = open("Rawsequences_training{0}.fatsa".format(sent), "w")
        sent=sent+1
    #Strip the endline character from each input line
    strLine = strLine.rstrip("\n")
    #Output the header
    fileOutput.write(">" + str(count) + "\n")
    fileOutput.write(strLine + "\n")
    count = count + 1
print ("Done.")
#Close the input and output file
fileInput.close()
fileOutput.close()
