
# Our First Python Program | Anchingni Skangipa Python Program


# Game Title ko mesokani 
from time import sleep
print("*******########*******\n")
print("*******BRANCORE*******\n")
print("*******########*******\n")
print("*******Question*******")
print("**********&***********")
print("********Answer********\n")
print("# Rimchaksoa Sakantikon Angni singani aro Aganchakani GAME ona #\n")


# Game ni code

while ValueError: # While loop chi abachengenga aro Value Error ongama ongjama uko
    try:  # Try keyword ko onchengenga 
        q1 = input("(Computer)>> Nangni bimungko mai minga?\n\t(Na'a)>> ")
        if q1 == "":
            print("\n(Na'a Blank dona manjawa bimungko...)\n")
            raise ValueError
        print("Computer chanchienga......\n")
        sleep(2)
        print(f"(Computer)>> {q1}? Bimung silade :)\n")


        q2 = input("(Computer)>> Nangni chatchi ra mai?\n\t(Na'a)>> ")
        if q2 == "":
            print("\n(Na'a Blank dona manjawa Chatchiko...)\n")
            raise ValueError
        print("Computer chanchienga......\n")
        sleep(2)
        print(f"(Computer)>> {q2}? Oh na'aba {q2} rangsamo? Dakode chugimikde {q1} {q2} ..")

            

      
        q3 = int(input("(Computer)>> Na'a baita bilsi ongjok?\n\t(Na'a)>> "))
        if q3 < 13:
            print("Computer chanchienga......")
            sleep(2)
            print("(Computer)>> Na'ade chonkuaienga, teenager ba onkuja\n")        
        elif q3 < 18:
            print("Computer chanchienga......\n")
            sleep(2)
            print("(Computer)>> Na'ade teenager ongkuaienga")       
        elif q3 > 18:
            print("Computer chanchienga......\n")
            sleep(2)
            print("(Computer)>> Na'aba adult ongjokde dalajok... ")
   

        

           
        q4 = input("(Computer)>> Hai anching game kalna 1 aro 20 ona jebasi/random number ko chanchie nina.\nType 'kalgen' na'a kalgen ongode ongjaode type 'kaljawa' \n(Na'a)>> ")
        
        if q4 == "kalgen":
            import rand_num_game  
            rand_num_game.randy()
        elif q4 == "kaljawa":
            q4_1 = input("Ongkatgenok Game oni? Type 'hoe'| ongkatjaode type 'ongkatjawa' ")
            if q4_1 == "ongkatjawa":
                rand_num_game.randy()
            elif q4_1 == "hoe":
                break
            
        
            
    except:
        pass

