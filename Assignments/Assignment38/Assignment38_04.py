import pandas as pd

from sklearn.model_selection import train_test_split

def main():

    DataFilePath="student_performance_ml.csv"  

    df=pd.read_csv(DataFilePath) 

    FirstFiveRecords=df.head()
    print("First 5 Records Are :\n",FirstFiveRecords)

    LastFiveRecords=df.tail()
    print("Last 5 Records Are :\n",LastFiveRecords)

    rows,columns=df.shape
    print(f"Total numbers of Rows: {rows}")
    print(f"Total numbers of Columns: {columns}") 

    print("Data Types of each column")
    print(df.dtypes) 

    # 2

    print("Total Number of Students:",rows)

    print("Students Passed:",(df['FinalResult']==1).sum())
    print("Students Failed:",(df['FinalResult']==0).sum())

    # 3
    print("Average StudyHours:",(df['StudyHours'].mean()))
    print("Average Attendence:",(df['Attendance'].mean()))
    print("Maximum PreviousScore:",(df['PreviousScore'].max()))
    print("Minimum SleepHours:",(df['SleepHours'].min()))

    # 4
    print("Passed and Failed Students:",df['FinalResult'].value_counts())

if __name__=="__main__":
    main()
