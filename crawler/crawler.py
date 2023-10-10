import sys
import os
import csv
from pathlib import Path
import asyncio
import sh
from time import sleep
from datetime import datetime
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from UI.crawler import Ui_W_CRAWLER

sys.path.append(str(Path.cwd().parent))


class Crawler(Ui_W_CRAWLER, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # check box control
        self.cb_rule1.clicked.connect(self.single_checkbox)
        self.cb_rule2.clicked.connect(self.single_checkbox)
        self.cb_rule3.clicked.connect(self.single_checkbox)

        # set datetime
        self.dte_from.setDateTime(datetime.now().replace(microsecond=0, second=0, minute=0, hour=0, day=1))
        self.dte_to.setDateTime(datetime.now().replace(microsecond=0, second=0, minute=0, hour=0))

        # post-crawling
        self.pb_crawling.clicked.connect(self.crawling)
        self.items_checked = []
        self.lw_file_list.itemDoubleClicked.connect(self.item_clicked)

        # File Processing

    @qtc.Slot()
    def single_checkbox(self):
        if self.cb_rule1.isChecked():
            self.cb_rule2.setEnabled(False)
            self.cb_rule3.setEnabled(False)
        elif self.cb_rule2.isChecked():
            self.cb_rule1.setEnabled(False)
            self.cb_rule3.setEnabled(False)
        elif self.cb_rule3.isChecked():
            self.cb_rule1.setEnabled(False)
            self.cb_rule2.setEnabled(False)
        else:
            self.cb_rule1.setEnabled(True)
            self.cb_rule2.setEnabled(True)
            self.cb_rule3.setEnabled(True)

    @qtc.Slot()
    def crawling(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        loop.close()

        for file in sorted(os.listdir(f"{Path.cwd().parent}/data")):
            self.lw_file_list.addItem(f"{Path.cwd().parent}/data/{file}")
        self.le_check_files.setEnabled(True)
        self.le_check_files.setReadOnly(True)
        self.le_check_files.setText("각 파일 확인 필요")

    async def main(self):
        futures = [asyncio.ensure_future(self.tmp_file_writer(fname)) for fname in ('file1', 'file2')]
        return await asyncio.gather(*futures)

    async def tmp_file_writer(self, file_name):
        with open(f"{Path.cwd().parent}/data/{file_name}", 'w') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(['COL1', 'COL2', 'COL3', 'COL4', 'COL5', 'COL6'])
            writer.writerows([['a', 'b', 'c', 'd', self.dte_from.date().getDate(), self.dte_to.date().getDate()], ['e', 'f', 'g', 'h', 'i', self.dte_from.date().getDate(), self.dte_to.date().getDate()]])
        await asyncio.sleep(5)

    def item_clicked(self, item):
        file_path = item.text()
        mvim = sh.mvim.bake(file_path)
        mvim()
        icon = qtg.QIcon()
        icon.addFile(u":/buttons/tick.png", qtc.QSize(), qtg.QIcon.Normal, qtg.QIcon.Off)
        item.setIcon(icon)
        if file_path not in self.items_checked:
            self.items_checked.append(file_path)
        if len(self.items_checked) == self.lw_file_list.count():
            self.pb_processing.setEnabled(True)




if __name__ == "__main__":
    app = qtw.QApplication()

    crawler_window = Crawler()
    crawler_window.show()

    sys.exit(app.exec())


