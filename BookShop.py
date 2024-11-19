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
