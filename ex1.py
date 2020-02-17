a=10
def go():
    print("go")
class test:
    a=100
    def go():
        a=1000
        print("goes")
        print(a)
    def good(self):
            print("good")
go()
print(a)
test.go()
ob=test()
ob.good()
print(test.a)
print(ob.a)
    
