import SlotMachine,random, os, time, sys, copy

from Exel_classes import Exel_spreedshet

"""
FUNCTIONS
"""
def Chose_optionInList(Options,Question):
    Selected_Index = 0
    User_input = 0
    while not User_input == "":
        print(Question)
        print("")
        for options in range(0,len(Options)):
            if options == Selected_Index:
                print(options + 1,Options[options],"<----")
            else:
                print(options + 1,Options[options]) 
        User_input = input()
        try:
            User_input = int(User_input)  
        except: 
            User_input = User_input
        if type(User_input) == int:
            if User_input < 0 or User_input > len(Options):
                os.system("cls")
                print(f"There is no option number {User_input}")
                time.sleep(1)
                os.system("cls")
            else :
                Selected_Index  = int(User_input) - 1
                os.system("cls")
        elif User_input == "":
            os.system("cls")
            return Options[Selected_Index]
        else:
            os.system("cls")
            print("You can't type that")
            time.sleep(1)

os.system("cls")

def Titel_screen(Titel,Bank_acount):
    """
    Rules
    """
    Slot_machine_rules = "SLOT MACHINE RULES:.\n" \
                         ".\n" \
                         "The Slot machine is a famous Casino machine based on luck.\n" \
                         "The machine spins three rows and if the line in the middle.\n" \
                         "all has the same symbol you win a prize based on what symbol.\n" \
                         "you got and what you bet.\n" \
                         ".\n" \
                         "Casino Lotten Version:.\n" \
                         ".\n" \
                         "Full line X = Bet * 5.\n" \
                         "Full line ? = Bet * random number betwen 2 and 14.\n" \
                         "Full line $ = Bet * 20.\n" \
                         "Full line * = Bet * 100(The Jackpot).\n"
    Black_Jack_rules = "BLACK JACK RULES\n" \
                       "\n" \
                       "Black Jack is a famous Casino Game where you play against the Dealer\n" \
                       "The Goal of the Game is to have a higher number than the Dealer but this\n" \
                       "cannot be higher than 21\n" \
                       "\n" \
                       "How it works\n" \
                       "\n" \
                       "At the Start of the round The Dealer will give you two cards with values betwen 2 and 10\n" \
                       "The Dealer will also take two cards but will show only one of his card\n" \
                       "Then the Dealer will ask you if you want to take another card(Hit) or stay with these cards(Stand)\n" \
                       "If you decide to hit the Dealer will give you another Card\n" \
                       "You can take as many cards as you want but if the Card Value is higher than 21 you losse\n" \
                       "If you decide to stand the Dealer will do the same thing you did The one who busted losses\n" \
                       "If you have a higher number than the Dealer you win and you get twice your bet\n" \
                       "If you have a lower number than the Dealer you loose your bet\n" \
                       "\n" \
                       "(Advice) 1.There are no aces in this game\n" \
                       "         2.The Dealer will stop taking cards if he has 17 points or more"

    
    """
    __________________________________________
    """
    Titel_scren = True
    while Titel_scren:
        print(Titel)
        print("To select press enter")
        print("Enter the coresponding number to chose the option")
        print("")
        print(f"Bank acount: {Bank_acount}")
        Activities_option = ["Games","Rules Book"]
        Chosen_activitie = Chose_optionInList(Activities_option,"")
        if Chosen_activitie == "Rules Book":
            Rules_options = ["Slot Machine","Black Jack"]
            Chosen_rules = Chose_optionInList(Rules_options,"Rules Book:")
            if Chosen_rules == "Slot Machine":
                print(Slot_machine_rules)
            elif Chosen_rules == "Black Jack":
                print(Black_Jack_rules)
            User_input = input("(t)itle screen")
            if User_input == "t":
                os.system("cls")
                continue
            else:
                os.system("cls")
                continue
        Game_options = ["Slot Machine","Black Jack"]
        Chosen_game = Chose_optionInList(Game_options,"Chose your game :")
        Titel_scren = False
    return Chosen_game
def Update_bank_acountM(Bank_acount,Username_info,Price):
    Old_bank_acount = copy.copy(Bank_acount)
    Bank_acount = Bank_acount + Price
    if not Username_info == "None":
        Username_info.pop(2) 
        Username_info.insert(2,Bank_acount)
        Casino_sheet.Update_bank_acount("UserInfo",Username_info)
    return Bank_acount
"""
___________________________MAIN GAME__________________________________________
"""
Titel = ("""   _____          _               _           _   _             
  / ____|        (_)             | |         | | | |            
 | |     __ _ ___ _ _ __   ___   | |     ___ | |_| |_ ___ _ __  
 | |    / _` / __| | '_ \ / _ \  | |    / _ \| __| __/ _ \ '_ \ 
 | |___| (_| \__ \ | | | | (_) | | |___| (_) | |_| ||  __/ | | |
  \_____\__,_|___/_|_| |_|\___/  |______\___/ \__|\__\___|_| |_|
                                                                
                                                                """)


Casino_sheet = Exel_spreedshet(r"C:\Users\sueyl\Desktop\Coding\Phyton\Project\Casino Lotten\Casino Lotten Files\Info Player spreedshet.xlsx")
Is_spreedshet_open = Casino_sheet.Is_Spreedshet_open()
if Is_spreedshet_open:
    print("The Exel File is open this will cause an Error")
    print("Please close the file and atempt to open the program again")
    sys.exit()
Log_in = False

while not Log_in:
    Acount_option = ["Yes","Im fine","I would like to make an acount"]
    User_input = Chose_optionInList(Acount_option,"Log in ?")
    if User_input == "Yes":
        Answered = False
        while not Answered :
            Username = input("Enter Username: ")
            os.system("cls")
            Username_info = Casino_sheet.Check_User("UserInfo",Username)
            if Username_info[0] == "Not found":
                print("User not found")
                User_input = Chose_optionInList(["Yes","No"],"Try again ?")
                if User_input == "No":
                    break
                else:
                    continue
            elif Username_info[0] == Username:
                Password = ""
                while not Password == Username_info[1]:
                    Password = input("Enter Password: ")
                    os.system("cls")
                    if Password == str(Username_info[1]):
                        Bank_acount = Username_info[2]
                        Answered = True
                        Log_in = True
                        break
                    else:
                        print("Wrong Password")
                        User_input = Chose_optionInList(["Yes","No"],"Try again ?")
                        if User_input == "Yes":
                            continue
                        else:
                            Answered = True
                            break
    if User_input == "Im fine":
        Bank_acount = 1000
        Username_info = "None"
        Log_in = True
    if User_input == "I would like to make an acount":
        Answered = False
        while Answered == False:
            Username = input("Username: ")
            Username_info = Casino_sheet.Check_User("UserInfo",Username)
            if Username_info[0] == "Not found":
                Password = input("Password: ") 
                os.system("cls")       
                Casino_sheet.Add_user(Username,Password,"UserInfo")
                Bank_acount = 1000
                Answered = True
            else:
                print("This Username already exists try again")
while True:
    Chosen_game = Titel_screen(Titel,Bank_acount)
    Bet_ready = False
    while not Bet_ready:
        try:
            Bet = int(input("Bet: "))
        except:
            print("You need to enter a number")
            time.sleep(1)
            os.system("cls")
            continue
        if Bet < 0:
            print("You can't enter this number")
            time.sleep(1)
            os.system("cls")
        elif Bet > Bank_acount:
            print("You don't have enough Money")
            time.sleep(1)
            os.system("cls")
        elif Bank_acount == 0:
            os.system("cls")
            print("You don't have enough Money")
            time.sleep(1)
            os.system("cls")
        elif Bet == 0:
            print("You can't bet nothing")
            time.sleep(1)
            os.system("cls")
        else:
            Bet_ready = True       
    if Chosen_game == "Slot Machine":   
        playing = True
        while playing:
            if Bank_acount - Bet < 0 or Bank_acount == 0:
                os.system("cls")
                print("You don't have enough money to play")
                time.sleep(1)
                os.system("cls")
                playing = False
                continue
            for i in range(9 ):
                Board = SlotMachine.create_board()
                SlotMachine.display_machine(Board)
                time.sleep(0.5)
                if not i == 8:
                    os.system("cls")
                else:
                    Price = SlotMachine.check_answer(Board,Bet)
                    Old_bank_acount = copy.copy(Bank_acount)
                    Bank_acount = Bank_acount + Price
                    if not Username_info == "None":
                        Username_info.pop(2) 
                        Username_info.insert(2,Bank_acount)
                        Casino_sheet.Update_bank_acount("UserInfo",Username_info)
                    if Bank_acount < Old_bank_acount:
                        print(f"You lost {Price}$")
                    else:
                        print(f"You won {Price}$")
                
                    User_input = ""
                    while not User_input == ["k","q","t"]:
                        print(f"Bank acount: {Bank_acount}")
                        User_input = input("(k)eep playing (q)uit (t)itel screen\n")
                        if User_input == "q":
                            sys.exit(0)
                        elif User_input == "k":
                            break
                        elif User_input == "t":
                            playing = False
                            os.system("cls")
                            break
                        else:
                            print("Command Uknown")
    if Chosen_game == "Black Jack":
        Black_jack = True 
        while Black_jack == True:
            os.system("cls")
            Player_turn = True 
            Dealer = [random.randint(2,10)]
            Player = [random.randint(2,10)]
            Player_points = int(Player[0])
            Player_string = str(Player[0])
            Dealer_points = int(Dealer[0])
            Dealer_string = str(Dealer[0])
            Dealer_turn = True
            while Player_turn:
                
                print(f"Dealer: {Dealer[0]} ?\n")
                print(f"Player: {Player_string}")
                User_input = Chose_optionInList(["Hit","Stand"],"")
                if User_input == "Hit":
                    Player.append(random.randint(2,10))
                    Player_points = Player_points + int(Player[len(Player) -1])
                    Player_string = Player_string + f" {str(Player[len(Player) -1 ])}"
                    if Player_points > 21:  
                        Dealer_turn = False 
                        print(f"Dealer: {Dealer[0]} ?\n")
                        print(f"Player: {Player_string}")          
                        print("\nBUST")
                        Price = Bet - Bet*2
                        Bank_acount = Update_bank_acountM(Bank_acount,Username_info,Price)
                        print(f"\nYou lost {Price}")
                        print(f"Bank acount: {Bank_acount}")    
                        User_input = Chose_optionInList(["Keep playing","Quit","Title Screen"],"")
                        if User_input == "Keep playing":
                            Player_turn = False 
                            break
                        elif User_input == "Quit":
                            sys.exit()
                        else:
                            Black_jack = False
                            break
                else:
                    Player_turn = False
                    break
            
            
            while Dealer_turn: 
                if Dealer_points >= 17:
                    print(f"Dealer: {Dealer_string}\n")
                    print(f"Player: {Player_string}")
                    if Dealer_points > 21:
                        print("The Dealer Busted")
                        print("You won",Bet*2)
                        Price = Bet*2
                    else:
                        print("The Dealer Stands\n")
                        if Dealer_points < Player_points:
                            print("You won",Bet*2)
                            Price = Bet*2
                        elif Dealer_points == Player_points:
                            Price = 0
                            print("Nobody won")
                        else:
                            Price = Bet - Bet*2
                            print("The Dealer Won\n")
                            print(f"You lost {Bet}")

                    Bank_acount = Update_bank_acountM(Bank_acount,Username_info,Price)
                    print(f"Bank acount: {Bank_acount}")
                    User_input = Chose_optionInList(["Keep playing","Quit","Title Screen"],"")
                    if User_input == "Keep playing":
                        Dealer_turn = False 
                        break
                    elif User_input == "Quit":
                        sys.exit()
                    else:
                        Black_jack = False
                        break    
                print("The Dealer takes another Card")
                Dealer.append(random.randint(2,10))
                Dealer_string = Dealer_string = Dealer_string + f" {str(Dealer[len(Dealer) -1 ])}"
                Dealer_points = Dealer_points + int(Dealer[len(Dealer) -1])
                print(f"Dealer: {Dealer_string}\n")
                print(f"Player: {Player_string}")
                time.sleep(4)
                os.system("cls")