from PySide2.QtWidgets import QTreeView
from PySide2.QtGui import QStandardItem, QStandardItemModel

from timecard.data import TimeLog

# Datestamp | Description | Duration


class LogView:
    model = QStandardItemModel(0, 3)
    view = QTreeView()

    @classmethod
    def build(cls):
        cls.model.setHorizontalHeaderLabels(
            ("Date", "Activity", "Duration")
        )
        # TODO: Lock data types
        cls.view.setModel(cls.model)
        #cls.view.setEditTriggers(QTreeView.EditTrigger.DoubleClicked)
        cls.load_data()
        return cls.view

    @classmethod
    def load_data(cls):
        for entry in TimeLog.log:
            cls.model.appendRow((
                QStandardItem(entry[0]),
                QStandardItem(entry[2]),
                QStandardItem(entry[1])
            ))