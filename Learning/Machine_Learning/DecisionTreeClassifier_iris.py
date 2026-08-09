from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def main():
    iris_data=load_iris()

    X=iris_data.data
    Y=iris_data.target

    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

    model=DecisionTreeClassifier()

    model=model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    result=accuracy_score(y_test,y_pred)

    print("Accutracy is :",result*100)

if __name__=="__main__":
    main()