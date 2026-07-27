import datetime
import os
'''
class VotingSystem:
    def __init__(self, candidates, voters_id):
        self.candidates = candidates
        self.voters_id = voters_id
        self.votes = {candidate: 0 for candidate in candidates}
        self.voted_voters = set()
        self.winners = []  # ensure it exists even if no votes

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

import os
import datetime

class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.votes = {}
        self.voters_id = []
        self.voted_voters = set()
        self.election_started = False

    def load_candidates(self):
        if os.path.exists("candidates.txt"):
            with open("candidates.txt", "r", encoding="utf-8") as f:
                self.candidates = [line.strip() for line in f if line.strip()]
        else:
            print("No candidates file found. Enter candidates manually.")
            n = int(input("How many candidates? "))
            for i in range(1, n + 1):
                name = input(f"Enter name of candidate {i}: ")
                self.candidates.append(name)
            with open("candidates.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(self.candidates))
        self.votes = {name: 0 for name in self.candidates}

    def load_voters(self):
        if os.path.exists("voters.txt"):
            with open("voters.txt", "r", encoding="utf-8") as f:
                self.voters_id = [line.strip() for line in f if line.strip()]
                self.voters_id = [int(x) for x in self.voters_id if x.isdigit()]
        else:
            print("No voters file found. Using default voters.")
            self.voters_id = [101, 102, 103, 104]

    def show_candidates(self):
        print("\nCandidates:")
        for i, name in enumerate(self.candidates, 1):
            print(f"{i}. {name}")

    def vote(self):
        if not self.election_started:
            self.election_started = True

        try:
            voter_id = int(input("\nEnter your voter ID: "))
        except ValueError:
            print("Invalid voter ID (must be a number).")
            return

        if voter_id not in self.voters_id:
            print("Invalid voter ID.")
            return

        if voter_id in self.voted_voters:
            print("You have already voted.")
            return

        self.show_candidates()
        try:
            choice = int(input("Enter your choice (number): "))
        except ValueError:
            print("Invalid choice (must be a number).")
            return

        if 1 <= choice <= len(self.candidates):
            selected = self.candidates[choice - 1]
            self.votes[selected] += 1
            self.voted_voters.add(voter_id)
            print(f"Your vote for '{selected}' has been recorded.")
        else:
            print("Invalid choice. Please choose a valid candidate number")

    def result(self):
        print("\nVoting completed.")
        max_votes = max(self.votes.values())

        print("\nVote summary:")
        for name, count in self.votes.items():
            print(f"{name}: {count} votes")

        winners = [name for name, count in self.votes.items() if count == max_votes]

        if len(winners) == 1:
            print(f"\nWinner: {winners[0]} with {max_votes} votes!")
        else:
            print(f"\nIt's a tie between: {', '.join(winners)} with {max_votes} votes each!")

        # Save results to file
        with open("voting_results.txt", "w", encoding="utf-8") as f:
            f.write("Voting Results\n")
            f.write("================\n")
            for name, count in self.votes.items():
                f.write(f"{name}: {count} votes\n")
            f.write("\n")
            if len(winners) == 1:
                f.write(f"Winner: {winners[0]} with {max_votes} votes\n")
            else:
                f.write(f"Tie between: {', '.join(winners)} with {max_votes} votes each\n")
            f.write("\nTime: " + str(datetime.datetime.now()))
        print("\nResults saved to 'voting_results.txt'")

    def start_voting(self):
        self.load_candidates()
        self.load_voters()
        total_voters = len(self.voters_id)
        print(f"\nTotal voters: {total_voters}")

        while len(self.voted_voters) < total_voters:
            self.vote()
        self.result()


if __name__ == "__main__":
    v = VotingSystem()
    v.start_voting()