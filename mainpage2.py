# Form implementation generated from reading ui file 'mainpage2.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_Frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_Frame.sizePolicy().hasHeightForWidth())
        self.top_Frame.setSizePolicy(sizePolicy)
        self.top_Frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_Frame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 127);\n"
"border-bottom: 1px solid #000;\n"
"}")
        self.top_Frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.top_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_Frame.setObjectName("top_Frame")
        self.toggle_Frame = QtWidgets.QFrame(self.top_Frame)
        self.toggle_Frame.setGeometry(QtCore.QRect(0, 0, 56, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_Frame.sizePolicy().hasHeightForWidth())
        self.toggle_Frame.setSizePolicy(sizePolicy)
        self.toggle_Frame.setMinimumSize(QtCore.QSize(56, 40))
        self.toggle_Frame.setMaximumSize(QtCore.QSize(56, 40))
        self.toggle_Frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.toggle_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.toggle_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.toggle_Frame.setObjectName("toggle_Frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_Frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toggle_btn = QtWidgets.QPushButton(self.toggle_Frame)
        self.toggle_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.toggle_btn.setMaximumSize(QtCore.QSize(56, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toggle_btn.setFont(font)
        self.toggle_btn.setStyleSheet("QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"\n"
"")
        self.toggle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/toggle.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toggle_btn.setIcon(icon)
        self.toggle_btn.setIconSize(QtCore.QSize(40, 40))
        self.toggle_btn.setObjectName("toggle_btn")
        self.verticalLayout_2.addWidget(self.toggle_btn)
        self.verticalLayout.addWidget(self.top_Frame)
        self.lower_Frame = QtWidgets.QFrame(self.centralwidget)
        self.lower_Frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lower_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lower_Frame.setObjectName("lower_Frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.lower_Frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_Toggle_menu = QtWidgets.QFrame(self.lower_Frame)
        self.left_Toggle_menu.setMaximumSize(QtCore.QSize(56, 16777215))
        self.left_Toggle_menu.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.096, y1:0.118636, x2:1, y2:1, stop:0 rgba(255, 153, 51, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"padding:5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"}")
        self.left_Toggle_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_Toggle_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_Toggle_menu.setObjectName("left_Toggle_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_Toggle_menu)
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu_btns = QtWidgets.QFrame(self.left_Toggle_menu)
        self.menu_btns.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.menu_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_btns.setObjectName("menu_btns")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_btns)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.create_Invoice_Btn = QtWidgets.QPushButton(self.menu_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_Invoice_Btn.sizePolicy().hasHeightForWidth())
        self.create_Invoice_Btn.setSizePolicy(sizePolicy)
        self.create_Invoice_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.create_Invoice_Btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.create_Invoice_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Create Invoice.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.create_Invoice_Btn.setIcon(icon1)
        self.create_Invoice_Btn.setIconSize(QtCore.QSize(40, 40))
        self.create_Invoice_Btn.setObjectName("create_Invoice_Btn")
        self.verticalLayout_4.addWidget(self.create_Invoice_Btn)
        self.new_Customer_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.new_Customer_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.new_Customer_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Add User1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.new_Customer_Btn.setIcon(icon2)
        self.new_Customer_Btn.setIconSize(QtCore.QSize(40, 40))
        self.new_Customer_Btn.setObjectName("new_Customer_Btn")
        self.verticalLayout_4.addWidget(self.new_Customer_Btn)
        self.update_Customer_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.update_Customer_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.update_Customer_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/update customer1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.update_Customer_Btn.setIcon(icon3)
        self.update_Customer_Btn.setIconSize(QtCore.QSize(40, 40))
        self.update_Customer_Btn.setObjectName("update_Customer_Btn")
        self.verticalLayout_4.addWidget(self.update_Customer_Btn)
        self.customer_Details_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.customer_Details_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.customer_Details_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Customer_Details1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.customer_Details_Btn.setIcon(icon4)
        self.customer_Details_Btn.setIconSize(QtCore.QSize(40, 40))
        self.customer_Details_Btn.setObjectName("customer_Details_Btn")
        self.verticalLayout_4.addWidget(self.customer_Details_Btn)
        self.delete_Customer_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.delete_Customer_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.delete_Customer_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Delete customer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_Customer_Btn.setIcon(icon5)
        self.delete_Customer_Btn.setIconSize(QtCore.QSize(40, 40))
        self.delete_Customer_Btn.setObjectName("delete_Customer_Btn")
        self.verticalLayout_4.addWidget(self.delete_Customer_Btn)
        self.add_Item_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.add_Item_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.add_Item_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/Add item.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_Item_Btn.setIcon(icon6)
        self.add_Item_Btn.setIconSize(QtCore.QSize(40, 40))
        self.add_Item_Btn.setObjectName("add_Item_Btn")
        self.verticalLayout_4.addWidget(self.add_Item_Btn)
        self.update_Item_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.update_Item_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.update_Item_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/Update Item.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.update_Item_Btn.setIcon(icon7)
        self.update_Item_Btn.setIconSize(QtCore.QSize(40, 40))
        self.update_Item_Btn.setObjectName("update_Item_Btn")
        self.verticalLayout_4.addWidget(self.update_Item_Btn)
        self.item_Details_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.item_Details_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.item_Details_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/Item Details.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.item_Details_Btn.setIcon(icon8)
        self.item_Details_Btn.setIconSize(QtCore.QSize(40, 40))
        self.item_Details_Btn.setObjectName("item_Details_Btn")
        self.verticalLayout_4.addWidget(self.item_Details_Btn)
        self.delete_Item_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.delete_Item_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.delete_Item_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/Delete item.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_Item_Btn.setIcon(icon9)
        self.delete_Item_Btn.setIconSize(QtCore.QSize(40, 40))
        self.delete_Item_Btn.setObjectName("delete_Item_Btn")
        self.verticalLayout_4.addWidget(self.delete_Item_Btn)
        self.logout_Btn = QtWidgets.QPushButton(self.menu_btns)
        self.logout_Btn.setMinimumSize(QtCore.QSize(100, 0))
        self.logout_Btn.setStyleSheet("QPushButton {\n"
"text-align:left;\n"
"padding-left:70px;\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/Logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logout_Btn.setIcon(icon10)
        self.logout_Btn.setIconSize(QtCore.QSize(40, 40))
        self.logout_Btn.setObjectName("logout_Btn")
        self.verticalLayout_4.addWidget(self.logout_Btn)
        self.verticalLayout_3.addWidget(self.menu_btns)
        self.horizontalLayout.addWidget(self.left_Toggle_menu)
        self.content_Page = QtWidgets.QFrame(self.lower_Frame)
        self.content_Page.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content_Page.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.content_Page.setObjectName("content_Page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content_Page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_Page)
        self.stackedWidget.setStyleSheet("background-image: url(:/newPrefix/cashier-supermarket-billing-software-pos-pchvector-e1584790103322.jpg);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.content_Page)
        self.verticalLayout.addWidget(self.lower_Frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_Invoice_Btn.setText(_translate("MainWindow", "    Create Invoice"))
        self.new_Customer_Btn.setText(_translate("MainWindow", "  New Customer"))
        self.update_Customer_Btn.setText(_translate("MainWindow", "  Update Customer"))
        self.customer_Details_Btn.setText(_translate("MainWindow", "  Customer Details"))
        self.delete_Customer_Btn.setText(_translate("MainWindow", "  Delete Customer"))
        self.add_Item_Btn.setText(_translate("MainWindow", "  Add Item             "))
        self.update_Item_Btn.setText(_translate("MainWindow", "  Update Item       "))
        self.item_Details_Btn.setText(_translate("MainWindow", "  Item Details       "))
        self.delete_Item_Btn.setText(_translate("MainWindow", "  Delete Item        "))
        self.logout_Btn.setText(_translate("MainWindow", "   Logout                "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
