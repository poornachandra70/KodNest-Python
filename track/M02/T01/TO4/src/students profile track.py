class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score=0.0,
        skills=None,
        is_placed=False
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = [] if skills is None else list(skills)
        self.is_placed = is_placed

    def __str__(self):
        skills_text = (
            ", ".join(self.skills)
            if self.skills
            else "Not Added"
        )

        placement_status = (
            "Placed" if self.is_placed
            else "Not Placed"
        )

        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Skills: {skills_text}\n"
            f"Placement Status: {placement_status}"
        )

student = StudentProfile(
    student_id=101,
    name="deepak",
    course="Python",
    score=99.6,
    skills=["Python"],
    is_placed=True
)
print(student)

