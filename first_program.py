
# Our First Python Program | Anchingni Skangipa Python Program

# Game Title ko mesokani 
from time import sleep
print("\t*******########*******\n")
print("\t********A'chik*******\n")
print("\t*******Computer*******\n")
print("\t*******Programmer*******\n")
print("\t*******########*******\n")
print("\t*******Question*******\n")
print("\t**********&***********\n")
print("\t********Answer********\n")
print("# Rimchaksoa Sakantikon Angni singani aro Aganchakani GAME ona #\n")



while ValueError: 
    try:  
        q1 = input("(Computer)>> Nangni bimungko mai minga?\n\t(Na'a)>> ")
        if q1 == "":
            print("\n(Na'a Blank dona manjawa bimungko...)\n")
            raise ValueError
        print("Computer chanchienga......\n")
        sleep(1)
        print(f"(Computer)>> {q1}? Bimung silade :)\n")


        q2 = input("(Computer)>> Nangni chatchi ra mai?\n\t(Na'a)>> ")
        if q2 == "":
            print("\n(Na'a Blank dona manjawa Chatchiko...)\n")
            raise ValueError
        print("Computer chanchienga......\n")
        sleep(1)
        print(f"(Computer)>> {q2}? Oh na'aba {q2} rangsamo? Dakode chugimikde {q1} {q2} ..\n")

            

      
        q3 = int(input("(Computer)>> Na'a baita bilsi ongjok?\n\t(Na'a)>> "))
        if q3 < 13:
            print("Computer chanchienga......\n")
            sleep(1)
            print("(Computer)>> Na'ade chonkuaienga, teenager ba onkuja\n")        
        elif q3 < 18:
            print("Computer chanchienga......\n")
            sleep(1)
            print("(Computer)>> Na'ade teenager ongkuaienga\n")       
        elif q3 > 18:
            print("Computer chanchienga......\n")
            sleep(1)
            print("(Computer)>> Na'aba adult ongjokde daljok...\n ")
        
        q4 = input("(Computer)>> Nangni Namnikbatsrangipa cha'ani ra mai?\n\t(Na'a)>> ")
        print(f"(Computer)>> {q4}? Anga antangba namnika uko.")

        q5 = input("(Computer)>> Nangni Hobby rang ra mairang?\n\t(Na'a)>>")
        print(f"(Computer)>> {q5}? Namaba, maiba hobby de dongna nanga oe ge'sa mangmangde")

        q6 = input("(Computer)>> Nangni namnikbatgipa Colour ra mai?\n\t(Na'a)>> ")
        print(f"(Computer)>> Atcha silaba colour. ")

        q7 = input("(Computer)>> Na'a mai ongna ska ba mai kamko ka'na ska?\n\t(Na'a)>> ")
        print(f"(Computer)>> {q7}? Namaba. Kam de antang namnika ansengakosa ka'na nanga. Gongeming aro sengeming poraibo\n")


        
        print("(Computer)>> Nangni Aganchakgimin data rangko chimongenga. Kasapae ontisa sengbo...\n")
        sleep(5)

        print("**********Nangni Aganchakgimin Data rang**********\n\t")    
        nangni_data = (f"""(Computer)>>\n
        Nangni chugimik bimungde {q1} {q2} onga.
        Na'a {q3} bilsi ongjok. Nangni namnikbatsrangipa cha'ani {q4} onga, 
        aro nangni namnikgipa colour de {q6} onga.
        Nangni ka'ana sikgipa kamde {q7} onga.  
        Mitella aganchakani na\n
        """)

        print(nangni_data)

        sleep(6)
        print("**********Number masieni? Game**********")

        q8 = input("""\n\t(Computer)>> Hai anching game kalna 1 aro 20 ona jebasi/random number ko chanchie nina.
        Type 'kalgen' na'a kalgen ongode ongjaode type 'kaljawa' \n\t(Na'a)>> """)
        
        if q8 == "kalgen":
            import rand_num_game  
            rand_num_game.randy()
        elif q8 == "kaljawa":
            q8_1 = input("\n\t(Computer)>>Ongkatgenok Game oni? Type 'hoe'| ongkatjaode type 'ongkatjawa' ")
            if q8_1 == "ongkatjawa":
                rand_num_game.randy()
            elif q8_1 == "hoe":
                break
            
        
            
    except:
        pass

