class StudentProfile:
    def __init__(self, student_id, name, score, skills):
        # Create safe private starting values
        self.__student_id = int(student_id)
        self.__name = "Unknown"
        self.__score = 0
        self.__skills = []

        # Initialize the properties and skills safely
        self.name = name
        self.score = score
        for skill in skills:
            self.add_skill(skill)

    @property
    def student_id(self):
        # Return the read-only student ID
        return self.__student_id

    @property
    def name(self):
        # Return the private name
        return self.__name

    @name.setter
    def name(self, new_name):
        cleaned_name = new_name.strip()
        if cleaned_name:
            self.__name = cleaned_name

    @property
    def score(self):
        # Return the private score
        return self.__score

    @score.setter
    def score(self, new_score):
        # Accept only scores from 0 to 100
        if 0 <= new_score <= 100:
            self.__score = new_score

    @property
    def skills(self):
        # Return a tuple containing the skills
        return tuple(self.__skills)

    def add_skill(self, new_skill):
        cleaned_skill = new_skill.strip()
        if cleaned_skill and cleaned_skill not in self.__skills:
            self.__skills.append(cleaned_skill)

    def __str__(self):
        skills_str = ", ".join(self.__skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {skills_str}"
        )


if __name__ == "__main__":
    sid = int(input())
    sname = input()
    sscore = int(input())
    sskills = [s.strip() for s in input().split(",")]
    new_score = int(input())
    new_skill = input()

    student = StudentProfile(sid, sname, sscore, sskills)
    student.score = new_score
    student.add_skill(new_skill)
    print(student)