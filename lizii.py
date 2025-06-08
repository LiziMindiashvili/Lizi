from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from expenses_ui import Ui_MainWindow

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.total = 0

        # თუ ComboBox-ში კატეგორიები არ გაქვს UI-ში, აქ დაამატე
        if self.ui.categoryBox.count() == 0:
            self.ui.categoryBox.addItems(["საკვები", "ტრანსპორტი", "გართობა"])

        self.ui.addButton.clicked.connect(self.add_expense)

    def add_expense(self):
        text = self.ui.amountInput.text()
        try:
            amount = float(text)
        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "გთხოვ შეიყვანე რიცხვი")
            return

        self.total += amount
        self.ui.totalLabel.setText(f"ჯამური ხარჯი: {self.total} ₾")
        self.ui.amountInput.clear()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())