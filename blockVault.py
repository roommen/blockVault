import os
from coreLogic import splitFile

def clearScreen():
    cmd = "clear"
    os.system(cmd)

def printBanner():
    print("\t\t\t\t\t\t\t-----------------------------------------")
    print("\t\t\t\t\t\t\t|                                       |")
    print("\t\t\t\t\t\t\t|              BLOCK VAULT              |")
    print("\t\t\t\t\t\t\t|                                       |")
    print("\t\t\t\t\t\t\t-----------------------------------------")

def uploadVault():
    print("\n")
    filePath = input("Enter file name (with path) :: ")
    splitFile(filePath)
    print("split success")

def downloadVault():
    print("Download functionality")

def listVault():
    print("List Vault functionality")

def auditTrail():
    print("Audit Trail functionality")

def exit():
    print("Good bye!")

def printMenu():
    ans = True
    while ans:
        print("\t\t1. Upload to Vault")
        print("\t\t2. Download from Vault")
        print("\t\t3. List Vault Contents")
        print("\t\t4. View Audit Trail")
        print("\t\t5. Exit")
        ans = input("\n\t\tEnter your selection :: ")
        # print("you entered", ans)
        if int(ans) == 1:
            uploadVault()
        if int(ans) == 2:
            downloadVault()
        if int(ans) == 3:
            listVault()
        if int(ans) == 4:
            auditTrail()
        if int(ans) == 5:
            exit()
            ans = None


if __name__ == "__main__":
    clearScreen()
    printBanner()
    printMenu()