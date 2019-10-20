import os
from coreLogic import uploadCoreLogic, downloadCoreLogic

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
    # print("\n")
    filePath = input("\t\tEnter file name (with path) :: ")
    uploadCoreLogic(filePath)
    print("split success")

def downloadVault():
    # print("Download functionality")
    fileName = input("\t\tEnter file name :: ")
    downloadCoreLogic(fileName)

def listVault():
    print("\t\tListing the vault contents...")
    cmd = "aws s3 ls s3://inouthack6 | awk '{print $4}' | rev | cut -c 3- | rev"
    os.system(cmd)
    input()

def auditTrail():
    print("Audit Trail functionality")

def exit():
    print("\nGood bye!")

def printMenu():
    ans = True
    while ans:
        print("\t\t***********************")
        print("\t\t1. Upload to Vault")
        print("\t\t2. Download from Vault")
        print("\t\t3. List Vault Contents")
        print("\t\t4. View Audit Trail")
        print("\t\t5. Exit")
        print("\t\t***********************")
        print("\n")
        
        ans = input("\t\tMake your selection :: ")

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
