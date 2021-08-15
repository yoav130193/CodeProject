import pandas as pd
import numpy as np

class pandasExamples():
    def __init__(self):
        super().__init__()
        print('pandas')

    readFileName = 'data/FL_insurance_sample.csv'
    writeFileName = 'data/new_data.csv'

    def seriesExamples(self):
        print('hey series panda')
        a= pd.Series([1,2,3,4,'cool'])
        print(a)
        b = pd.Series([1,2,3,4,'cool'],index=['a','b','c','d','e'])
        print(b)
        c= pd.Series({'yoav': 1,'rinat': 2})
        print(c)
        print(c['yoav'])
        print(c[c>1])

    def dataFramesExamples(self):
        print('hey data frames panda')
        a = np.array([[1,2,3],[4,5,6]])
        df1 = pd.DataFrame(a)
        print(df1)
        s1 = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
        s2 = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
        print(s1)
        print(s2)
        df2 = pd.concat([s1,s2],axis=1)
        print(df2)
        df3 = pd.concat([s1, s2])
        print(df3)

    def one(self):
        mylist = list('abcedfghijklmnopqrstuvwxyz')
        print(mylist)
        self.seperator()
        myarr = np.arange(26)
        mydict = dict(zip(mylist, myarr))
        print(mydict)
        self.seperator()
        s1 = pd.Series(mylist)
        s2 = pd.Series(myarr)
        s3 = pd.Series(mydict)
        print(s1)
        self.seperator()
        print(s2)
        self.seperator()
        print(s3)
        self.seperator()
        df = pd.DataFrame(s3)
        print(df)

        self.seperator()
        df2 = s3.to_frame().reset_index()
        print(df2)
        self.seperator()

        df3 = pd.concat([s1, s2], axis=1)
        print(df3)
        self.seperator()

        self.writeFileName(df)

    def second(self):
        mylist = list('abcedfghijklmnopqrstuvwxyz')
        myarr = np.arange(26)
        mydict = dict(zip(mylist, myarr))
        s1 = pd.Series(mylist)
        s2 = pd.Series(myarr)
        s3 = pd.Series(mydict)
        df = pd.DataFrame(s3)
        print(df)
        self.writeFiles(df,self.writeFileName)
        self.readFiles(self.writeFileName)
    def seperator(self):
        print('--------')

    def readFiles(self,fileName):
        df = pd.read_csv(fileName)
        print(df.head())

    def writeFiles(self,df: pd.DataFrame,fileName):
        df.to_csv(fileName)