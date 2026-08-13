class JobDescription:

    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"


class PlacementManager:

    def __init__(self):
        self.job_descriptions = []

    def add_job_description(self, job_description):
        self.job_descriptions.append(job_description)

    def find_job_by_id(self, job_id):
        # Receive a job ID and search the stored job objects one by one
        for job in self.job_descriptions:
            if job.job_id == job_id:
                # Return the complete matching object if found
                return job
        # Return None if no matching job is found
        return None


# Read the number of jobs
n = int(input())

manager = PlacementManager()

# Read job details and add them to the manager
for _ in range(n):
    job_id = int(input())
    company = input()
    role = input()
    job = JobDescription(job_id, company, role)
    manager.add_job_description(job)

# Read the job ID to search for
search_id = int(input())

# Search for the job description
result = manager.find_job_by_id(search_id)

# Display the output as per requirements
if result:
    print(result)
else:
    print(f"Job description with ID {search_id} not found")