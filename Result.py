class Student:
    def __init__(self):
        self._name_ = ""
        self._marks_ = []
        self._total_ = 0
        self._percentage_ = 0
        self._grade_ = ""
        self._result_ = ""

    def Set_Student(self):
        self._name_ = input("\nEnter Name: ")
        print("\nEnter marks of 5 subjects: \n")
        for i in range(5):
            self._marks_.append(int(input("Subject " + str(i + 1) + ": ")))

    def total_calc(self):
        for x in self._marks_:
            self._total_ += x

    def Percentage_calc(self):
        self._percentage_ = self._total_ / 5

    def Grade_calc(self):
        if self._percentage_ <= 45:
            self._grade_ = "Third Divison"
        elif self._percentage_ >= 45 and self._percentage_ <60:
            self._grade_ = "Second Divison"
        elif self._percentage_ >= 60:
            self._grade_ = "First Division"

    def Result_calc(self):
        count = 0
        for x in self._marks_:
            if x >= 33:
                count += 1
        if count == 5:
            self._result_ = "Pass"
        else:
            self._result_ = "FAIL"

    def Show_student(self):
        self.total_calc()
        self.Percentage_calc()
        self.Grade_calc()
        self.Result_calc()
        print("\nStudent's name:\t", self._name_)
        print("The total marks is:\t", self._total_)
        print("The percentage is:\t", self._percentage_)
        print("The result is:\t", self._result_)
        print("Division:\t", self._grade_)


def main():
    # Student object
    s = Student()
    s.Set_Student()
    s.Show_student()


if __name__ == '__main__':
    main()
