"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def equalThan(self, other):
        """Returns True if the two students have the same name."""
        return self.scores == other.scores

    def lessThan(self, other):
        """Returns True if the current student's name is less than the other student's name."""
        return self.scores < other.scores

    def greaterOrEqual(self, other):
        """Returns True if the current student's name is greater than the other student's name."""
        return self.scores >= other.scores

def main():
    """A simple test."""
    student1 = Student("Alice", 1)
    student2 = Student("Bob", 1)
    student3 = Student("Dani", 1)

    student1.setScore(1, 90)
    student2.setScore(1, 95)
    student3.setScore(1, 90)

    print("Student 1:", student1)
    print("Student 2:", student2)
    print("Student 3:", student3)

    
    print("Is student 1 equal than Student 2?:", student1.equalThan(student2))
    print("Is student 1 equal than Student 3?:", student1.equalThan(student3))
    print("Is student 1 less than than Student 2?:", student1.lessThan(student2))
    print("Is student 1 less than than Student 3?:", student1.lessThan(student3))
    print("Is student 1 greater than Student 2?:", student1.greaterOrEqual(student2))
    print("Is student 1 greater than Student 3?:", student1.greaterOrEqual(student3))

    print("\n")

    print("Is student 2 equal than Student 1?:", student2.equalThan(student1))
    print("Is student 2 equal than Student 3?:", student2.equalThan(student3))
    print("Is student 2 less than than Student 1?:", student2.lessThan(student1))
    print("Is student 2 less than than Student 3?:", student2.lessThan(student3))
    print("Is student 2 greater than Student 1?:", student2.greaterOrEqual(student1))
    print("Is student 2 greater than Student 3?:", student2.greaterOrEqual(student3))

    print("\n")

    print("Is student 3 equal than Student 1?:", student3.equalThan(student1))
    print("Is student 3 equal than Student 2?:", student3.equalThan(student2))
    print("Is student 3 less than than Student 1?:", student3.lessThan(student1))
    print("Is student 3 less than than Student 2?:", student3.lessThan(student2))
    print("Is student 3 greater than Student 1?:", student3.greaterOrEqual(student1))
    print("Is student 3 greater than Student 2?:", student3.greaterOrEqual(student2))

if __name__ == "__main__":
    main()
