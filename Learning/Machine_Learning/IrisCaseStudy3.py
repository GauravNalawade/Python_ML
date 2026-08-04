from sklearn.datasets import load_iris


def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset=load_iris()

    # MetaData of dataset
    print("Independent variables are:")
    print(Dataset.feature_names)
    print("Length of Independent variable:",len(Dataset.feature_names))

    print("Dependent variables are:")
    print(Dataset.target_names)
    print("Length of Dependent variable:",len(Dataset.target_names))


if __name__=="__main__":
    main()