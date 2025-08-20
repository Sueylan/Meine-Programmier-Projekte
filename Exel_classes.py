import os, time, openpyxl

class Exel_spreedshet:
    def __init__(self,Exel_path):
        self.Exel_path = Exel_path
        self.wb = openpyxl.load_workbook(Exel_path)
    def Check_space(self,sheet):  # Checks where there is Space or if there is any space left
        self.sheet = sheet
        self.sheet = self.wb[sheet]
        return self.sheet.max_row
  
    def Add_user(self,Username,Password,sheet):  # Adds User in Exel Spreedshet
        self.sheet = self.wb[sheet]
        Row = self.sheet.max_row + 1
        self.Username = Username
        self.Password = Password
        self.sheet[f'A{Row}'] = Username
        self.sheet[f'B{Row}'] = Password
        self.sheet[f'C{Row}'] = 1000
        self.wb.save('Info Player spreedshet.xlsx')
    def Check_User(self,sheet,Username):   # Searches fo User in Exel with his Username
        self.Username = Username
        self.sheet = self.wb[sheet]
        self.Curent_Username = ""
        Number = int(self.sheet.max_row) 
        # Number = int(Number)
        while not self.Curent_Username == Username:
            for number in range(1,Number + 1):
                self.Curent_Username = str(self.sheet[f"A{str(number)}"].value)                      # PROBLEM Not finding Pablo
                if self.Username == self.Curent_Username:
                    self.Username = self.sheet[f'A{number}'].value 
                    self.Password = self.sheet[f'B{number}'].value 
                    self.Bank_acount = self.sheet[f'C{number}'].value 
                    self.User_info = [self.Username,self.Password,self.Bank_acount,number]
                    return self.User_info
            break
        self.User_info = ["Not found"]
        return self.User_info
    def Update_bank_acount(self,sheet,User_info):
        self.sheet = sheet
        self.sheet = self.wb[sheet]
        Row = self.User_info[3]
        self.Bank_acount = User_info[2]
        self.sheet[f'C{Row}'] = self.Bank_acount
        self.wb.save(str(self.Exel_path))
    def Save(self):
        self.wb.save(str(self.Exel_path))
    def Is_Spreedshet_open(self):
        try:
            # Attempt to open the file in read mode
            with open(self.Exel_path, 'r+'):
                return False  # File is not open elsewhere
        except IOError:
            return True  # File is open elsewhere or locked
        
"""  
             #   TEST          AREA
    
Casino_spreedshet = Exel_spreedshet("Info Player spreedshet.xlsx")

print(Casino_spreedshet.Check_User("UserInfo","Sueylan"))
print(Casino_spreedshet.Check_User("UserInfo","Pablo"))
print(Casino_spreedshet.Check_User("UserInfo","Xool"))

print(Casino_spreedshet.Check_space("UserInfo"))
Exel_path = "Info Player spreedshet.xlsx"
wb = openpyxl.load_workbook(Exel_path)
sheet = wb["UserInfo"]
print(sheet[f"A{str(3)}"].value)
"""
