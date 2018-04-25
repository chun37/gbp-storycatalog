# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import itertools
import json
import math


def click_button():
    """
    ボタンが押された時のQLineEditの文字列を取得し、取得した文字列が含まれる画像を渡す
    """
    text = inputtext.text()
    if bool(text):
        data = [i for i in basedata if text in i[1]]
    else:
        data = basedata
    setPiclist(data)


def setPiclist(data):
    """
    受け取ったデータを元にグリッドレイアウトを作成し、描画
    """
    mainlayout = QtWidgets.QVBoxLayout()
    under = QtWidgets.QGridLayout()
    top = QtWidgets.QVBoxLayout()
    top.addWidget(inputtext)
    Button = QtWidgets.QPushButton()
    Button.setText("適用")
    top.addWidget(Button)
    mainlayout.addLayout(top)
    mainlayout.addLayout(under)
    widget.setLayout(mainlayout)
    count = 0
    row = math.ceil(len(data) / 4)
    for i, v in itertools.product(range(row), range(4)):
        layout = QtWidgets.QVBoxLayout()
        ImageView = QtWidgets.QGraphicsView()
        ImageView.setFixedSize(147, 83)  # 自分のPCの半分のウィンドウサイズでいい感じに表示されるようにしている
        scene = QtWidgets.QGraphicsScene()
        try:  # 組み合わせ分回してるので必ず過剰にループしてしまうのでIndexError回避
            img_byte = QtCore.QByteArray.fromBase64(
                data[count][2].encode("utf-8"))
        except:
            break
        img = QtGui.QImage()
        img.loadFromData(img_byte)
        item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
        scene.addItem(item)
        ImageView.setScene(scene)
        label = QtWidgets.QLabel(data[count][0])
        label.setFixedSize(147, 12)
        label2 = QtWidgets.QLabel(data[count][1])
        label2.setFixedSize(147, 12)
        layout.addWidget(ImageView)
        layout.addWidget(label)
        layout.addWidget(label2)
        under.addLayout(layout, i, v)
        count += 1

    inner = QtWidgets.QWidget()
    inner.setLayout(mainlayout)
    Button.clicked.connect(click_button)
    widget.setWidget(inner)


if __name__ == '__main__':
    with open("data.json") as f:
        basedata = json.loads(f.read())
    myapp = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QScrollArea()
    inputtext = QtWidgets.QLineEdit()
    widget.setWidgetResizable(True)
    inner = setPiclist(basedata)
    widget.setWidget(inner)
    widget.show()
    sys.exit(myapp.exec_())
