import pandas as pd 
import re 


class IrisData():
    missing_values = ["-", "--", "na", "NA", "n/a", "nan", "NaN", "null", "ng", "NG"]
    versicolor_pattern = r'versicolo'
    versicolor_regex = re.compile(versicolor_pattern, re.IGNORECASE)
    setosa_pattern = r'setosa'
    setosa_regex = re.compile(setosa_pattern, re.IGNORECASE)
    virginica_pattern = r'virginica'
    virginica_regex = re.compile(virginica_pattern, re.IGNORECASE)

    def __init__(self: object) -> None:
        self.df: pd.DataFrame = pd.read_csv("iris_with_errors.csv", na_values = self.missing_values)
        self.cleaned_df: pd.DataFrame = pd.read_csv("iris_with_errors.csv", na_values = self.missing_values)

    def clean_false_data(self: object) -> None:
        for index in self.df.index: 
            name = self.df['variety'][index]
            if not (0 <= self.df['sepal.length'][index] <= 15):
                self.cleaned_df.drop(index=index, inplace=True)

            if not (0 <= self.df['petal.length'][index] <= 15):
                self.cleaned_df.drop(index=index, inplace=True)

            if not (0 <= self.df['sepal.width'][index] <= 15):
                self.cleaned_df.drop(index=index, inplace=True)

            if not (0 <= self.df['petal.width'][index] <= 15):
                self.cleaned_df.drop(index=index, inplace=True)

            virginica_match = self.virginica_regex.search(name) 
            setosa_match = self.setosa_regex.search(name) 
            versicolor_match = self.versicolor_regex.search(name)
            
            if versicolor_match: 
                self.cleaned_df['variety'][index] = 'versicolor'
                self.df['variety'][index] = 'versicolor'
            elif setosa_match:
                self.cleaned_df['variety'][index] = 'setosa'
                self.df['variety'][index] = 'setosa'
            elif virginica_match:
                self.cleaned_df['variety'][index] = 'virginica'
                self.df['variety'][index] = 'virginica'
            else: 
                self.cleaned_df.drop(index=index, inplace=True)
    def clean_final_data(self: object) -> None:
        for index in self.df.index: 
            name = self.df['variety'][index]
            if not (0 <= self.df['sepal.length'][index] <= 15):
                self.df['sepal.length'][index] = self.countCleanedMedian('sepal.length')

            if not (0 <= self.df['petal.length'][index] <= 15):
                self.df['petal.length'][index] = self.countCleanedMedian('petal.length')

            if not (0 <= self.df['sepal.width'][index] <= 15):
                self.df['sepal.width'][index] = self.countCleanedMedian('sepal.width')

            if not (0 <= self.df['petal.width'][index] <= 15):
                self.df['petal.width'][index] = self.countCleanedMedian('petal.width')

            virginica_match = self.virginica_regex.search(name) 
            setosa_match = self.setosa_regex.search(name) 
            versicolor_match = self.versicolor_regex.search(name)
            
            if versicolor_match: 
                self.cleaned_df['variety'][index] = 'versicolor'
                self.df['variety'][index] = 'versicolor'
            elif setosa_match:
                self.cleaned_df['variety'][index] = 'setosa'
                self.df['variety'][index] = 'setosa'
            elif virginica_match:
                self.cleaned_df['variety'][index] = 'virginica'
                self.df['variety'][index] = 'virginica'
            else: 
                self.cleaned_df.drop(index=index, inplace=True)

    def countCleanedMedian(self: object, key: str) -> float:
        self.cleaned_df[key].median()

def main()-> None: 
    iris = IrisData()
    iris.clean_false_data()
    iris.clean_final_data()
    iris.df.to_csv("iris_cleaned.csv", index=False)
main()