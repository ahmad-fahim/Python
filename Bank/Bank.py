# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:10:24 2018

@author: fahim.ahmad
"""

# Lazy Buttons
# Demonstrates creating buttons
from tkinter import *

Account_name_list = []
Account_number_list = []



class Account_Display(Frame):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Account_Display, self).__init__(master)
        self.grid()
        self.display_account()
    
    def display_account(self):

        for acc_list in range(0, len(Account_number_list)):
            #print(Account_number_list[acc_list], Account_name_list[acc_list])
            Total_string = Account_number_list[acc_list]  + "\t" + Account_name_list[acc_list]
            #print(Total_string)
            
            #self.display_lbl = Label(self, text = Total_string) 
            
            label = Label(self, text = Total_string)
            label.grid(row = acc_list, column = 0, sticky = W)
             
        
    def Submit_action(self):

        Account_name_list.append(self.Acc_Name_ent.get())
        Account_number_list.append(self.Acc_number_ent.get())

class Deposit_screen(Frame):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Deposit_screen, self).__init__(master)
        self.grid()
        self.create_screen()
        
    def create_screen (self):
        self.Acc_number_lbl = Label(self, text = "Account Number : ") 
        self.Acc_number_lbl.grid(row = 1, column = 0, sticky = W)
        self.Acc_number_lbl.grid()
        self.Acc_number_ent = Entry(self)
        self.Acc_number_ent.grid(row = 1, column = 1, sticky = W)
        
        
        self.Acc_Name_lbl = Label(self, text = "Tran Amount : ") 
        self.Acc_Name_lbl.grid(row = 2, column = 0, sticky = W)
        self.Acc_Name_lbl.grid()
        self.Acc_Name_ent = Entry(self)
        self.Acc_Name_ent.grid(row = 3, column = 1, sticky = W)
        
        
        self.submit_bttn = Button(self, text = "Submit", command = self.Submit_action)
        self.submit_bttn.grid(row = 3, column = 0, sticky = W)
        
    def Submit_action(self):
        sub_action = Deposit_transaction()

class Deposit_transaction(Deposit_screen):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Deposit_transaction, self).__init__(master)
        self.grid()
        self.deposit_tran()
    
    def deposit_tran(self):
        None




class Withdraw_screen(Frame):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Withdraw_screen, self).__init__(master)
        self.grid()
        self.create_screen()
        
    def create_screen (self):
        self.Acc_number_lbl = Label(self, text = "Account Number : ") 
        self.Acc_number_lbl.grid(row = 1, column = 0, sticky = W)
        self.Acc_number_lbl.grid()
        self.Acc_number_ent = Entry(self)
        self.Acc_number_ent.grid(row = 1, column = 1, sticky = W)
        
        
        self.Acc_Name_lbl = Label(self, text = "Tran Amount : ") 
        self.Acc_Name_lbl.grid(row = 2, column = 0, sticky = W)
        self.Acc_Name_lbl.grid()
        self.Acc_Name_ent = Entry(self)
        self.Acc_Name_ent.grid(row = 3, column = 1, sticky = W)
        
        
        self.submit_bttn = Button(self, text = "Submit", command = self.Submit_action)
        self.submit_bttn.grid(row = 3, column = 0, sticky = W)
        
    def Submit_action(self):
        sub_action = Deposit_transaction()

class Withdraw_transaction(Deposit_screen):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Deposit_transaction, self).__init__(master)
        self.grid()
        self.deposit_tran()
    
    def deposit_tran(self):
        None














class Account_creator(Frame):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Account_creator, self).__init__(master)
        self.grid()
        self.create_account()
    
    def create_account(self):
        self.Acc_number_lbl = Label(self, text = "Account Number : ") 
        self.Acc_number_lbl.grid(row = 1, column = 0, sticky = W)
        self.Acc_number_lbl.grid()
        self.Acc_number_ent = Entry(self)
        self.Acc_number_ent.grid(row = 1, column = 1, sticky = W)
        
        
        self.Acc_Name_lbl = Label(self, text = "Account Name : ") 
        self.Acc_Name_lbl.grid(row = 2, column = 0, sticky = W)
        self.Acc_Name_lbl.grid()
        self.Acc_Name_ent = Entry(self)
        self.Acc_Name_ent.grid(row = 3, column = 1, sticky = W)
        
        
        
        
        self.submit_bttn = Button(self, text = "Submit", command = self.Submit_action)
        self.submit_bttn.grid(row = 3, column = 0, sticky = W)
        
    def Submit_action(self):

        Account_name_list.append(self.Acc_Name_ent.get())
        Account_number_list.append(self.Acc_number_ent.get())




class Bank_layout(Frame):
    ### A GUI application with three buttons. """
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Bank_layout, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_an_account(self):
        acc = Tk()
        acc.title("Account creation form")
        acc.geometry("400x400")
        acc_creat = Account_creator(acc)
        acc_creat.mainloop()
    def create_an_account_2(self):
        acc = Tk()
        acc.title("Account creation form")
        acc.geometry("400x400")
        acc_creat = Account_creator(acc)
        acc_creat.mainloop()
        
    def account_display(self):
        acc = Tk()
        acc.title("Account list Display")
        acc.geometry("400x400")
        acc_creat = Account_Display(acc)
        acc_creat.mainloop()
        
    def deposit_amount(self):
        acc = Tk()
        acc.title("Deposit Screen")
        acc.geometry("400x400")
        acc_creat = Deposit_screen(acc)
        acc_creat.mainloop()
        
    def Withdraw_amount(self):
        acc = Tk()
        acc.title("Deposit Screen")
        acc.geometry("400x400")
        acc_creat = Withdraw_screen(acc)
        acc_creat.mainloop()
        
        
        

    def create_widgets(self):
        # create first button
        self.bttn1 = Button(self, text = "Create a account")
        self.bttn1.grid()
        self.bttn1["command"] = self.create_an_account
        self.bttn1["command"] = self.create_an_account_2
        # create second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Deposit to an account")
        self.bttn2["command"] = self.deposit_amount
        # create third button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Withdraw from an account"
        self.bttn3["command"] = self.Withdraw_amount
        
        self.bttn4 = Button(self, text = "Display account")
        self.bttn4.grid()
        self.bttn4["command"] = self.account_display
        
# main
root = Tk()
root.title("My Bank")
root.geometry("400x400")
app = Bank_layout(root)

root.mainloop()