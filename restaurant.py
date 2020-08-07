from tkinter import *
import random
import datetime
from tkinter import messagebox
import os

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Restaurant Billing Sotware")
        bgcolor = "#223A2A"
        title = Label(self.root, text="Restaurant Billing Software", bd=12, relief=GROOVE, bg=bgcolor, fg="white",
                      font=("algerian", 30, "bold"), pady=2).pack(fill=X)
        self.root.wm_iconbitmap("favicon.ico")

        # +++++++++++++ Per unit price of items +++++++++++

        self.uchicken = 150
        self.ubuff = 140
        self.uveg = 130
        self.ucjhol = 160
        self.ucfry = 180
        self.uvfry = 150
        self.ubfry = 160
        self.upaneer = 200
        self.ugreen = 180
        self.ufish = 210
        self.ucheese = 170
        self.ukothe = 175
        self.uchilly = 180
        self.uwheat = 150
        self.ucoke = 50
        self.ufanta = 50
        self.usprite = 50
        self.udew = 40
        self.ulitchi = 40
        self.ufrooty =45
        self.upepsi = 55

        # ================== Variables ++++++++++++++++++++

        self.chicken = IntVar()
        self.buff = IntVar()
        self.veg = IntVar()
        self.cjhol = IntVar()
        self.cfry = IntVar()
        self.bfry = IntVar()
        self.vfry = IntVar()
        self.paneer = IntVar()
        self.fish = IntVar()
        self.green = IntVar()
        self.cheese = IntVar()
        self.kothe = IntVar()
        self.chilly = IntVar()
        self.wheat = IntVar()
        self.Coke = IntVar()
        self.Fanta = IntVar()
        self.Sprite = IntVar()
        self.Dew = IntVar()
        self.Litchi = IntVar()
        self.Frooty = IntVar()
        self.Pepsi = IntVar()

        # ===================== Total item price  +++++++++++++++++++

        self.Total_momo = StringVar()
        self.Total_cd = StringVar()
        self.Service_charge = StringVar()
        self.Total_pay = StringVar()

        # +++++++++++++++++ customer details variables ++++++++++++++++

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        xt = random.randint(10000, 99999)
        self.bill_no.set(str(xt))
        self.search_bill = StringVar()

        # +++++++ customer detail frame +++++++++++

        f1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1, width=20, textvariable=self.c_name, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                column=1,
                                                                                                                pady=5,
                                                                                                                padx=10)

        cphone_lbl = Label(f1, text="Phone Number", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(f1, width=20, textvariable=self.c_phone, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  pady=5,
                                                                                                                  padx=10)

        cbill_lbl = Label(f1, text="Bill Number", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1, width=20, textvariable=self.search_bill, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(f1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=60,
                                                                                                                pady=10)
        # +++++++++++Momo frame +++++++++++++

        f2 = LabelFrame(self.root, text="MOMO Items", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f2.place(x=5, y=185, width=665, height=430)

        Chicken_lbl = Label(f2, text="Chicken Steamed", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        Chicken_txt = Entry(f2, width=10, textvariable=self.chicken, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Buff_lbl = Label(f2, text="Buff Steamed", font=("times new roman", 16, "bold"), bg=bgcolor,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Buff_txt = Entry(f2, width=10, textvariable=self.buff, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Veg_lbl = Label(f2, text="Veg Steamed", font=("times new roman", 16, "bold"), bg=bgcolor,
                              fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Veg_txt = Entry(f2, width=10, textvariable=self.veg, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        ChickenJhol_lbl = Label(f2, text="Chicken Jhol", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        ChickenJhol_txt = Entry(f2, width=10, textvariable=self.cjhol, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        ChickenFry_lbl = Label(f2, text="Chicken Fried", font=("times new roman", 16, "bold"), bg=bgcolor,
                             fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ChickenFry_txt = Entry(f2, width=10, textvariable=self.cfry, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        BuffFry_lbl = Label(f2, text="Buff Fried", font=("times new roman", 16, "bold"), bg=bgcolor,
                           fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        BuffFry_txt = Entry(f2, width=10, textvariable=self.bfry, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        VegFry_lbl = Label(f2, text="Veg Fried", font=("times new roman", 16, "bold"), bg=bgcolor,
                          fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        VegFry_txt = Entry(f2, width=10, textvariable=self.vfry, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        Paneer_lbl = Label(f2, text="Paneer MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="lightgreen").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        Paneer_txt = Entry(f2, width=10, textvariable=self.paneer, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)

        Fish_lbl = Label(f2, text="Fish MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                         fg="lightgreen").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        Fish_txt = Entry(f2, width=10, textvariable=self.fish, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)

        Green_lbl = Label(f2, text="Green MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                        fg="lightgreen").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        Green_txt = Entry(f2, width=10, textvariable=self.green, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        Cheese_lbl = Label(f2, text="Cheese MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                                fg="lightgreen").grid(row=3, column=2, padx=10, pady=10, sticky="w")
        Cheese_txt = Entry(f2, width=10, textvariable=self.cheese, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3, column=3, padx=10, pady=10)

        Wheat_lbl = Label(f2, text="Wheat MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                               fg="lightgreen").grid(row=4, column=2, padx=10, pady=10, sticky="w")
        Wheat_txt = Entry(f2, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=4, column=3, padx=10, pady=10)

        Kothe_lbl = Label(f2, text="Kothe MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                            fg="lightgreen").grid(row=5, column=2, padx=10, pady=10, sticky="w")
        Kothe_txt = Entry(f2, width=10, textvariable=self.kothe, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=3, padx=10, pady=10)

        Chilly_lbl = Label(f2, text="Chilly MOMO", font=("times new roman", 16, "bold"), bg=bgcolor,
                           fg="lightgreen").grid(row=6, column=2, padx=10, pady=10, sticky="w")
        chilly_txt = Entry(f2, width=10, textvariable=self.chilly, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=6, column=3, padx=10, pady=10)



        # ++++++++++++ Cold Drinks frame ++++++++++++++

        f4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f4.place(x=675, y=185, width=325, height=430)

        Coke_lbl = Label(f4, text="Coke", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        Coke_txt = Entry(f4, width=10, textvariable=self.Coke, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Fanta_lbl = Label(f4, text="fanta", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Fanta_txt = Entry(f4, width=10, textvariable=self.Fanta, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Sprite_lbl = Label(f4, text="Sprite", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Sprite_txt = Entry(f4, width=10, textvariable=self.Sprite, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Dew_lbl = Label(f4, text="Mountain Dew", font=("times new roman", 16, "bold"), bg=bgcolor,
                        fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Dew_txt = Entry(f4, width=10, textvariable=self.Dew, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Litchi_lbl = Label(f4, text="Slice", font=("times new roman", 16, "bold"), bg=bgcolor,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Litchi_txt = Entry(f4, width=10, textvariable=self.Litchi, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Frooty_lbl = Label(f4, text="Frooty", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        Frooty_txt = Entry(f4, width=10, textvariable=self.Frooty, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        Pepsi_lbl = Label(f4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=6, column=0, padx=10, pady=10, sticky="w")
        Pepsi_txt = Entry(f4, width=10, textvariable=self.Pepsi, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        # ++++++++++++ Bill area frame ++++++++++++++

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1010, y=185, width=505, height=430)
        bill_title = Label(f5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # +++++++++++ Button Frame +++++++++++++

        f6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bgcolor)
        f6.place(x=0, y=625, relwidth=1, height=160)

        m1_lbl = Label(f6, text="Total MOMO Price", bg=bgcolor, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky="w")
        m1_txt = Entry(f6, width=18, textvariable=self.Total_momo, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=2)

        m2_lbl = Label(f6, text="Total Cold Drinks Price", bg=bgcolor, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        m2_txt = Entry(f6, width=18, textvariable=self.Total_cd, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=2)

        t1_lbl = Label(f6, text="Service Charge", bg=bgcolor, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky="w")
        t1_txt = Entry(f6, width=18, textvariable=self.Service_charge, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=2)

    

        t2_lbl = Label(f6, text="Total Payment", bg=bgcolor, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=5, sticky="w")
        t2_txt = Entry(f6, width=18, textvariable=self.Total_pay, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=2)



        # +++++++++++++++ main button frame ++++++++++++++++++++++++

        btn_frame = Frame(f6, bd=7, relief=GROOVE)
        btn_frame.place(x=820, width=690, height=115)

        total_btn = Button(btn_frame, command=self.total, text="Total", bg="#00F9FF", fg="black", pady=20, bd=5,
                           width="12", font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        Bill_btn = Button(btn_frame, text="Generate Bill", command=self.bill_area, bg="yellow", fg="black", pady=20,
                          bd=5, width="12", font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_frame, text="Clear", command=self.clear_data, bg="#F66323", fg="black", pady=20, bd=5,
                           width="12", font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_frame, text="Exit", command=self.exit_app, bg="red", fg="black", pady=20, bd=5,
                          width="11", font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.Total_momoo = float(
            (self.chicken.get() * self.uchicken) +
            (self.buff.get() * self.ubuff) +
            (self.veg.get() * self.uveg) +
            (self.cjhol.get() * self.ucjhol) +
            (self.cfry.get() * self.ucfry) +
            (self.bfry.get() * self.ubfry) +
            (self.vfry.get() * self.uvfry)+
            (self.paneer.get() * self.upaneer)+
            (self.fish.get() * self.ufish) +
            (self.green.get() * self.ugreen) +
            (self.cheese.get() * self.ucheese) +
            (self.kothe.get() * self.ukothe) +
            (self.chilly.get() * self.uchilly) +
            (self.wheat.get() * self.uwheat)
        )
        self.Total_momo.set("Rs " + str(self.Total_momoo))

        # calculating total for cold drinks products
        self.total_cdrinks_price = float(
            (self.Coke.get() * self.ucoke) +
            (self.Sprite.get() * self.usprite) +
            (self.Fanta.get() * self.ufanta) +
            (self.Dew.get() * self.udew) +
            (self.Litchi.get() * self.ulitchi) +
            (self.Frooty.get() * self.ufrooty) +
            (self.Pepsi.get() * self.upepsi)
        )
        self.Total_cd.set("Rs " + str(self.total_cdrinks_price))

        self.Service_charge.set("Rs " + str(round((self.total_cdrinks_price+self.Total_momoo) * 0.10, 2)))
        self.Total_pay.set(self.Total_momoo + self.total_cdrinks_price + round(
            (self.total_cdrinks_price + self.Total_momoo) * 0.10, 2))
        self.Total_payy = self.Total_momoo + self.total_cdrinks_price + round((self.total_cdrinks_price+self.Total_momoo) * 0.10, 2)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tWelcome Jhapali MOMO center\n")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        x = datetime.datetime.now()
        datee = x.strftime("%Y/%m/%d")
        self.txtarea.insert(END, f"\nDate:{datee}")
        self.txtarea.insert(END, "\n=========================================================")
        self.txtarea.insert(END, "\nItems \t\t QTY \t Unit_Price\t\tTotal_Price")
        self.txtarea.insert(END, "\n=========================================================")

    #++++++++++++++++ bill area ++++++++++++++++++

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif (self.Total_momo.get() == "Rs 0.0" and self.Total_cd.get() == "Rs 0.0"):
            messagebox.showerror("Error", "No products purchased")
        else:
            self.welcome_bill()

            if (self.chicken.get() != 0):
                self.txtarea.insert(END,
                                    f"\nChicken momo \t\t {self.chicken.get()} \t Rs {self.uchicken}\t\tRs {self.chicken.get() * self.uchicken} ")

            if (self.buff.get() != 0):
                self.txtarea.insert(END,
                                    f"\nBuff momo \t\t {self.buff.get()} \t Rs {self.ubuff}\t\tRs {self.buff.get() * self.ubuff} ")

            if (self.veg.get() != 0):
                self.txtarea.insert(END,
                                    f"\nVeg momo \t\t {self.veg.get()} \t Rs {self.uveg}\t\tRs {self.veg.get() * self.uveg} ")

            if (self.cjhol.get() != 0):
                self.txtarea.insert(END,
                                    f"\nChicken Jhol \t\t {self.cjhol.get()} \t Rs {self.ucjhol}\t\tRs {self.cjhol.get() * self.ucjhol} ")

            if (self.cfry.get() != 0):
                self.txtarea.insert(END,
                                    f"\nChicken Fry \t\t {self.cfry.get()} \t Rs {self.ucfry}\t\tRs {self.cfry.get() * self.ucfry} ")

            if (self.bfry.get() != 0):
                self.txtarea.insert(END,
                                    f"\nBuff Fry \t\t {self.bfry.get()} \t Rs {self.ubfry}\t\tRs {self.bfry.get() * self.ubfry} ")

            if (self.vfry.get() != 0):
                self.txtarea.insert(END,
                                    f"\nVeg Fry \t\t {self.vfry.get()} \t Rs {self.uvfry}\t\tRs {self.vfry.get() * self.uvfry} ")

            if (self.paneer.get() != 0):
                self.txtarea.insert(END,
                                    f"\nPaneer momo \t\t {self.paneer.get()} \t Rs {self.upaneer}\t\tRs {self.paneer.get() * self.upaneer} ")

            if (self.fish.get() != 0):
                self.txtarea.insert(END,
                                    f"\nFish momo \t\t {self.fish.get()} \t Rs {self.ufish}\t\tRs {self.fish.get() * self.ufish} ")

            if (self.green.get() != 0):
                self.txtarea.insert(END,
                                    f"\nGreen momo \t\t {self.green.get()} \t Rs {self.ugreen}\t\tRs {self.green.get() * self.ugreen} ")

            if (self.cheese.get() != 0):
                self.txtarea.insert(END,
                                    f"\nCheese momo \t\t {self.cheese.get()} \t Rs {self.ucheese}\t\tRs {self.cheese.get() * self.ucheese} ")

            if (self.kothe.get() != 0):
                self.txtarea.insert(END,
                                    f"\nKothe momo \t\t {self.kothe.get()} \t Rs {self.ukothe}\t\tRs {self.kothe.get() * self.ukothe} ")

            if (self.chilly.get() != 0):
                self.txtarea.insert(END,
                                    f"\nChilly momo \t\t {self.chilly.get()} \t Rs {self.uchilly}\t\tRs {self.chilly.get() * self.uchilly} ")

            if (self.wheat.get() != 0):
                self.txtarea.insert(END,
                                    f"\nWheat momo \t\t {self.wheat.get()} \t Rs {self.uwheat}\t\tRs {self.wheat.get() * self.uwheat} ")

            # =============== for cold drinks ==================

            if (self.Coke.get() != 0):
                self.txtarea.insert(END,
                                    f"\nCoke \t\t {self.Coke.get()} \t Rs {self.ucoke}\t\tRs {self.Coke.get() * self.ucoke} ")

            if (self.Fanta.get() != 0):
                self.txtarea.insert(END,
                                    f"\nFanta \t\t {self.Fanta.get()} \t Rs {self.ufanta}\t\tRs {self.Fanta.get() * self.ufanta} ")

            if (self.Sprite.get() != 0):
                self.txtarea.insert(END,
                                    f"\nSprite \t\t {self.Sprite.get()} \t Rs {self.usprite}\t\tRs {self.Sprite.get() * self.usprite} ")

            if (self.Dew.get() != 0):
                self.txtarea.insert(END,
                                    f"\nMountain Dew \t\t {self.Dew.get()} \t Rs {self.udew}\t\tRs {self.Dew.get() * self.udew} ")

            if (self.Litchi.get() != 0):
                self.txtarea.insert(END,
                                    f"\nSlice \t\t {self.Litchi.get()} \t Rs {self.ulitchi}\t\tRs {self.Litchi.get() * self.ulitchi} ")

            if (self.Frooty.get() != 0):
                self.txtarea.insert(END,
                                    f"\nFrooty \t\t {self.Frooty.get()} \t Rs {self.ufrooty}\t\tRs {self.Frooty.get() * self.ufrooty} ")

            if (self.Pepsi.get() != 0):
                self.txtarea.insert(END,
                                    f"\nPepsi \t\t {self.Pepsi.get()} \t Rs {self.upepsi}\t\tRs {self.Pepsi.get() * self.upepsi} ")

            self.txtarea.insert(END, "\n---------------------------------------------------------")
            if (self.Total_momo.get() != "Rs 0.0"):
                self.txtarea.insert(END, f"\nTotal MOMO Payment:\t\t{self.Total_momo.get()}")

            if (self.Total_cd.get() != "Rs 0.0"):
                self.txtarea.insert(END, f"\nTotal Cold Drinks Payment:\t\t{self.Total_cd.get()}")

            if (self.Service_charge.get() != "Rs 0.0"):
                self.txtarea.insert(END, f"\nTotal Service Charge(10%):\t\t{self.Service_charge.get()}")

            self.txtarea.insert(END, "\n---------------------------------------------------------")

            self.txtarea.insert(END, f"\nTotal Payment:\t\tRs {self.Total_payy}")
            self.txtarea.insert(END, "\n---------------------------------------------------------")
            self.save_bill()

    #+============== Function for saving the bill +++++++++++++++++++++

    def save_bill(self):
        op = messagebox.askyesno("Save", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill: {self.bill_no.get()} saved successfully")
        else:
            return
    #++++++++++++++++++= Function for searching the bill ++++++++++++++++++++++

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Bill Not Found")

    #++++++++++++++++++++++ Function for clearing the data ++++++++++++++++++++

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data?")
        if op > 0:
            # ==================set Variables to 0 ++++++++++++++++++++
            self.chicken.set(0)
            self.buff.set(0)
            self.veg.set(0)
            self.cjhol.set(0)
            self.cfry.set(0)
            self.bfry.set(0)
            self.vfry.set(0)
            self.paneer.set(0)
            self.fish.set(0)
            self.green.set(0)
            self.cheese.set(0)
            self.kothe.set(0)
            self.chilly.set(0)
            self.wheat.set(0)
            self.Coke.set(0)
            self.Fanta.set(0)
            self.Sprite.set(0)
            self.Dew.set(0)
            self.Litchi.set(0)
            self.Frooty.set(0)
            self.Pepsi.set(0)

            self.Total_momo.set("")
            self.Total_cd.set("")
            self.Service_charge.set("")
            self.Total_pay.set("")

            # +++++++++++++++++ customer details  ++++++++++++++++
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            xt = random.randint(10000, 99999)
            self.bill_no.set(str(xt))
            self.search_bill.set("")
            self.welcome_bill()

    #++++++++++++++ Function for exiting the app++++++++++++++++++

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()