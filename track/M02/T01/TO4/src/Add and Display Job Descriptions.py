class JobDescription:
    def __init__(self, job_id, company_name, job_role):
        self.job_id = job_id
        self.company_name = company_name
        self.job_role = job_role

    def __str__(self):
        return f"{self.job_id} - {self.company_name} - {self.job_role}"


class PlacementManager:
    def __init__(self):
        self.job_descriptions = []

    def add_job_description(self, job_description):
        # Add the received job object
        self.job_descriptions.append(job_description)

    def display_job_descriptions(self):
        # Handle an empty collection
        if not self.job_descriptions:
            print("No job descriptions available")
        else:
            print("JOB DESCRIPTIONS")
            # Display all job descriptions
            for job in self.job_descriptions:
                print(job)


manager = PlacementManager()

n = int(input())

for _ in range(n):
    job_id = int(input())
    company_name = input().strip()
    job_role = input().strip()
    
    job = JobDescription(job_id, company_name, job_role)
    manager.add_job_description(job)

manager.display_job_descriptions()