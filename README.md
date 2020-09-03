# python-challenge

Both the PyBank and PyPoll scripts were created using Python.

## PyBank
Task: Analyze financial records of a company over a time span. 

- The imported modules needed for the PyBank script were both os and csv.
- Paths were created with os.join for both the budget.data.csv and the pybank_analysis.txt file that would be used at the end.
- Empty lists were necessary before opening the files so they could be appended and iterated over once the csv was opened.
- Opening and reading the file using with open() ensured the file would automatically close after it is exhausted and using next() skipped the header row of the dataset.
- The first for loop was used to iterate over the rows of the dataset:
   - Two empty lists were appended here to find the total months and the total amount of profit and loss.
- The second for loop was used within a range to find the monthly change of profits and losses:
   - Since the first row would not have a change that needed to be calculated, the iterator started at 1 instead of 0.
   - An empty list was appended and the lists were turned to integers to find the difference by subtracting the rows from each other at 1 less index to assure months were being subtracted in order.
- Calucations were used within print statements instead of creating new variables and entered into the print statements to reduce the number of lines in the script.
   - To find the months with the greatest increase and decrease, .index() was used with the greatest increase and decrease amounts. Once the index was found, 1 was added to each to account for starting the range at 1. 
- A second file path was opened in order to created an output to write a text file with the results of the analysis:
   - Here writelines() was used to create one large statement instead of many writeline() statements.
   
   
## PyPoll
Task: Help a small, rural town modermize its vote counting process.

- Similarly, the imported modules needed for PyPoll were os and csv.
- Both of the paths for the election_data.csv, used for analysis, and the pypoll_analysis.txt, for results output, were created using os.join.
- Empty lists were created before opening the csv to be used with append to iterate over.
- A dictionary with candidate names as keys was created with the values set at 0 to start. This would be used later to count votes.
- The csv was opened using with open() and the header was skipped using next().
- With the csv opened in the read mode, the two empty lists were appended:
  - The first list was used to count total votes.
  - The second list was used with an index to only count how many votes each candidate received. 
- In order to count votes across all four candidates, a second for loop was used with Boolean logic if and elif statments:
  - Each candidate has a separate statement to ensure votes are not mixed up.
  - For each key in the counter, the counter increases by += 1 every time the value matches the candidates name for the respective candidates.
- After the votes are counted, each counter key is assigned to a new variable as an integer to calculate percentages:
  - First, all of the newly assinged integer variables are added together and assinged to a total votes variable.
  - Then, each candidates votes are divided by total votes and multiplied by 100 to find each respective percentage of votes. 
- For results to show on the terminal, print statement were used with the variables within calulations to reduce lines in the script. 
- The second file path is opened in order to print the results to a text file using writelines().
  
