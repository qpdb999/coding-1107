
'''
객체지향 프로그래밍 심화

    오늘 배운 내용

이번에는 파이썬의 객체지향 프로그래밍을 더 깊게 학습했다.

클래스와 객체의 기본 개념을 복습하고,
인스턴스 변수와 클래스 변수의 차이,
인스턴스 메서드와 클래스 메서드, 정적 메서드,
상속과 메서드 오버라이딩, 캡슐화에 대해 알아보았다.

    정의

1) 인스턴스 변수와 클래스 변수

인스턴스 변수는 객체마다 각각 다른 값을 저장하는 변수이다.
클래스 변수는 클래스에 속하며, 해당 클래스로 생성된 객체들이 함께 사용하는 변수이다.

2) 인스턴스 메서드

객체의 데이터를 사용하거나 변경하는 메서드이다.
첫 번째 매개변수로 self를 사용한다.

3) 클래스 메서드

클래스 자체의 데이터를 다루는 메서드이다.
@classmethod를 사용하며, 첫 번째 매개변수로 cls를 사용한다.

4) 정적 메서드

객체나 클래스의 변수에 직접 접근하지 않고,
독립적인 기능을 수행하는 메서드이다.
@staticmethod를 사용한다.

5) 상속

기존 클래스의 변수와 메서드를 새로운 클래스에서 물려받아 사용하는 기능이다.

6) 메서드 오버라이딩

자식 클래스에서 부모 클래스의 메서드를
자신에게 맞게 다시 정의하는 것이다.

7) 캡슐화

객체의 내부 데이터를 직접 변경하지 못하도록 제한하고,
메서드를 통해 안전하게 접근하도록 만드는 개념이다.

    사용 방법

1) 인스턴스 변수와 클래스 변수

class Student:
    school = "성일정보고"

    def __init__(self, name):
        self.name = name

student1 = Student("철수")
student2 = Student("영희")

print(student1.name)
print(student2.name)
print(Student.school)

2) 인스턴스 메서드, 클래스 메서드, 정적 메서드

class Calculator:
    count = 0

    def add(self, a, b):
        return a + b

    @classmethod
    def show_count(cls):
        return cls.count

    @staticmethod
    def multiply(a, b):
        return a * b

calc = Calculator()

print(calc.add(3, 5))
print(Calculator.show_count())
print(Calculator.multiply(3, 5))

3) 상속과 메서드 오버라이딩

class Animal:
    def sound(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def sound(self):
        print("멍멍!")

dog = Dog()
dog.sound()

4) 캡슐화

class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def show_score(self):
        print(self.__score)

student = Student("철수", 90)
student.show_score()

    코드 분석

1) 인스턴스 변수와 클래스 변수

student1과 student2는 각각 다른 이름을 저장한다.
하지만 school은 클래스에 선언되어 두 객체가 함께 사용할 수 있다.

2) 메서드의 종류

add()는 self를 사용하여 객체의 기능을 수행한다.
show_count()는 cls를 통해 클래스 변수에 접근한다.
multiply()는 객체나 클래스의 상태에 의존하지 않고 계산을 수행한다.

3) 상속과 오버라이딩

Dog 클래스는 Animal 클래스를 상속받는다.
Dog에서 sound()를 다시 정의했기 때문에
Dog 객체에서는 부모 클래스의 메서드 대신 자식 클래스의 메서드가 실행된다.

4) 캡슐화

__score처럼 변수 이름 앞에 밑줄 두 개를 붙이면
클래스 외부에서 해당 변수에 직접 접근하기 어렵게 만들 수 있다.
대신 show_score()와 같은 메서드를 통해 값을 확인할 수 있다.

    복습하면서 알게 된 점

객체지향 프로그래밍은 단순히 클래스를 만들고 객체를 생성하는 것뿐만 아니라,
데이터와 기능을 어떻게 관리할지 정하는 것도 중요하다는 것을 알게 되었다.

특히 상속을 사용하면 기존 코드를 재사용할 수 있고,
오버라이딩을 활용하면 자식 클래스에 맞는 기능으로 변경할 수 있다는 점을 이해했다.

📌 AI 활용 복습 문제

1) 인스턴스 변수와 클래스 변수의 차이점은?

정답: 인스턴스 변수는 객체마다 별도로 저장되고,
클래스 변수는 같은 클래스를 사용하는 객체들이 공유한다.

2) 클래스 메서드에서 사용하는 첫 번째 매개변수는?

정답: cls

3) 정적 메서드를 선언할 때 사용하는 데코레이터는?

정답: @staticmethod

4) 상속이란 무엇인가?

정답: 부모 클래스의 변수와 메서드를 자식 클래스에서 물려받아 사용하는 기능이다.

5) 메서드 오버라이딩이란?

정답: 자식 클래스에서 부모 클래스의 메서드를 다시 정의하는 것이다.

6) 캡슐화에서 변수 이름 앞에 사용하는 표시는?

정답: 밑줄 두 개(__)
'''
