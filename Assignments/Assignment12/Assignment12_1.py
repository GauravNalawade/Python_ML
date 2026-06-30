def CheckVowel(Chr):
    if Chr=='a'or Chr=='e'or Chr=='i'or Chr=='o'or Chr=='u'or Chr=='A' or Chr=='E'or Chr=='I'or Chr=='O' or Chr=='U' :
        return True
    else:
        return False


def main():
    print("Enter Character")
    ch=input()

    Ret=CheckVowel(ch)

    if(Ret==True):
        print("Vowel")
    else:
        print("Constant")



if __name__=="__main__":
    main()