from task1 import Student

# 2. 중급 문제


## 문제 3: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        avg_score = sum(self.scores) / len(self.scores)
        return round(avg_score, 4)

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요.
        # YOUR CODE HERE

        if hours >= 5:
            self.add_score(100)
        elif hours >= 3:
            self.add_score(50)
        elif hours >= 1:
            self.add_score(30)
        else:
            self.add_score(0)


# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
gs = GradedStudent("철수", 10, 3)
gs.study(2)
gs.study(2)
gs.study(4)
print("평균 점수: ", gs.calculate_average())
