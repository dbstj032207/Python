# import game.sound.echo
# import game.graphic.render
# import game.mylib
#
# game.sound.echo.echo_test()
# game.graphic.render.render_test()
#
# cal = game.mylib.Calculator(10, 20)
# print(cal.sum())

print("--------------------------------------")

# import game.sound.echo as soundecho
# import game.graphic.render as rendering
# import game.mylib as my
#
# soundecho.echo_test()
# rendering.render_test()
# cal = my.Calculator(10, 20)
# print(cal.sum())

print("--------------------------------------")

# from game.mylib import COMPANY, Calculator, info
#
# print(COMPANY)
# cal = Calculator(100, 100)
# print(cal.sum())
# info(80, 170, name="홍길동", age=20)

print("--------------------------------------")

# from game.mylib import *
#
# print(COMPANY)
# cal = Calculator(100, 100)
# print(cal.sum())
# info(80, 170, name="홍길동", age=20)

print("--------------------------------------")

# from game.mylib import Calculator as calc
#
# cal = calc(10, 10)
# print(cal.sum())

print("--------------------------------------")

import sys
sys.path.append("C:\\PythonWork")

from game.mylib import Calculator as calc

cal = calc(10, 10)
print(cal.sum())


