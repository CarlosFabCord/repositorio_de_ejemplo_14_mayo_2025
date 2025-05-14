import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class DataAnalyzer:
    def __init__(self, data):
        self.df=data
    def summary(self):
        print(self.df.info())
        print(self.df.describe())
    def missing_values(self):
        return self.df.isnull()
    def imprimir(self):
        print("Hola")

    def correlation_matrix(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        corr = self.df[numeric_cols].corr()
        plt.figure()
        sns.heatmap(corr, annot=True, cmap ="coolwarm")
        plt.title("Matriz de correlación")
        plt.show()

    def categorical_analisis(self):
        categorical_cols=self.df.select_dtypes(include="object").columns
        print(f"Las columnas categóricas son: {categorical_cols}")
        column = input("Digite la columna a visualizar: ")

        if column in categorical_cols:
            plt.figure()
            sns.countplot(data=self.df, x= column, order = self.df[column].value_counts().index)
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("La columna no es categórica o está mal escrita")