import pandas as pd
import matplotlib.pyplot as plt

def main():
    df=pd.read_csv("iris.csv")

    plt.hist(
        df['sepal length (cm)'],
        bins=10,
        color="skyblue",
        edgecolor="black",
        # rwidth=0.9
    )

    plt.title("Marvellous Histogram for IRIS")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")

    plt.show()


if __name__=="__main__":
    main()
