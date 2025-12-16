import datetime
candidate_1, candidate_2 = list(map(str, input("Enter 2 candidates name: ")).split())
candidates1_votes = 0
candidates2_votes = 0
voters_id = [101, 102, 103, 104]
no_of_voters = len(voters_id)
print(f"Total number of voters: {no_of_voters}")
voted_voters = set()
while True:
    if voters_id == []:
        print("Voting completed.")
        if candidates1_votes > candidates2_votes:
            print(f"{candidate_1} won with {candidates1_votes} election votes.")
        elif candidates1_votes < candidates2_votes:
            print(f"{candidate_2} won with {candidates2_votes} election votes.")
        elif candidates1_votes == candidates2_votes:
            print(f"It's a tie between {candidate_1} and {candidate_2} with {candidates1_votes} election votes each.")
        else:
            print("Voting incomplete.")
    else:
        voter_id = int(input("Enter your voter ID: "))
        if voter_id in voted_voters:
            print("You have already voted.")
        else:
            print(f"\n1. {candidate_1}\n2. {candidate_2}")
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
                print("Invalid choice. Please try again.")
        

