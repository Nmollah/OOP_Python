class BookRentShop:
    def __init__(self,NoOfBook):
        self.book=NoOfBook


    def displayBook(self):
        print(self.book)


    def rentBook(self,q):

        if q<=0:
            print("Please enter a valid number")
        elif q>self.book:
            print("Please enter less the stock")
        else:
            self.book=self.book-q
            print("Total Price", q*10)
            print("Total No of stocks",self.book)

while True:
    shop1=BookRentShop(100)
    ui=int(input('''inter a input
    1 =Display Books Stocks
    2 =Rent Book
    3 = exit
    '''))
    if ui==1:
        print("Book in Store",shop1.displayBook())
    elif ui==2:
        n=int(input('Enter the number of book'))
        shop1.rentBook(n)
    else:
        break