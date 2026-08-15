class CandidateProfile:
    def __init__(self, name, email, score):
        # Create a public name attribute
        self.name = name

        # Create a protected email attribute
        self._email = email

        # Create a private score attribute
        self.__score = score

    def get_email(self):
        # Return the protected email
        return self._email

    def get_score(self):
        # Return the private score
        return self.__score


name = input().strip()
email = input().strip()
score = int(input())

# Create one CandidateProfile object
candidate = CandidateProfile(name, email, score)

# Print the name directly
print("CANDIDATE PROFILE")
print("Name:", candidate.name)

# Print the email using get_email()
print("Email:", candidate.get_email())

# Print the score using get_score()
print("Score:", candidate.get_score())