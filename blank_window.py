## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget


# QWidget은 부모 클래스
# 부모 클래스를 상속받아서 MyApp이라는 클래스를 생성
class MyApp(QWidget):

    def __init__(self):
        # super는 부모 클래스를 가리킴
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창의 이름을 설정
        self.setWindowTitle('MyApp')
        # 창을 띄우는 초기 위치
        self.move(1000, 100)
        # 창의 크기
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
