import datetime
# class based
class VotingSystem:
    def __init__(self, candidates, voters_id):
        self.candidates = candidates
        self.voters_id = voters_id
        self.votes = {candidate: 0 for candidate in candidates}
        self.voted_voters = set()

    def start_voting(self):
        print("========== Voting System Started ==========\n")
        for voter_id in self.voters_id:
            if voter_id in self.voted_voters:
                print(f"Voter ID {voter_id} has already voted. Skipping...")
                continue

            print(f"\nVoter {voter_id}, please vote for your preferred candidate.")
            print("Candidates:")
            for candidate in self.candidates:
                print(f" - {candidate}")

            while True:
                vote = input("Enter your vote: ").strip()
                if vote in self.votes:
                    self.votes[vote] += 1
                    self.voted_voters.add(voter_id)
                    print(f"Your vote for '{vote}' has been recorded.")
                    break
                else:
                    print("Invalid candidate name. Please try again.\n")

        self.show_results()
        self.save_results()

    def show_results(self):
        print("\n========== Voting Summary ==========")
        for candidate, count in self.votes.items():
            print(f"{candidate}: {count} votes")

        max_votes = max(self.votes.values())
        self.winners = [candidate for candidate, count in self.votes.items() if count == max_votes]

        print("\n========== Final Result ==========")
        if len(self.winners) == 1:
            print(f"Winner: {self.winners[0]} with {max_votes} votes!")
        else:
            print(f"It's a tie between: {', '.join(self.winners)} with {max_votes} votes each!")

    def save_results(self):
        max_votes = max(self.votes.values())
        with open("voting_result.txt", "w", encoding="utf-8") as file:
            file.write("Voting Result\n")
            file.write("=====================\n")
            for candidate, count in self.votes.items():
                file.write(f"{candidate}: {count} votes\n")
            file.write("\n")
            if len(self.winners) == 1:
                file.write(f"Winner: {self.winners[0]} with {max_votes} votes\n")
            else:
                file.write(f"It's a tie between: {', '.join(self.winners)} with {max_votes} votes each\n")
            file.write("\nTime: " + str(datetime.datetime.now()))
        print("\nResults saved to 'voting_result.txt'")
        print("========== Voting Completed ==========\n")

if __name__ == "__main__":
    candidates = ["Alice", "Bob", "Charlie"]
    voters_id = ["101", "102", "103", "104"]

    voting_system = VotingSystem(candidates, voters_id)
    voting_system.start_voting()

'''
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

'''


    


