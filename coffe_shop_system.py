import sys
import os
import datetime
import time
import random

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

class Cafe(QWidget):
    def __init__(self):
        super().__init__()
        self.setupui_cafe()

    def setupui_cafe(self):
        self.resize(1366, 768)
        self.move(60, 80)
        self.setWindowTitle("Coffee Shop System")

    #----------Title----------#
        self.label_title = QLabel("COFFEE SHOP SYSTEM")
        self.label_title.setObjectName("pseudolabel1")

        hbox_label_title = QHBoxLayout()
        hbox_label_title.addWidget(self.label_title)

    #----------Hot Drinks Info----------#
        self.groupbox_hot_drinks = QGroupBox("Hot Drinks")

        self.label_turkish_coffee = QLabel("Turkish Coffee")
        self.label_turkish_coffee_price = QLabel("2$")

        self.label_espresso = QLabel("Espresso")
        self.label_espresso_price = QLabel("3$")

        self.label_cappuccino = QLabel("Cappuccino")
        self.label_cappuccino_price = QLabel("4$")

        self.label_hot_chocolate = QLabel("Hot Chocolate")
        self.label_hot_chocolate_price = QLabel("6$")

        self.label_green_tea = QLabel("Green Tea")
        self.label_green_tea_price = QLabel("5$")

        grid_hot_drinks = QGridLayout()
        grid_hot_drinks.addWidget(self.label_turkish_coffee, 0, 0)
        grid_hot_drinks.addWidget(self.label_turkish_coffee_price, 0, 1)
        grid_hot_drinks.addWidget(self.label_espresso, 1, 0)
        grid_hot_drinks.addWidget(self.label_espresso_price, 1, 1)
        grid_hot_drinks.addWidget(self.label_cappuccino, 2, 0)
        grid_hot_drinks.addWidget(self.label_cappuccino_price, 2, 1)
        grid_hot_drinks.addWidget(self.label_hot_chocolate, 3, 0)
        grid_hot_drinks.addWidget(self.label_hot_chocolate_price, 3, 1)
        grid_hot_drinks.addWidget(self.label_green_tea, 4, 0)
        grid_hot_drinks.addWidget(self.label_green_tea_price, 4, 1)

        vbox_hot_drinks = QVBoxLayout()
        vbox_hot_drinks.addLayout(grid_hot_drinks)
        self.groupbox_hot_drinks.setLayout(vbox_hot_drinks)

    #----------Cold Drinks Info----------#
        self.groupbox_cold_drinks = QGroupBox("Cold Drinks")

        self.label_iced_tea = QLabel("Iced Tea")
        self.label_iced_tea_price = QLabel("4$")

        self.label_frappeccino = QLabel("Frappeccino")
        self.label_frappeccino_price = QLabel("5$")

        self.label_milk_shake = QLabel("Milk Shake")
        self.label_milk_shake_price = QLabel("6$")

        self.label_smoothies = QLabel("Fruit Smoothies")
        self.label_smoothies_price = QLabel("7$")

        self.label_soft_drinks = QLabel("Soft Drinks")
        self.label_soft_drinks_price = QLabel("3$")

        grid_cold_drinks = QGridLayout()
        grid_cold_drinks.addWidget(self.label_iced_tea, 0, 0)
        grid_cold_drinks.addWidget(self.label_iced_tea_price, 0, 1)
        grid_cold_drinks.addWidget(self.label_frappeccino, 1, 0)
        grid_cold_drinks.addWidget(self.label_frappeccino_price, 1, 1)
        grid_cold_drinks.addWidget(self.label_milk_shake, 2, 0)
        grid_cold_drinks.addWidget(self.label_milk_shake_price, 2, 1)
        grid_cold_drinks.addWidget(self.label_smoothies, 3, 0)
        grid_cold_drinks.addWidget(self.label_smoothies_price, 3, 1)
        grid_cold_drinks.addWidget(self.label_soft_drinks, 4, 0)
        grid_cold_drinks.addWidget(self.label_soft_drinks_price, 4, 1)

        vbox_cold_drinks = QVBoxLayout()
        vbox_cold_drinks.addLayout(grid_cold_drinks)
        self.groupbox_cold_drinks.setLayout(vbox_cold_drinks)
    
    #----------Calculator----------#
        self.groupbox_calculator = QGroupBox("Calculator")

        self.lineEditInput = QLineEdit()
        self.lineEditInput.setAlignment(Qt.AlignRight)
        self.lineEditInput.setFont(QFont('Sanserif', 14))
        self.lineEditInput.setDisabled(True)

        self._7Button = QPushButton('7')
        self._8Button = QPushButton('8')
        self._9Button = QPushButton('9')
        self.clearButton = QPushButton('CE')

        self._4Button = QPushButton('4')
        self._5Button = QPushButton('5')
        self._6Button = QPushButton('6')
        self.multiplyButton = QPushButton('*')

        self._1Button = QPushButton('1')
        self._2Button = QPushButton('2')
        self._3Button = QPushButton('3')
        self.divideButton = QPushButton('/')

        self._0Button = QPushButton('0')
        self.pointButton = QPushButton('.')
        self.substractButton = QPushButton('-')
        self.addButton = QPushButton('+')

        self.percentButton = QPushButton('%')
        self.equalButton = QPushButton('=')

        layout = QGridLayout()
        layout.addWidget(self.lineEditInput, 0, 0, 1, 4)
        layout.addWidget(self._7Button, 1, 0)
        layout.addWidget(self._8Button, 1, 1)
        layout.addWidget(self._9Button, 1, 2)
        layout.addWidget(self.clearButton, 1, 3)

        layout.addWidget(self._4Button, 2, 0)
        layout.addWidget(self._5Button, 2, 1)
        layout.addWidget(self._6Button, 2, 2)
        layout.addWidget(self.multiplyButton, 2, 3)

        layout.addWidget(self._1Button, 3, 0)
        layout.addWidget(self._2Button, 3, 1)
        layout.addWidget(self._3Button, 3, 2)
        layout.addWidget(self.divideButton, 3, 3)

        layout.addWidget(self._0Button, 4, 0)
        layout.addWidget(self.pointButton, 4, 1)
        layout.addWidget(self.substractButton, 4, 2)
        layout.addWidget(self.addButton, 4, 3)

        layout.addWidget(self.percentButton, 5, 0)
        layout.addWidget(self.equalButton, 5, 1, 1, 3)

        vbox_calculator = QVBoxLayout()
        vbox_calculator.addLayout(layout)
        self.groupbox_calculator.setLayout(vbox_calculator)

    #----------Customer Data----------#
        self.groupbox_dtcustomer = QGroupBox("Customer Data")

        self.label_dtreference = QLabel("Customer No")
        self.edit_dtreference = QLineEdit()

        self.label_dtturkish_coffee = QLabel("Turkish Coffee")
        self.edit_dtturkish_coffee = QLineEdit("0")

        self.label_dtespresso = QLabel("Espresso")
        self.edit_dtespresso = QLineEdit("0")

        self.label_dtcappucino = QLabel("Cappuccino")
        self.edit_dtcappuccino = QLineEdit("0")

        self.label_dthot_chocolate = QLabel("Hot Chocolate")
        self.edit_dthot_chocolate = QLineEdit("0")

        self.label_dtgreen_tea = QLabel("Green Tea")
        self.edit_dtgreen_tea = QLineEdit("0")

        self.label_dticed_tea = QLabel("Iced Tea")
        self.edit_dticed_tea = QLineEdit("0")

        self.label_dtfrappecino = QLabel("Frappecino")
        self.edit_dtfrappecino = QLineEdit("0")

        self.label_dtmilk_shake = QLabel("Milk Shake")
        self.edit_dtmilk_shake = QLineEdit("0")

        self.label_dtsmoothies = QLabel("Smoothies")
        self.edit_dtsmoothies = QLineEdit("0")

        self.label_dtsoft_drinks = QLabel("Soft Drinks")
        self.edit_dtsoft_drinks = QLineEdit("0")

        grid_dtcustomer = QGridLayout()
        grid_dtcustomer.addWidget(self.label_dtreference, 0, 0)
        grid_dtcustomer.addWidget(self.edit_dtreference, 0, 1)
        grid_dtcustomer.addWidget(self.label_dtturkish_coffee, 1, 0)
        grid_dtcustomer.addWidget(self.edit_dtturkish_coffee, 1, 1)
        grid_dtcustomer.addWidget(self.label_dtespresso, 2, 0)
        grid_dtcustomer.addWidget(self.edit_dtespresso, 2, 1)
        grid_dtcustomer.addWidget(self.label_dtcappucino, 3, 0)
        grid_dtcustomer.addWidget(self.edit_dtcappuccino, 3, 1)
        grid_dtcustomer.addWidget(self.label_dthot_chocolate, 4, 0)
        grid_dtcustomer.addWidget(self.edit_dthot_chocolate, 4, 1)
        grid_dtcustomer.addWidget(self.label_dtgreen_tea, 5, 0)
        grid_dtcustomer.addWidget(self.edit_dtgreen_tea, 5, 1)

        grid_dtcustomer.addWidget(self.label_dticed_tea, 1, 2)
        grid_dtcustomer.addWidget(self.edit_dticed_tea, 1, 3)
        grid_dtcustomer.addWidget(self.label_dtfrappecino, 2, 2)
        grid_dtcustomer.addWidget(self.edit_dtfrappecino, 2, 3)
        grid_dtcustomer.addWidget(self.label_dtmilk_shake, 3, 2)
        grid_dtcustomer.addWidget(self.edit_dtmilk_shake, 3, 3)
        grid_dtcustomer.addWidget(self.label_dtsmoothies, 4, 2)
        grid_dtcustomer.addWidget(self.edit_dtsmoothies, 4, 3)
        grid_dtcustomer.addWidget(self.label_dtsoft_drinks, 5, 2)
        grid_dtcustomer.addWidget(self.edit_dtsoft_drinks, 5, 3)

        vbox_dtcustomer = QVBoxLayout()
        vbox_dtcustomer.addLayout(grid_dtcustomer)
        self.groupbox_dtcustomer.setLayout(vbox_dtcustomer)

    #----------Charge----------#
        self.groupbox_charge = QGroupBox("Bill")

        self.label_subtotal = QLabel("Sub-Total")
        self.edit_subtotal = QLineEdit("0.00")

        self.label_discount = QLabel("Discount")
        self.edit_discount = QLineEdit("0.00")

        self.label_service_charge = QLabel("Service Charge")
        self.edit_service_charge = QLineEdit("2.00")

        self.label_additional_charge = QLabel("Additional Charge")
        self.edit_additional_charge = QLineEdit("0.00")

        self.label_taxvat = QLabel("VAT Tax 11%")
        self.edit_taxvat = QLineEdit("0.00")

        self.label_cccharge = QLabel("Credit Card Charge")
        self.edit_cccharge = QLineEdit("0.00")

        self.label_total = QLabel("Total")
        self.edit_total = QLineEdit("0.00")

        grid_charge = QGridLayout()
        grid_charge.addWidget(self.label_subtotal, 0, 0)
        grid_charge.addWidget(self.edit_subtotal, 0, 1)
        grid_charge.addWidget(self.label_discount, 1, 0)
        grid_charge.addWidget(self.edit_discount, 1, 1)
        grid_charge.addWidget(self.label_service_charge, 2, 0)
        grid_charge.addWidget(self.edit_service_charge, 2, 1)
        grid_charge.addWidget(self.label_additional_charge, 3, 0)
        grid_charge.addWidget(self.edit_additional_charge, 3, 1)
        grid_charge.addWidget(self.label_taxvat, 4, 0)
        grid_charge.addWidget(self.edit_taxvat, 4, 1)
        grid_charge.addWidget(self.label_cccharge, 5, 0)
        grid_charge.addWidget(self.edit_cccharge, 5, 1)
        grid_charge.addWidget(self.label_total, 6, 0)
        grid_charge.addWidget(self.edit_total, 6, 1)

        vbox_charge = QVBoxLayout()
        vbox_charge.addLayout(grid_charge)
        self.groupbox_charge.setLayout(vbox_charge)

    #----------Buttons----------#
        self.button_total = QPushButton("Total")
        self.button_reset = QPushButton("Reset")
        self.button_exit = QPushButton("Exit")

        vbox_button = QVBoxLayout()
        vbox_button.addStretch()
        vbox_button.addWidget(self.button_total)
        vbox_button.addWidget(self.button_reset)
        vbox_button.addWidget(self.button_exit)
        vbox_button.addStretch()

    #----------Layout----------#
        layout_hmix1 = QHBoxLayout()
        layout_hmix1.addWidget(self.groupbox_hot_drinks)
        layout_hmix1.addWidget(self.groupbox_cold_drinks)
        layout_hmix1.addWidget(self.groupbox_calculator)

        layout_hmix2 = QHBoxLayout()
        layout_hmix2.addWidget(self.groupbox_dtcustomer)
        layout_hmix2.addWidget(self.groupbox_charge)
        layout_hmix2.addLayout(vbox_button)
        

        layout_vmix1 = QVBoxLayout()
        layout_vmix1.addLayout(hbox_label_title)
        layout_vmix1.addLayout(layout_hmix1)
        layout_vmix1.addLayout(layout_hmix2)

        self.setLayout(layout_vmix1)

    #----------Total Charge Signal and Slot----------#
        self.button_exit.clicked.connect(self.button_exit_click)
        self.button_reset.clicked.connect(self.button_reset_click)
        self.button_total.clicked.connect(self.button_total_click)

    #----------Calculator Signal and Slot----------#
        self._0Button.clicked.connect(lambda: self.writeDigit(0))
        self._1Button.clicked.connect(lambda: self.writeDigit(1))
        self._2Button.clicked.connect(lambda: self.writeDigit(2))
        self._3Button.clicked.connect(lambda: self.writeDigit(3))
        self._4Button.clicked.connect(lambda: self.writeDigit(4))
        self._5Button.clicked.connect(lambda: self.writeDigit(5))
        self._6Button.clicked.connect(lambda: self.writeDigit(6))
        self._7Button.clicked.connect(lambda: self.writeDigit(7))
        self._8Button.clicked.connect(lambda: self.writeDigit(8))
        self._9Button.clicked.connect(lambda: self.writeDigit(9))

        self.addButton.clicked.connect(lambda: self.writeOperator("+"))
        self.substractButton.clicked.connect(lambda: self.writeOperator("-"))
        self.multiplyButton.clicked.connect(lambda: self.writeOperator("*"))
        self.divideButton.clicked.connect(lambda: self.writeOperator("/"))

        self.pointButton.clicked.connect(self.writePoint)
        self.clearButton.clicked.connect(self.lineEditInput.clear)

        self.equalButton.clicked.connect(self.equalButtonclick)
        self.percentButton.clicked.connect(self.percentButtonclick)

    #----------Calculator Methode----------#
    def writeDigit(self, digit):
        if digit in range(0, 10):
            self.lineEditInput.setText(self.lineEditInput.text() + str(digit))

    def writeOperator(self, operator):
        if len (self.lineEditInput.text()) == 0: return
        if operator in ['*', '/', '+', '-']:
            if self.lineEditInput.text()[-1] in ['*', '/', '+', '-']:
                self.lineEditInput.setText(self.lineEditInput.text()[:-1] + operator)
            else:
                self.lineEditInput.setText(self.lineEditInput.text() + operator)

    def writePoint(self):
        if len (self.lineEditInput.text()) == 0 or self.lineEditInput.text()[-1] in ['*', '/', '+', '-']:
            return
        else:
            self.lineEditInput.setText(self.lineEditInput.text() + '.')

    def equalButtonclick(self):
        expression = self.lineEditInput.text()
        if len(expression) == 0: return
        try:
            result = eval(expression)
            self.lineEditInput.setText(str(result))
        except:
            self.lineEditInput.setText("ERROR!")

    def percentButtonclick(self):
        expression = self.lineEditInput.text()
        if len(expression) == 0: return
        try:
            result = eval(expression)/100
            self.lineEditInput.setText(str(result))
        except:
            self.lineEditInput.setText("ERROR!")
        

    #----------Total Charge Methode----------#
    def button_exit_click(self):
        self.close()

    def button_reset_click(self):
        self.edit_dtreference.setText("")
        self.edit_dtturkish_coffee.setText("0")
        self.edit_dtespresso.setText("0")
        self.edit_dtcappuccino.setText("0")
        self.edit_dthot_chocolate.setText("0")
        self.edit_dtgreen_tea.setText("0")
        self.edit_dticed_tea.setText("0")
        self.edit_dtfrappecino.setText("0")
        self.edit_dtmilk_shake.setText("0")
        self.edit_dtsmoothies.setText("0")
        self.edit_dtsoft_drinks.setText("0")
        

        self.edit_subtotal.setText("0.00")
        self.edit_discount.setText("0.00")
        self.edit_service_charge.setText("2.00")
        self.edit_additional_charge.setText("0.00")
        self.edit_taxvat.setText("0.00")
        self.edit_cccharge.setText("0.00")
        self.edit_total.setText("0.00")

    def button_total_click(self):
        rand_ref = random.randint(0, 10000)
        conv_ref = ("REF-" + str(rand_ref))
        self.edit_dtreference.setText(conv_ref)

        turkish = float(self.edit_dtturkish_coffee.text())
        espresso = float(self.edit_dtespresso.text())
        cappuccino = float(self.edit_dtcappuccino.text())
        hot_chocolate = float(self.edit_dthot_chocolate.text())
        green_tea = float(self.edit_dtgreen_tea.text())

        iced_tea = float(self.edit_dticed_tea.text())
        frappeccino = float(self.edit_dtfrappecino.text())
        milk_shake = float(self.edit_dtmilk_shake.text())
        smoothies = float(self.edit_dtsmoothies.text())
        soft_drinks = float(self.edit_dtsoft_drinks.text())

        cost_turkish = turkish * 2
        cost_espresso = espresso * 3
        cost_cappuccino = cappuccino * 4
        cost_hot_chocolate = hot_chocolate * 6
        cost_green_tea = green_tea * 5
        cost_hot_drinks = cost_turkish + cost_espresso + cost_cappuccino + cost_hot_chocolate + cost_green_tea

        cost_iced_tea = iced_tea * 4
        cost_frappeccino = frappeccino * 5
        cost_milk_shake = milk_shake * 6
        cost_smoothies = smoothies * 7
        cost_soft_drinks  = soft_drinks  * 3
        cost_cold_drinks = cost_iced_tea + cost_frappeccino + cost_milk_shake + cost_smoothies + cost_soft_drinks

        cost_subtotal = cost_hot_drinks + cost_cold_drinks
        conv_cost_subtotal = str("%.2f" %cost_subtotal) + "$"
        self.edit_subtotal.setText(conv_cost_subtotal)

        discount = float(self.edit_discount.text())
        service_charge = float(self.edit_service_charge.text())
        additional_charge = float(self.edit_additional_charge.text())

        taxvat = ((cost_subtotal - discount + service_charge + additional_charge) * 0.11)
        conv_taxvat = str("%.2f" %taxvat) + "$"
        self.edit_taxvat.setText(conv_taxvat)

        cccharge = float(self.edit_cccharge.text())
        cost_total = cost_subtotal - discount + service_charge + additional_charge + taxvat + cccharge
        conv_cost_total = str("%.2f" %cost_total) + "$"
        self.edit_total.setText(conv_cost_total)

    #----------Modern GUI Methode----------#
    def modern_gui(self):
        return """
            Cafe {
                background-color: #112D32;
            }

            QGroupBox {
                font: bold italic 30px Nunito Sans Light;
                color: #88BDBC;
                
            }

            QLabel {
                font: italic 20px Nunito Sans Light;
                color: #88BDBC;
            }

            QLabel#pseudolabel1 {
                qproperty-alignment: AlignCenter;
                font: bold italic 35px Nunito Sans Light;
            }

            QLineEdit {
                font: italic 20px Nunito Sans Light;
                color: #112D32;
                border-style: outset;
                border-radius: 10px;
                min-width: 10em;
                padding: 5px;
                background-color: #88BDBC;
            }

            QPushButton {
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                background-color: #112D32;
                font: italic 20px Nunito Sans Light;
                color: #88BDBC;
                border-color: #88BDBC;
                min-width: 10em;
                padding: 5px;
            }

            QPushButton::hover {
                background-color: #88BDBC;
                color: #112D32;
                border-color: #112D32;
            }

        """

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Cafe()
    app.setStyleSheet(form.modern_gui())
    form.show()

    app.exec_()