username="lihleprecious"
password="abc1234"
attempt=3

while attempt> 0:
    user=input("enter username: ")
    pwd=input("enter password: ")

    if user == username and pwd == password:
        print("log in successful !")
        break
    else:
        attempt -=1      
        print(f"incorrect.you have {attempt} left")
        
    if attempt== 0:
        print("account locked. too many attemps")


