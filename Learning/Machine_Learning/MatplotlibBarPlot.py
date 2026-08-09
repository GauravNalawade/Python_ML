import matplotlib.pyplot as plt

def main():
    
    language=["C","c++","Java","Python"]
    students=[30,40,35,55]

    plt.bar(
        language,
        students,
        width=0.6,                      # width of bars
        edgecolor="black",              # border color of bars
        linewidth=1,                    # width of bar border
        alpha=0.8,                      # Transferemce 0.0 to 1.0
        label="Students",              # legend text
    )

    plt.title("Marvellous bar plot")

    plt.legend()

    plt.show()
if __name__=="__main__":
    main()

