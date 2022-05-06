# DSP-Exam4
The repository contains a python script titled 'Exam4.py' that loads a text file titled 'sampledna.txt'.
The user needs to update the reference file directory in the python script to match the github path or the local working path.
The script removes all characters from the file that are not A,T,C, or G. This includes spaces and non-alphanumeric characters.
The script is automated to recieve a variable number of lines in the input text file and to recieve a variable number of characters in each line. The input portion of the script calls functions to determine the possible number of kmers, observed number of kmers and calculates the linguistic complexity.
The possible number of kmers is calculated using the length (number of characters) in each line in the input text file. Integer arrays are then generated and used to calculate the length of the string minus k plus and 4^k. For all possible values of k for a single line, the minimum of these two variables is calculated to find the possible number.
Observed kmers are determined by seperating each line into a set of substrings. The substrings are then compared to find the number of unique substrings. Finally, this step is repeated for all possible values of k for a single line before continuing on to the next line.
The linguistic complexity is determined by finding the cumulative sum of possible and observed kmers for each line/string. The ratio of cumulative observed and possible kmers for each line is shown to be the linguistic complexity.
The described data is printed to the command line as dataframes and the dataframes are saved as txt files to the working directory. There are 6 output files, the linguistic complexity dataframes and files are seperated for simplicity.
