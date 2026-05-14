"""
class VotingSystem:
    def __init__(self):
        self.candidate_1, self.candidate_2 = input("Enter 2 candidates name: ").split()

        self.candidate1_votes = 0
        self.candidate2_votes = 0

        self.voters_id = [101, 102, 103, 104]

        self.voted_voters = set()

    def show_candidates(self):
        print(f"\n1. {self.candidate_1}")
        print(f"2. {self.candidate_2}")

    def vote(self):
        voter_id = int(input("\nEnter your voter ID: "))

        # invalid voter
        if voter_id not in self.voters_id:
            print("Invalid voter ID.")
            return

        # already voted
        if voter_id in self.voted_voters:
            print("You have already voted.")
            return
            
        self.show_candidates()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.candidate1_votes += 1
            self.voted_voters.add(voter_id)

            print(f"Your vote for '{self.candidate_1}' has been recorded.")

        elif choice == 2:
            self.candidate2_votes += 1
            self.voted_voters.add(voter_id)

            print(f"Your vote for '{self.candidate_2}' has been recorded.")

        else:
            print("Invalid choice.")

    def result(self):
        print("\nVoting completed.")

        print(f"{self.candidate_1} votes: {self.candidate1_votes}")
        print(f"{self.candidate_2} votes: {self.candidate2_votes}")

        if self.candidate1_votes > self.candidate2_votes:
            print(f"{self.candidate_1} won the election.")

        elif self.candidate2_votes > self.candidate1_votes:
            print(f"{self.candidate_2} won the election.")

        else:
            print("Election is tied.")

    def start_voting(self):
        total_voters = len(self.voters_id)
        print(f"\nTotal voters: {total_voters}")
        
        while len(self.voted_voters) < total_voters:
            self.vote()
        self.result()

if __name__ == "__main__":
    obj = VotingSystem()
    obj.start_voting()
"""

candidate_1, candidate_2 = list(map(str, input("Enter 2 candidates name: ").split()))

candidates1_votes = 0
candidates2_votes = 0

voters_id = [101, 102, 103, 104]

no_of_voters = len(voters_id)

print(f"Total number of voters: {no_of_voters}")

voted_voters = set()

while True:

    # voting complete
    if len(voted_voters) == no_of_voters:

        print("\nVoting completed.")

        if candidates1_votes > candidates2_votes:
            print(f"{candidate_1} won with {candidates1_votes} votes.")

        elif candidates2_votes > candidates1_votes:
            print(f"{candidate_2} won with {candidates2_votes} votes.")

        else:
            print(f"It's a tie between {candidate_1} and {candidate_2}")

        break

    voter_id = int(input("\nEnter your voter ID: "))

    # invalid voter
    if voter_id not in voters_id:
        print("Invalid voter ID.")
        continue

    # already voted
    if voter_id in voted_voters:
        print("You have already voted.")
        continue

    print(f"\n1. {candidate_1}")
    print(f"2. {candidate_2}")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        candidates1_votes += 1
        voted_voters.add(voter_id)
        print(f"Your vote for '{candidate_1}' has been recorded.")

    elif choice == 2:
        candidates2_votes += 1
        voted_voters.add(voter_id)
        print(f"Your vote for '{candidate_2}' has been recorded.")

    else:
        print("Invalid choice.")