class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def display_candidates(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(f"- {candidate}")

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Vote for {candidate} recorded successfully!")
        else:
            print(f"{candidate} is not a valid candidate. Please choose from the following candidates:")
            self.display_candidates()

    def display_results(self):
        print("Voting Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")


# Example usage:
candidates_list = ["Candidate A", "Candidate B", "Candidate C"]
voting_system = VotingSystem(candidates_list)

print("Welcome to the Voting System!")
voting_system.display_candidates()

while True:
    user_input = input("Enter the name of the candidate you want to vote for (or 'exit' to end): ")

    if user_input.lower() == 'exit':
        break

    voting_system.vote(user_input)

print("\nVoting has ended. Here are the final results:")
voting_system.display_results()
