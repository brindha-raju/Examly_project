EXAMLY RECRUITMENT DRIVE

ROUND -3

AIM: 

          To derive an algorithm for efficiently predicting the Coding skill score of a student in a particular Language with the given data.
          
PLATFORM USED:

•	Google Colab.
•	Anaconda prompt.

PROGRAMMING LANGUAGE USED:

•	Python

ALGORITHM:

STEP 1: Import pandas

STEP 2: Read the dataset that has been created earlier using .CSV format

STEP 3: Check for quality testing using head() function

STEP 4: Print the data frame  

STEP 5: Obtain the unique values of column SCORE and store it in the variable num_of_classes

STEP 6: Print the num_of_classes

STEP 7:  Generate descriptive statistics of the dataframe using describe() function

STEP 8: Split train input and output data whereas X is an train input data (except SCORE column) and Y is an train output data (only SCORE column).

STEP 9: print X and Y

STEP 10: import train_test_split library 

STEP 11: Split the dataframe into training (i.e 70% of data) and testing  (i.e 30%) sets

STEP 12: import pandas, matplotlib, numpy and linear model library files

STEP 13: Create the linear model and fit the trained data

STEP 14: Predict the test data and store it in Y_pred variable

STEP 15: Store the actual and predicted values to the dataframe

STEP 16: Print the dataframe 

EXPLANATION:
	First step of this project is to create the dataset for the parameters given in the question. The dataset has 18 columns  as given bellow 
•	Number of tests (eg: 3)
•	Score in each test (test1, test2, test3)
•	Number of questions attempted 
•	Programming language preferred (c, c++, java, python)
•	Number of learning videos viewed 
•	Number of practice test attempted 
•	Score in practice test
•	Number of student attended
•	Time taken to finish the test
•	Number of times compiled
•	Number of hints used
•	Number of questions correct
•	Number of questions wrong
•	Number of questions partially correct
•	Maximum mark obtained
•	Difficulty of the question

 


	Then I Imported pandas library and read the created dataset in .csv file formate.
 
	“df = pd.read_csv('/DATASET 2 (2).csv', error_bad_lines=False)” . In this line read_csv is used to import the data files from the system into python and load a comma separated files into dataframes. By giving the file path you can access the dataset you have created.
	By default invalid rows will raise an error, for example if my data has rows with too many values and if I try to load the data I get an error. To ignore those error lines error_bad_lines=False statement is used. If I specify this statement invalid rows are skipped.
	In next step quality testing is done using df.head() function. This function returns first n rows for the object based on position. It is useful for quality testing if the object has the right type of data in it.
	Print the dataframe using df.shape function which returns a tuple representing the dimensionality of the dataframe.
 


	To count all the unit values in the column SCORE and stored it in the variable ‘num_of_classes’ I have used len(df.SCORE.unique()) function .
 
	df.describe(): this function is used to generate descriptive statistics. Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN value.
	For numeric data the result index will include count, mean, std, min, max as well as lower, 50 and upper percentiles. By default the lower percentile is 25 and the upper percentile is 75. The 50 percentile is the same as the median.

 

	Next, the dataset has to be split into input and output data. For this purpose I have used df.drop(axis=0,column=[‘SCORE’]). This line is used to remove the column “SCORE” from the dataset and store the remaining data in the variable X which acts as an input data.
 
	Now, I have stored the removed “SCORE”column in Y variable which acts as an output data. Then I printed X and Y.
	train_test_split library file is imported to split the data into train and test sets. From the total dataset 70% of data is for training and 30% of data is for testing This can split an arrays or matrices into random train and test subsets.
	“X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)” in this line test size should be between 0.0 to 1.0 and represent the proportion of the dataset to include in the test split. Random_state is used to controls the shuffling applied to the data before applying the split.

 
	Finally pandas, numpy, matplotlib, linear model files were imported and created the linear model. Then stored the x test predicted values to the variable y_pred,
 
	At last the actual and predicted values of the students coding skill score is stored and printed.
 
 


