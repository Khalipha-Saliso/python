try:
    print(x)
except NameError:
    print("Variable x is not defined")    
#except:
    #print("Something went wrong")    
#finally:
    #print("The 'try except' is finished") 
else:
    print("Everything went wrong")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")           