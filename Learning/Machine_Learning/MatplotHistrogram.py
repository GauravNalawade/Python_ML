import matplotlib.pyplot as plt

def main():
    
    marks=[45,55,60,62.65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,                      #Continuous Data
        bins=5,                     # number of groups 
        edgecolor="black",          #Border color 
        alpha=0.8,                  #transperancy 
        rwidth=0.9,                 #relative width of bars 
    )

    plt.title("Marvellous Hostogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()


if __name__=="__main__":
    main()

