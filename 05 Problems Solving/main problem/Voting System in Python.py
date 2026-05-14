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
    v = VotingSystem()
    v.start_voting()

