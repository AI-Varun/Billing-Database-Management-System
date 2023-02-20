import datetime
import os
# from InvoiceGenerator.api import UnicodeProperty
# from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
# from InvoiceGenerator.pdf import SimpleInvoice
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QMainWindow, QStackedWidget, \
    QPushButton, QLineEdit, QFrame, QTableWidget, QTableWidgetItem,QTextBrowser
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QEasingCurve
from PyQt6 import uic
import sys
import mysql.connector as mc
from PyQt6 import QtGui
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("welcome.ui", self)
        self.login = self.findChild(QPushButton, "login")
        self.login.clicked.connect(self.goto_login)
        self.pushButton_Create_Account = self.findChild(QPushButton, "pushButton_Create_Account")
        self.pushButton_Create_Account.clicked.connect(self.goto_signUp)

    def goto_login(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_signUp(self):
        signup = Create_acc_screen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("Login.ui", self)
        self.username = self.findChild(QLineEdit, "lineEdit_Username")
        self.password = self.findChild(QLineEdit, "lineEdit_Password")
        self.label_error = self.findChild(QLabel, "label_Error")
        self.login_2 = self.findChild(QPushButton, "login_2")
        self.login_2.clicked.connect(self.login_function)
        self.welcome_Back = self.findChild(QPushButton, "pushButton_back")
        self.welcome_Back.setIcon(QIcon("Images/previous.png"))
        self.welcome_Back.clicked.connect(self.goto_welcome)

    def login_function(self):
        user = self.username.text()
        password = self.password.text()

        if len(user) == 0 or len(password) == 0:
            self.label_error.setText("Please input all field")

        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="billingdb"
                )
                mycursor = mydb.cursor()
                query = "SELECT username,password from users where username like '" + user + "'and password like '" + password + "'"

                mycursor.execute(query)
                result_password = mycursor.fetchone()

                if result_password == None:
                    self.label_error.setText("Invalid username and password")

                else:

                    # print("successfully logged in.")
                    self.goto_MainWindow()
                    # self.label_error.setText("successfully logged in.")

            except mc.Error as e:
                self.label_error.setText("Error in connection")

    def goto_welcome(self):
        welcome1 = WelcomeScreen()
        widget.addWidget(welcome1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_MainWindow(self):
        login_2 = MainWindow()
        widget.addWidget(login_2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Create_acc_screen(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("SignUp.ui", self)
        self.lineEdit_Username_SignUP = self.findChild(QLineEdit, "lineEdit_Username_SignUP")
        self.lineEdit_Password_SignUP = self.findChild(QLineEdit, "lineEdit_Password_SignUP")
        self.lineEdit_Confirm_Password_SignUP = self.findChild(QLineEdit, "lineEdit_Confirm_Password_SignUP")
        self.label_Error_SignUp = self.findChild(QLabel, "label_Error_SignUp")
        self.SignUp = self.findChild(QPushButton, "SignUp")
        self.SignUp.clicked.connect(self.signUp_function)
        self.pushButton_back_SignUp = self.findChild(QPushButton, "pushButton_back_SignUp")
        self.pushButton_back_SignUp.setIcon(QIcon("Images/previous.png"))
        self.pushButton_back_SignUp.clicked.connect(self.goto_welcomes)

    def signUp_function(self):
        user = self.lineEdit_Username_SignUP.text()
        password = self.lineEdit_Password_SignUP.text()
        confirmPassword = self.lineEdit_Confirm_Password_SignUP.text()

        if len(user) == 0 or len(password) == 0 or len(confirmPassword) == 0:
            self.label_Error_SignUp.setText("Please fill in all inputs.")

        elif password != confirmPassword:
            self.label_Error_SignUp.setText("Password do not match.")

        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="billingdb"
                )

                mycursor = mydb.cursor()

                query = "Insert Into users (username, password) VALUES (%s, %s)"
                value = (user, password)

                mycursor.execute(query, value)

                mydb.commit()
                self.label_Error_SignUp.setText("Data Inserted")
            except mc.Error as e:
                self.label_Error_SignUp.setText("Error in inserting data")

    def goto_welcomes(self):
        welcome2 = WelcomeScreen()
        widget.addWidget(welcome2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("main_page_2.ui", self)
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.stackedWidget.setCurrentWidget(self.create_Invoice_Page)

        self.left_Toggle_menu = self.findChild(QFrame, "left_Toggle_menu")
        self.left_Toggle_menu.setStyleSheet("background-image: url(Images/img1);")

        self.top_Frame = self.findChild(QFrame, "top_Frame")
        self.top_Frame.setStyleSheet("background-image: url(Images/img1);")

        self.content_Page = self.findChild(QFrame, "content_Page")
        self.content_Page.setStyleSheet("background-image: url(Images/img2);")
        self.Btn_Toggle = self.findChild(QPushButton, "toggle_btn")
        self.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Images/toggle.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        # self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIcon(QIcon("Images/toggle.png"))

        self.toggle_frame = self.findChild(QFrame, "left_Toggle_menu")

        self.create_Invoice_Btn = self.findChild(QPushButton, "create_Invoice_Btn")
        self.create_Invoice_Btn.setIcon(QIcon("Images/Create Invoice.png"))
        self.create_Invoice_Btn.clicked.connect(self.createInvoicepage)

        self.time = self.findChild(QTextBrowser, "time")
        self.date = self.findChild(QTextBrowser, "date")
        self.create_Invoice_Btn.clicked.connect(self.date_time)

        self.new_Customer_Btn = self.findChild(QPushButton, "new_Customer_Btn")
        self.new_Customer_Btn.setIcon(QIcon("Images/Add User1.png"))
        self.new_Customer_Btn.clicked.connect(self.newCustomerPage)

        self.newCustomer_Name_LineEdit = self.findChild(QLineEdit, "newCustomer_Name_LineEdit")
        self.newCustomer_Contact_LineEdit = self.findChild(QLineEdit, "newCustomer_Contact_LineEdit")
        self.newCustomer_Email_LineEdit = self.findChild(QLineEdit, "newCustomer_Email_LineEdit")
        self.newCustomer_Address_LineEdit = self.findChild(QLineEdit, "newCustomer_Address_LineEdit")
        self.newCustomer_Gender_LineEdit = self.findChild(QLineEdit, "newCustomer_Gender_LineEdit")
        self.newCustomer_Save = self.findChild(QPushButton, "newCustomer_Save")
        self.newCustomer_Save.clicked.connect(self.insert_New_Customer_Details)

        self.invoice_Detail_tableWidget = self.findChild(QTableWidget, "invoice_Detail_tableWidget")
        self.invoice_Generate_btn = self.findChild(QPushButton, "invoice_Generate_btn")
        self.invoice_Generate_btn.clicked.connect(self.invoice_generator)

        self.invoice_Contact_LineEdit = self.findChild(QLineEdit, "invoice_Contact_LineEdit")
        self.invoice_Name_LineEdit = self.findChild(QLineEdit, "invoice_Name_LineEdit")
        self.invoice_Email_LineEdit = self.findChild(QLineEdit, "invoice_Email_LineEdit")
        self.invoice_Address_LineEdit = self.findChild(QLineEdit, "invoice_Address_LineEdit")
        self.invoice_CustomerContact_Search_btn = self.findChild(QPushButton, "invoice_CustomerContact_Search_btn")
        self.invoice_CustomerContact_Search_btn.clicked.connect(self.retrive_Invoice_Customer_Details)

        self.invoice_PId_LineEdit = self.findChild(QLineEdit, "invoice_PId_LineEdit")
        self.invoice_ProductName_LineEdit = self.findChild(QLineEdit, "invoice_ProductName_LineEdit")
        self.invoice_Qty_LineEdit = self.findChild(QLineEdit, "invoice_Qty_LineEdit")
        self.invoice_Rate_LineEdit = self.findChild(QLineEdit, "invoice_Rate_LineEdit")
        self.invoice_ProductId_Search_btn = self.findChild(QPushButton, "invoice_ProductId_Search_btn")
        self.invoice_ProductId_Search_btn.clicked.connect(self.retrive_Invoice_Product_Details)

        self.invoice_Total_LineEdit = self.findChild(QLineEdit, "invoice_Total_LineEdit")
        self.invoice_PaidAmount_LineEdit = self.findChild(QLineEdit, "invoice_PaidAmount_LineEdit")
        self.invoice_ReturnAmount_LineEdit = self.findChild(QLineEdit, "invoice_ReturnAmount_LineEdit")

        # self.invoice_Calculate_btn = self.findChild(QPushButton, "invoice_Calculate_btn")
        # self.invoice_Calculate_btn.clicked.connect(self.summation)

        # self.invoice_Generate_btn = self.findChild(QPushButton, "invoice_Generate_btn")
        # self.invoice_Generate_btn.clicked.connect(self.retrive_Invoice_Product_Details)

        self.invoice_Add_btn = self.findChild(QPushButton, "invoice_Add_btn")
        self.invoice_Add_btn.clicked.connect(self.show_Invoice_Product_Details)

        self.newCustomer_Reset = self.findChild(QPushButton, "newCustomer_Reset")
        # self.newCustomer_Reset.clicked.connect(self.)

        self.update_Customer_Btn = self.findChild(QPushButton, "update_Customer_Btn")
        self.update_Customer_Btn.setIcon(QIcon("Images/update customer1.png"))
        self.update_Customer_Btn.clicked.connect(self.updateCustomerPage)

        self.updateCustomer_Name_LineEdit = self.findChild(QLineEdit, "updateCustomer_Name_LineEdit")
        self.updateCustomer_Contact_LineEdit = self.findChild(QLineEdit, "updateCustomer_Contact_LineEdit")
        self.updateCustomer_Email_LineEdit = self.findChild(QLineEdit, "updateCustomer_Email_LineEdit")
        self.updateCustomer_Address_LineEdit = self.findChild(QLineEdit, "updateCustomer_Address_LineEdit")
        self.updateCustomer_Gender_LineEdit = self.findChild(QLineEdit, "updateCustomer_Gender_LineEdit")
        self.updateCustomer_PrimaryKey_LineEdit = self.findChild(QLineEdit, "updateCustomer_PrimaryKey_LineEdit")

        self.updateCustomer_PrimaryKey_btn = self.findChild(QPushButton, "updateCustomer_PrimaryKey_btn")
        self.updateCustomer_PrimaryKey_btn.clicked.connect(self.retrive_Customer_Details)

        self.updateCustomer_Update_btn = self.findChild(QPushButton, "updateCustomer_Update_btn")
        self.updateCustomer_Update_btn.clicked.connect(self.update_Customer_Details)

        # self.updateCustomer_Reset_btn = self.findChild(QPushButton, "updateCustomer_Reset_btn")
        # self.updateCustomer_Reset_btn.clicked.connect(self.)

        self.customer_Details_Btn = self.findChild(QPushButton, "customer_Details_Btn")
        self.customer_Details_Btn.setIcon(QIcon("Images/Customer_Details1.png"))
        self.customer_Details_Btn.clicked.connect(self.customerDetailsPage)

        self.customer_Details_Table = self.findChild(QTableWidget, "customer_Details_Table")
        self.customer_Details_Btn.clicked.connect(self.show_Customer_Details)

        self.customer_Details_Print_Btn = self.findChild(QPushButton, "customer_Details_Print_Btn")
        self.customer_Details_Print_Btn.clicked.connect(self.print_file)

        self.delete_Customer_Btn = self.findChild(QPushButton, "delete_Customer_Btn")
        self.delete_Customer_Btn.setIcon(QIcon("Images/Delete customer.png"))
        self.delete_Customer_Btn.clicked.connect(self.deleteCustomerPage)

        self.delete_Customer_Name_LineEdit = self.findChild(QLineEdit, "delete_Customer_Name_LineEdit")
        self.delete_Customer_Contact_LineEdit = self.findChild(QLineEdit, "delete_Customer_Contact_LineEdit")
        self.delete_Customer_Email_LineEdit = self.findChild(QLineEdit, "delete_Customer_Email_LineEdit")
        self.delete_Customer_Address_LineEdit = self.findChild(QLineEdit, "delete_Customer_Address_LineEdit")
        self.delete_Customer_Gender_LineEdit = self.findChild(QLineEdit, "delete_Customer_Gender_LineEdit")
        self.delete_Customer_contact_primaryKey_LineEdit = self.findChild(QLineEdit,
                                                                          "delete_Customer_contact_primaryKey_LineEdit")

        self.delete_Customer_PrimaryKey_btn = self.findChild(QPushButton, "delete_Customer_PrimaryKey_btn")
        self.delete_Customer_PrimaryKey_btn.clicked.connect(self.retrive2_Customer_Details)

        self.delete_Customer_Delete_btn = self.findChild(QPushButton, "delete_Customer_Delete_btn")
        self.delete_Customer_Delete_btn.clicked.connect(self.delete_Customer_Details)

        self.add_Item_Btn = self.findChild(QPushButton, "add_Item_Btn")
        self.add_Item_Btn.setIcon(QIcon("Images/Add item.png"))
        self.add_Item_Btn.clicked.connect(self.addItemPage)
        self.add_Item_Btn.clicked.connect(self.fetch_Product_Id)

        self.AddItem_ProductId_PrimaryKey_Label = self.findChild(QLabel, "AddItem_ProductId_PrimaryKey_Label")
        self.AddItem_ProductName_LineEdit = self.findChild(QLineEdit, "AddItem_ProductName_LineEdit")
        self.AddItem_Rate_LineEdit = self.findChild(QLineEdit, "AddItem_Rate_LineEdit")
        self.AddItem_Description_LineEdit = self.findChild(QLineEdit, "AddItem_Description_LineEdit")

        self.AddItem_Save_PushButton = self.findChild(QPushButton, "AddItem_Save_PushButton")
        self.AddItem_Save_PushButton.clicked.connect(self.insert_New_Product_Details)
        self.AddItem_Save_PushButton.clicked.connect(self.fetch_Product_Id)

        self.update_Item_Btn = self.findChild(QPushButton, "update_Item_Btn")
        self.update_Item_Btn.setIcon(QIcon("Images/Update Item.png"))
        self.update_Item_Btn.clicked.connect(self.updateItemPage)

        self.updateItem_ProductId_Update_btn = self.findChild(QPushButton, "updateItem_ProductId_Update_btn")
        self.updateItem_ProductId_Update_btn.clicked.connect(self.update_Product_Details)

        self.updateItem_ProductId_PrimaryKey_LineEdit = self.findChild(QLineEdit,
                                                                       "updateItem_ProductId_PrimaryKey_LineEdit")
        self.updateItem_ProductName_LineEdit = self.findChild(QLineEdit, "updateItem_ProductName_LineEdit")
        self.updateItem_Rate_LineEdit = self.findChild(QLineEdit, "updateItem_Rate_LineEdit")
        self.updateItem_Description_LineEdit = self.findChild(QLineEdit, "updateItem_Description_LineEdit")

        self.updateItem_ProductId_Search_btn = self.findChild(QPushButton, "updateItem_ProductId_Search_btn")
        self.updateItem_ProductId_Search_btn.clicked.connect(self.retrive_Product_Details)

        self.item_Details_Btn = self.findChild(QPushButton, "item_Details_Btn")
        self.item_Details_Btn.setIcon(QIcon("Images/Item Details.png"))
        self.item_Details_Btn.clicked.connect(self.itemDetailsPage)

        self.item_Details_tableWidget = self.findChild(QTableWidget, "item_Details_tableWidget")
        self.item_Details_Btn.clicked.connect(self.show_Product_Details)

        self.item_Details_PushButton = self.findChild(QPushButton, "item_Details_PushButton")
        # self.item_Details_PushButton.clicked.connect(self.itemDetailsPage)
        self.item_Details_PushButton.clicked.connect(lambda: self.print_file(self.item_Details_tableWidget))


        self.delete_Item_Btn = self.findChild(QPushButton, "delete_Item_Btn")
        self.delete_Item_Btn.setIcon(QIcon("Images/Delete item.png"))
        self.delete_Item_Btn.clicked.connect(self.deleteItemPage)

        self.deleteItem_ProductId_PrimaryKey_LineEdit = self.findChild(QLineEdit,
                                                                       "deleteItem_ProductId_PrimaryKey_LineEdit")
        self.deleteItem_ProductName_LineEdit = self.findChild(QLineEdit, "deleteItem_ProductName_LineEdit")
        self.deleteItem_Rate_LineEdit = self.findChild(QLineEdit, "deleteItem_Rate_LineEdit")
        self.deleteItem_Description_LineEdit = self.findChild(QLineEdit, "deleteItem_Description_LineEdit")

        self.DeleteItem_Save_PushButton = self.findChild(QPushButton, "DeleteItem_Save_PushButton")
        self.DeleteItem_Save_PushButton.clicked.connect(self.delete_Product_Details)

        self.DeleteItem_Search_btn = self.findChild(QPushButton, "DeleteItem_Search_btn")
        self.DeleteItem_Search_btn.clicked.connect(self.retrive2_Product_Details)

        self.logout_Btn = self.findChild(QPushButton, "logout_Btn")
        self.logout_Btn.setIcon(QIcon("Images/Logout.png"))
        self.logout_Btn.clicked.connect(self.goto_WelcomeScreen)

        self.table_widget = QTableWidget()
        print(self.table_widget)


    def show_Invoice_Product_Details(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query2 = "SELECT * FROM product_table where product_id like'" + self.invoice_PId_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query2)
            row3 = mycursor.fetchall()

            text1 = self.invoice_PId_LineEdit.text()
            text2 = self.invoice_ProductName_LineEdit.text()
            text3 = self.invoice_Rate_LineEdit.text()
            text4 = "18%"
            text5 = self.invoice_Qty_LineEdit.text()
            total = ((int(text5)*int(text3))+(((int(text5)*int(text3))*18)/100))

            row = self.invoice_Detail_tableWidget.rowCount()
            self.invoice_Detail_tableWidget.insertRow(row)

            self.invoice_Detail_tableWidget.setItem(row, 0, QTableWidgetItem(str(text1)))
            self.invoice_Detail_tableWidget.setItem(row, 1, QTableWidgetItem(str(text2)))
            for row1 in row3:
                self.invoice_Detail_tableWidget.setItem(row, 2, QTableWidgetItem(str(row1[3])))
            self.invoice_Detail_tableWidget.setItem(row, 3, QTableWidgetItem(str(text3)))
            self.invoice_Detail_tableWidget.setItem(row, 4, QTableWidgetItem(str(text4)))
            self.invoice_Detail_tableWidget.setItem(row, 5, QTableWidgetItem(str(text5)))
            self.invoice_Detail_tableWidget.setItem(row, 6, QTableWidgetItem(str(total)))
            self.table_widget = self.invoice_PId_LineEdit

        except mc.Error as e:
            self.updateItem_ProductId_PrimaryKey_LineEdit("Error in connection")

    # def summation(self):
    #     row = self.table_widget.currentRow()
    #     table = QtGui.QTableWidgetItem()
    #     try:
    #         data = sum([int(item.text()) for item in self.table_widget.selectedItems()])
    #         table.setText(str(data))
    #     except ValueError:
    #         pass
    #     self.table_widget.setItem(row, 10, table)
    #     print(self.tableWidget)



    def retrive_Invoice_Product_Details(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query1 = "SELECT * FROM  product_table where product_id like'" + self.invoice_PId_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            row = mycursor.fetchall()

            if row == None:
                self.invoice_PId_LineEdit.setText("")

            else:
                for row1 in row:
                    self.invoice_ProductName_LineEdit.setText(str(row1[1]))
                    self.invoice_Rate_LineEdit.setText(str(row1[2]))

        except mc.Error as e:
            self.invoice_PId_LineEdit("Error in connection")

    def retrive_Invoice_Customer_Details(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query1 = "SELECT * FROM  customer_table where contact like'" + self.invoice_Contact_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            row = mycursor.fetchall()

            if row == None:
                # self.updateCustomer_Name_LineEdit.setText("No user found with this username")
                self.invoice_Contact_LineEdit.setText("")

            else:
                # self.updateCustomer_PrimaryKey_LineEdit.setText("username has been found")
                for row1 in row:
                    # self.invoice_Contact_LineEdit.setText(str(row1[0]))
                    self.invoice_Name_LineEdit.setText(str(row1[0]))
                    self.invoice_Email_LineEdit.setText(str(row1[2]))
                    self.invoice_Address_LineEdit.setText(str(row1[3]))

        except mc.Error as e:
            self.invoice_Contact_LineEdit("Error in connection")

    # def invoice_generator(self):
    #
    #     os.environ["INVOICE_LANG"] = "en"
    #
    #     client = Client(self.invoice_Name_LineEdit.text())
    #     provider = Provider('Galaxy Tech World', bank_account='85475956325895', bank_code='SBIN0009999')
    #     creator = Creator('Galaxy Tech World Manager')
    #
    #     invoice = Invoice(client, provider, creator)
    #     invoice.currency_locale = 'en_IN.UTF-8'
    #
    #
    #     invoice.add_item(Item(self.invoice_Qty_LineEdit.text(), self.invoice_Rate_LineEdit.text(), description=self.invoice_ProductName_LineEdit.text(),tax=18))
    #
    #
    #     pdf = SimpleInvoice(invoice)
    #     pdf.gen(self.invoice_Name_LineEdit.text()+".pdf", generate_qr_code=True)



    def date_time(self):
        DateTime=datetime.datetime.now()

        self.date.setText('date: %s:%s:%s'% (DateTime.day,DateTime.month,DateTime.year))
        self.time.setText('time: %s:%s:%s' % (DateTime.hour, DateTime.minute, DateTime.second))

    def show_Product_Details(self):

        tblname = "product_table"
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT *  FROM {}".format(tblname))

            result = mycursor.fetchall()

            self.item_Details_tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.item_Details_tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.item_Details_tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error Occured")


    def goto_WelcomeScreen(self):
        login_3 = WelcomeScreen()
        widget.addWidget(login_3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def print_file(self,customer_Details_Table):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.customer_Details_Table.print(printer)

    def retrive2_Product_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query2 = "SELECT * FROM product_table where product_id like'" + self.deleteItem_ProductId_PrimaryKey_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query2)
            row = mycursor.fetchall()

            if row == None:
                self.deleteItem_ProductId_PrimaryKey_LineEdit.setText("No user found with this username")
                self.deleteItem_ProductId_PrimaryKey_LineEdit.setText("")

            else:
                # self.updateCustomer_PrimaryKey_LineEdit.setText("username has been found")
                for row1 in row:
                    self.deleteItem_ProductName_LineEdit.setText(str(row1[1]))
                    self.deleteItem_Rate_LineEdit.setText(str(row1[2]))
                    self.deleteItem_Description_LineEdit.setText(str(row1[3]))

        except mc.Error as e:
            self.deleteItem_ProductId_PrimaryKey_LineEdit("Error in connection")

    def delete_Product_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            pid = str(self.deleteItem_ProductId_PrimaryKey_LineEdit.text())
            pname = str(self.deleteItem_ProductName_LineEdit.text())
            rate = str(self.deleteItem_Rate_LineEdit.text())
            desc = str(self.deleteItem_Description_LineEdit.text())

            query1 = ("DELETE FROM product_table WHERE product_id = '%s'" % (pid))
            query2 = ("DELETE FROM product_table WHERE Pname = '%s'" % (pname))
            query3 = ("DELETE FROM product_table WHERE Rate = '%s'" % (rate))
            query4 = ("DELETE FROM product_table WHERE Description = '%s'" % (desc))
            print(query3)

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            mycursor.execute(query2)
            if rate=="" :
                mycursor.execute(query3)
            mycursor.execute(query4)

        except mc.Error as e:
            print("Error in connection")

    def update_Product_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            pid = str(self.updateItem_ProductId_PrimaryKey_LineEdit.text())
            pname = str(self.updateItem_ProductName_LineEdit.text())
            rate = str(self.updateItem_Rate_LineEdit.text())
            desc = str(self.updateItem_Description_LineEdit.text())

            query1 = ("UPDATE product_table SET Pname = '%s' WHERE product_id = '%s'" % (pname, pid))
            query2 = ("UPDATE product_table SET Rate = '%s'WHERE product_id = '%s'" % (rate, pid))
            query3 = ("UPDATE product_table SET Description = '%s'WHERE product_id = '%s'" % (desc, pid))

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            print('hello')
            mycursor.execute(query2)
            mycursor.execute(query3)

        except mc.Error as e:
            print("Error in connection")

    def retrive_Product_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query2 = "SELECT * FROM product_table where product_id like'" + self.updateItem_ProductId_PrimaryKey_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query2)
            row = mycursor.fetchall()

            if row == None:
                self.updateItem_ProductId_PrimaryKey_LineEdit.setText("No user found with this username")
                self.updateItem_ProductId_PrimaryKey_LineEdit.setText("")

            else:
                # self.updateCustomer_PrimaryKey_LineEdit.setText("username has been found")
                for row1 in row:
                    self.updateItem_ProductName_LineEdit.setText(str(row1[0]))
                    self.updateItem_Rate_LineEdit.setText(str(row1[1]))
                    self.updateItem_Description_LineEdit.setText(str(row1[2]))

        except mc.Error as e:
            self.updateItem_ProductId_PrimaryKey_LineEdit("Error in connection")

    def fetch_Product_Id(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            query = "SELECT * FROM product_table ORDER BY product_id DESC LIMIT 1"
            # query1="insert into product_table set product_id = 1, val = "" "

            mycursor = mydb.cursor()
            mycursor.execute(query)
            row = mycursor.fetchone()
            self.AddItem_ProductId_PrimaryKey_Label.setText(str(row[0]))

        except mc.Error as e:
            self.delete_Customer_contact_primaryKey_LineEdit("Error in connection")

    def createInvoicepage(self):
        self.stackedWidget.setCurrentWidget(self.create_Invoice_Page)

    def newCustomerPage(self):
        self.stackedWidget.setCurrentWidget(self.new_Customer_Page)

    def customerDetailsPage(self):
        self.stackedWidget.setCurrentWidget(self.customer_Details_Page)

    def deleteCustomerPage(self):
        self.stackedWidget.setCurrentWidget(self.delete_Customer_Page)

    def addItemPage(self):
        self.stackedWidget.setCurrentWidget(self.add_Item_Page)

    def updateItemPage(self):
        self.stackedWidget.setCurrentWidget(self.update_Item_Page)

    def itemDetailsPage(self):
        self.stackedWidget.setCurrentWidget(self.item_Details_Page)

    def deleteItemPage(self):
        self.stackedWidget.setCurrentWidget(self.delete_Item_page)

    def updateCustomerPage(self):
        self.stackedWidget.setCurrentWidget(self.update_Customer_Page)

    def retrive2_Customer_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query2 = "SELECT * FROM  customer_table where contact like'" + self.delete_Customer_contact_primaryKey_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query2)
            row = mycursor.fetchall()

            if row == None:
                self.delete_Customer_contact_primaryKey_LineEdit.setText("No user found with this username")
                self.delete_Customer_contact_primaryKey_LineEdit.setText("")

            else:
                # self.updateCustomer_PrimaryKey_LineEdit.setText("username has been found")
                for row1 in row:
                    self.delete_Customer_Name_LineEdit.setText(str(row1[0]))
                    self.delete_Customer_Contact_LineEdit.setText(str(row1[1]))
                    self.delete_Customer_Email_LineEdit.setText(str(row1[2]))
                    self.delete_Customer_Address_LineEdit.setText(str(row1[3]))
                    self.delete_Customer_Gender_LineEdit.setText(str(row1[4]))
        except mc.Error as e:
            self.delete_Customer_contact_primaryKey_LineEdit("Error in connection")

    def retrive_Customer_Details(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            query1 = "SELECT * FROM  customer_table where contact like'" + self.updateCustomer_PrimaryKey_LineEdit.text() + "'"

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            row = mycursor.fetchall()

            if row == None:
                self.updateCustomer_Name_LineEdit.setText("No user found with this username")
                self.updateCustomer_Name_LineEdit.setText("")

            else:
                # self.updateCustomer_PrimaryKey_LineEdit.setText("username has been found")
                for row1 in row:
                    self.updateCustomer_Name_LineEdit.setText(str(row1[0]))
                    self.updateCustomer_Contact_LineEdit.setText(str(row1[1]))
                    self.updateCustomer_Email_LineEdit.setText(str(row1[2]))
                    self.updateCustomer_Address_LineEdit.setText(str(row1[3]))
                    self.updateCustomer_Gender_LineEdit.setText(str(row1[4]))
        except mc.Error as e:
            self.updateCustomer_Name_LineEdit("Error in connection")

    def delete_Customer_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            contact2 = str(self.delete_Customer_contact_primaryKey_LineEdit.text())
            Name1 = str(self.delete_Customer_Name_LineEdit.text())
            contact1 = str(self.delete_Customer_Contact_LineEdit.text())
            Email1 = str(self.delete_Customer_Email_LineEdit.text())
            Address1 = str(self.delete_Customer_Address_LineEdit.text())
            Gender1 = str(self.delete_Customer_Gender_LineEdit.text())

            query1 = ("DELETE FROM customer_table WHERE Name = '%s'" % (Name1))
            query2 = ("DELETE FROM customer_table WHERE contact = '%s'" % (contact1))
            query3 = ("DELETE FROM customer_table WHERE Email = '%s'" % (Email1))
            query4 = ("DELETE FROM customer_table WHERE Address = '%s'" % (Address1))
            query5 = ("DELETE FROM customer_table WHERE Gender = '%s'" % (Gender1))

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            mycursor.execute(query2)
            mycursor.execute(query3)
            mycursor.execute(query4)
            mycursor.execute(query5)

        except mc.Error as e:
            print("Error in connection")

    def update_Customer_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )
            # query = "UPDATE customer_table SET Name like '",\
            #         +str(self.updateCustomer_Name_LineEdit.text()),\
            #         + "',contact like '" + str(self.updateCustomer_Contact_LineEdit.text()),\
            #         + "',Email like '" + str(self.updateCustomer_Email_LineEdit.text()),\
            #         + "',Address like '" + str(self.updateCustomer_Address_LineEdit.text()),\
            #         + "',Gender like '" + str(self.updateCustomer_Gender_LineEdit.text()),\
            #         + "', WHERE contact like'",\
            #         + str(self.updateCustomer_PrimaryKey_LineEdit.text()) + "'"

            # query = "UPDATE customer_table SET Name,\
            # = str(self.updateCustomer_Name_LineEdit.text()) ,\
            # WHERE contact = str(self.updateCustomer_PrimaryKey_LineEdit.text())"

            # query = "update customer_table set Name,\
            # = str(self.updateCustomer_Name_LineEdit.text()),where,\
            # contact =str(self.updateCustomer_PrimaryKey_LineEdit.text())"
            #
            # query ="""Update customer_table set Name = %s, contact = %d,Email,\
            #  = %s,Address = %s,Gender = %s where contact = %s"""

            contact2 = str(self.updateCustomer_PrimaryKey_LineEdit.text())
            Name1 = str(self.updateCustomer_Name_LineEdit.text())
            contact1 = str(self.updateCustomer_Contact_LineEdit.text())
            Email1 = str(self.updateCustomer_Email_LineEdit.text())
            Address1 = str(self.updateCustomer_Address_LineEdit.text())
            Gender1 = str(self.updateCustomer_Gender_LineEdit.text())

            query1 = ("UPDATE customer_table SET name = '%s' WHERE contact = '%s'" % (Name1, contact2))
            query2 = ("UPDATE customer_table SET contact = '%s'WHERE contact = '%s'" % (contact1, contact2))
            query3 = ("UPDATE customer_table SET Email = '%s'WHERE contact = '%s'" % (Email1, contact2))
            query4 = ("UPDATE customer_table SET Address = '%s'WHERE contact = '%s'" % (Address1, contact2))
            query5 = ("UPDATE customer_table SET Gender = '%s'WHERE contact = '%s'" % (Gender1, contact2))

            mycursor = mydb.cursor()
            mycursor.execute(query1)
            mycursor.execute(query2)
            mycursor.execute(query3)
            mycursor.execute(query4)
            mycursor.execute(query5)

        except mc.Error as e:
            print("Error in connection")

    def show_Customer_Details(self):

        tblname = "customer_table"
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT *  FROM {}".format(tblname))

            result = mycursor.fetchall()

            self.customer_Details_Table.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.customer_Details_Table.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.customer_Details_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error Occured")

    def insert_New_Product_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            mycursor = mydb.cursor()

            P_Name = self.AddItem_ProductName_LineEdit.text()
            Rate = self.AddItem_Rate_LineEdit.text()
            Description = self.AddItem_Description_LineEdit.text()

            query = "Insert Into product_table (Pname,Rate,Description) VALUES (%s, %s, %s)"
            value = (P_Name, Rate, Description,)

            mycursor.execute(query, value)

            mydb.commit()
            # self.label_3.setText("Data Inserted")
        except mc.Error as e:
            # self.label_3.setText("Error in inserting data")
            print("Error in inserting data")

    def insert_New_Customer_Details(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="billingdb"
            )

            mycursor = mydb.cursor()

            Name = self.newCustomer_Name_LineEdit.text()
            contact = self.newCustomer_Contact_LineEdit.text()
            Email = self.newCustomer_Email_LineEdit.text()
            Address = self.newCustomer_Address_LineEdit.text()
            Gender = self.newCustomer_Gender_LineEdit.text()
            query = "Insert Into customer_table (Name,contact,Email,Address,Gender) VALUES (%s, %s, %s, %s, %s)"
            value = (Name, contact, Email, Address, Gender)

            mycursor.execute(query, value)

            mydb.commit()
            # self.label_3.setText("Data Inserted")
        except mc.Error as e:
            # self.label_3.setText("Error in inserting data")
            print("Error in inserting data")


class UIFunctions(WelcomeScreen):
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.toggle_frame.width()
            maxExtend = maxWidth
            standard = 56

            # SET MAX WIDTH
            if width == 56:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.toggle_frame, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animation.start()


app = QApplication([])
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setGeometry(250, 120, 1400, 800)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")
