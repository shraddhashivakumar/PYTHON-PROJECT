import csv
import textwrap
from prettytable import PrettyTable


LOGGEDINUSER = ''

def validate(password):
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(password) < 6:
        print('Password length should be at least 6')
        val = False
          
    if len(password) > 20:
        print('Password length should be not be greater than 20')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return True
        

def write(name,password,address):
    f = open("signin.csv", "a",newline="")
    det = [name,password,address]
    write = csv.writer(f)
    write.writerow(det)
    f.close()


def chk(name,password=None):
    f = open("signin.csv","r")
    read = csv.reader(f)
    for i in read:
        if i == []:
            pass
        else:
            if i[0] == name and password == None:
                return 1
            if i[0] == name and i[1] == password:
                return 2
    else:
        return 0
    f.close()


#creating a new account
def username_pass():
    global LOGGEDINUSER
    f = open("signin.csv","r")
    read = csv.reader(f)
    f.close()
    name = input("Enter your username: ")
    if chk(name) == 1:
        print("Already exists.create a new account")
        username_pass()
    else:
        while True :
            password = input("Enter password: ")
            goodpass = validate(password)
            if goodpass: break 
        reenterpassword = input("Enter password again:")
        if reenterpassword == password:
            address = input("Enter your address:")
            write(name, password, address)
            LOGGEDINUSER = name
            return True
        else:
            print("Your passwords do not match. Please try again.")
            username_pass()
        


#signing in
def sign_in(times):
    global LOGGEDINUSER
    name = input("Enter your username: ")
    passwd = input("Enter your password: ")
    if chk(name,passwd) == 2:
        print('Logging in as',name,'....')
        LOGGEDINUSER = name
        return True 
    else:
        if times < 3:
            print("Your username or password is incorrect. Please try again.")
            sign_in(times+1)
        else:
            print("You've exceeded the number of attempts. Try again later.")
            return False
                

#adding records to the csv file    

def adding():

    # open the file, read the contents
    oFile = open("book.csv", "r", newline='')
    oContents = list(csv.reader(oFile))

    nRows = len(oContents)
    print("Number of rows in the file is " + str(nRows))
    oFile.close()
    sBookname = input("Enter the name of the book: ")
    sBookname = sBookname.lower().strip()

    bMatchFound = False

    if sBookname != "":
       
        for i in range(nRows):
            if sBookname == oContents[i][0].lower().strip():
                # we found a match
                bMatchFound = True
        
                # accept review
                sReview = input("Enter your review: ")

                oContents[i][7] = oContents[i][7].replace(oContents[i][7], oContents[i][7] + " | " + sReview)
                break
            
    if bMatchFound == False:
       
        sAuthor = input("Enter the name of the author: ")
        nRating = float(input("Rating of the specified book: "))
        sGenre = input("Genre of the specified book: ")
        sReview = input("Review of the specified book: ")
        nPages = input("Enter the number of pages: ")
        nCost = 0
        nStock = 0
        oContents.append([sBookname, sAuthor, nRating, sGenre, nPages, ncost,nstock, sReview])

        
    oFile = open("bookrev.csv", "w", newline='')
    oWrite = csv.writer(oFile)
    oWrite.writerows(oContents)

    oFile.close()

    if bMatchFound:
        print("The review has been added successfully! Thank you for your feedback!")
    else:
        print("The book entry and review have been added successfully! Thank you for your feedback!")



    
def reading():
    f = open("book.csv","r")
    csv_r = csv.reader(f)
    read = list(csv_r)
    book = input("Enter name of the book :")
    pt_det = []
    alldet = []
    sno = 0
    for i in read:
        if i == []:
            pass
        elif book.lower() in i[0].lower():
            sno = sno+1
            alldet.append([sno,i[7],i[1],i[3],i[2],i[4]])
            pt_det.append([sno,i[0],i[1]])
            table = PrettyTable(['SNo','Books','Author'])
            table.add_rows(pt_det)


    if not pt_det:
        print("No book matching name is available")
        reading() 
    else:
        print(table)
        while True:
            try:
                aski = int(input("Enter the sno of the book you want to see review for:"))
            except ValueError:
                print('Enter a valid number')
            else:
                if 1 <= aski <= sno:
                    break
                else: print('Your number is invalid')        

        for i in alldet:
            if aski == i[0]:
                print("Review:")
                for line in (textwrap.wrap(i[1], width = 50)):
                    print (line)
                print(" ")
                print("AUTHOR: ",i[2])
                print(" ")
                print("GENRE: ",i[3])
                print(" ")
                print("RATING: ",i[4])
                print(" ")
                print("NUMBER OF PAGES: ",i[5])
                print(" ")
           
    f.close()


# reading a review by the authors name
def author():
    f = open("book.csv","r",newline = "")
    read = csv.reader(f)
    L = list(read)
    name_author = input("Enter the name of the author: ")
    A = []
    new_L=[]
    sno = 0
    for i in L:
        if i == []:
            pass
        elif name_author.lower() in i[1].lower():
            sno = sno+1
            new_L.append([sno,i[7],i[1],i[3],i[2],i[4]])
            A.append([sno,i[0],i[1]])
            table = PrettyTable(['SNO','BOOKS','AUTHOR'])
            table.add_rows(A)
            
            
    if not A:
        print("No such author found.")
        author()
    else:
        print(table)
        while True:
            try:
                aski = int(input("Enter the sno of the book you want to see review for:"))
            except ValueError:
                print('Enter a valid number')
            else:
                if 1 <= aski <= sno:
                    break
                else:
                    print('Your number is invalid')
                
        for i in new_L:
            if aski == i[0]:
                print("Review:")
                for line in (textwrap.wrap(i[1], width = 50)):
                    print (line)
                print(" ")
                print("AUTHOR: ",i[2])
                print(" ")
                print("GENRE: ",i[3])
                print(" ")
                print("RATING: ",i[4])
                print(" ")
                print("NUMBER OF PAGES: ",i[5])
                print(" ")
           
    f.close()

# reading review by genre
def genre():
    f = open("book.csv","r",newline = "")
    read = csv.reader(f)
    L = list(read)
    genre = input("Enter the genre of the book : ")
    A = []
    new_L=[]
    sno = 0
    for i in L:
        if i == []:
            pass
        if genre.lower() in i[3].lower():
            sno = sno+1
            new_L.append([sno,i[7],i[1],i[3],i[2],i[4]])
            A.append([sno,i[0],i[1],i[3]])
            table = PrettyTable(['SNO','BOOKS','AUTHOR','GENRE'])
            table.add_rows(A)
    if not A:
        print("No books with the given genre found.")
        genre()
    else:
        print(table)
        while True:
            try:
                aski = int(input("Enter the sno of the book you want to see review for:"))
            except ValueError:
                print('Enter a valid number')
            else:
                if 1 <= aski <= sno:
                    break
                else: print('Your number is invalid')        
        for i in new_L:
            if aski == i[0]:
                print("Review:")
                for line in (textwrap.wrap(i[1], width = 50)):
                    print (line)
                print(" ")
                print("AUTHOR: ",i[2])
                print(" ")
                print("GENRE: ",i[3])
                print(" ")
                print("RATING: ",i[4])
                print(" ")
                print("NUMBER OF PAGES: ",i[5])
                print(" ")
           
    f.close()

def ask_o():
    yorn = input("Do you want to read a review of any book?(yes/no): ")
    if yorn.lower() == 'yes':
        return 1
    elif yorn.lower() == 'no':
        print("Okay, Thank you!")
    else:
        print("Enter yes or no.")
        ask_o()
        

#displaying the top ten books.
def topten():
    f = open("book.csv")
    read = csv.reader(f)
    L = list(read)
    A = []
    new_L = []
    sno1 = 0
    sno = 0
    for i in L:

        if i == []:
            pass

        else:
            a = i[0]
            b = i[1]
            c = i[2]
            A.append([a,b,c])
            new_L.append([i[1],i[7],i[2],i[3],i[4]])
            
    def rate(A):
            return A[2]
    def ratin(new_L):
            return new_L[2]    
    
    A.sort(key=rate,reverse = True)
    new_L.sort(key = ratin,reverse=True)    
    l1 = A[1:11]
    l2 = new_L[1:11]
    for i in l1:
        sno1+=1
        i.insert(0,sno1)

    for i in l2:
        sno+=1
        i.insert(0,sno)

    for i in range(len(l1)):
        table = PrettyTable(['SNO','BOOKNAME','AUTHOR','RATING'])
        table.add_rows(l1)

    print("            - T O P  T E N  B O O K S - ")
    print(table)
    result = ask_o()
    if result == 1:
        while True:
            try:
                aski = int(input("Enter the sno of the book you want to see review for:"))
            except ValueError:
                print('Enter a valid number')
            else:
                if 1 <= aski <= sno:
                    break
                else: print('Your number is invalid')        

        for i in l2:
            if aski == i[0]:
                print("Review:")
                for line in (textwrap.wrap(i[2], width = 50)):
                    print (line)
                print(" ")
                print("AUTHOR: ",i[1])
                print(" ")
                print("GENRE: ",i[4])
                print(" ")
                print("RATING: ",i[3])
                print(" ")
                print("NUMBER OF PAGES: ",i[5])
                print(" ")
    
    f.close()


def account():
    yor = input("ALREADY HAVE A ACCOUNT? (yes/no): ")

    if yor == 'yes' or yor == 'y':
        times = 1
        if not sign_in(times): account()

    elif yor == 'no' or yor=='n':
        username_pass()
    else:
        print("Please enter yes or no.")
        account()

# Buying a book
def buying():
    g = open("book.csv",'r',newline='')
    cost = list(csv.reader(g))
    g.close()
    bname = input("Enter the name of the book you want to buy: ")
    sno = 0
    table = PrettyTable()
    table.field_names = ['SNO','BOOK', 'AUTHOR', 'RATING', 'COST(in Rs)']
    L = []
    stock = []
    for i in cost[1:]:
        if i ==[]:
            continue
        elif bname.lower() in i[0].lower():
            sno = sno + 1
            L.append([sno,i[0],i[1],i[2],i[5]])
            stock.append([sno,i[6]])
    table.add_rows(L)
    if not L:
        print("No book matching name is available")
        buying()    
    else:
        print(table)
        while True:
            try:
                aski = int(input("Enter the sno of the book you want to buy:"))
            except ValueError:
                print('Enter a valid number')
            else:
                if 1 <= aski <= sno:
                    break
                else: print('Your number is invalid')        

        for k in stock:
            if aski == k[0]:
                if int(k[-1]) > 0:
                    for i in L:
                        if aski == i[0]:
                            print(" ")
                            print("-DETAILS-")
                            print(" ")
                            print("Name:",i[1])
                            print("Author:",i[2])
                            print("Rating:",i[3])
                            print("Total Cost: ",i[4])
                            print(" ")
                            print("Thank you,the book will be delivered as per the shipment date.")
                            m = open('book.csv','w',newline='')
                            for j in cost:
                                if j[0] == i[1]:
                                    j[6] = int(j[6]) - 1
                                    break 
                            c = csv.writer(m)
                            c.writerows(cost)
                            m.close()
                            break
                else:
                    print("Sorry, the book is out of stock")



def menu():
    global LOGGEDINUSER
    while True:
        if not LOGGEDINUSER:
            print('''

            ====================| WELCOME TO SNS BOOKREVZZ |=====================
            ''')
            account()
        print('''

        ====================| SNS BOOKREVZZ MENU |=====================
                            1. BUY A BOOK
                            2. READ A REVIEW BY THE BOOK NAME.
                            3. READ A REVIEW BY THE AUTHOR NAME.
                            4. READ A REVIEW BY GENRE
                            5. ADD A BOOK.
                            6. THE TOP TEN BOOKS.
                            7. LOGOUT
                            8. EXIT
        ''')
        
        choice = input("YOUR CHOICE? (1/2/3/4/5/6/7/8): ")
        if choice == '1':
            buying()

        elif choice=='2':
            reading()

        elif choice == '3':
            author()

        elif choice == '4':
            genre()

        elif choice=='5':
            adding()

        elif choice == '6':
            topten()

        elif choice == '7':
            print("Logging out",LOGGEDINUSER,"...")
            LOGGEDINUSER = ''

        elif choice == '8':
            print("Thank you for visiting,! Hope to better our services next time :D")
            break
        else:
            print("Enter a valid number.")          

menu()



    
