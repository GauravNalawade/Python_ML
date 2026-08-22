import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    # Step 1: Load Dataset
    df=pd.read_csv("Mall_Customers.csv")

    print("Data Loaded Successfulyy")
    print(df.head())

    print("Missing values :")
    print(df.isnull().sum()) 

    # Step 2: Feature Selection
    X=df[["AnnualIncome","SpendingScore"]]

    print("Selected Features: ")
    print(X.head())

    # Step 3: Scale the Data
    scalar=StandardScaler()

    X_Scaled=scalar.fit_transform(X)

    print("Scaled Data:")
    print(X_Scaled[:5])

    # step4 :elbow method
    WCSS=[]

    for k in range(1,11):
        model=KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_Scaled)

        WCSS.append(model.inertia_)
    print("Values of WCSS :")
    for i in range(len(WCSS)):
        print(f"{i+1}:{WCSS[i]}")

    # step 5:Visulalize data
    plt.plot(
        range(1,11),
        WCSS,
        marker="o"
    )
    plt.xlabel("Number of cluster:k")
    plt.ylabel("WCSS")
    plt.title("Marvellous")
    plt.grid(True)
    plt.show()

    # step 6
    model=KMeans(
                n_clusters=4,
                random_state=42,
                n_init=10
                )

    clusters=model.fit_predict(X_Scaled)

    df["Clusters"]=clusters
    print("Dataset with clusters:")
    print(df.head(100)) 

if __name__=="__main__":
    main()