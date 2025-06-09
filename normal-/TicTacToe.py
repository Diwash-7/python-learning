import random as r

def get_input ()  :                         # get inputs and return them

    # get computer input 

    options = [1,2,3]
    row = r.choice(options)
    col = r.choice(options)
    c_com = [row ,col]


    # get player input
    while True :
        try :
            p_row = int(input ("row: "))
            p_col = int(input ("col: "))
            
            if p_row in options and p_col in options :
                break
            else :
                print ("invalid! try btn (1,2,3)")
        except ValueError :
                print ("only numbers btn (1,2,3)")

    c_plr = [p_row,p_col]

    # return

    choices ={'plr':c_plr , 'com':c_com }
    return choices

val = get_input()
print (val)





    
    
    
    


