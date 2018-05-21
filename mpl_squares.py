import matplotlib.pyplot as pyplot

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
pyplot.plot(input_value, squares, linewidth=5)

# 그래프 제목과 축 레이블을 지정합니다.
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

# 눈금 레이블 크기를 지정합니다.
pyplot.tick_params(axis='both', labelsize=14)

pyplot.show()