def Religion(religion):
    match religion:
        case "Islam":
            print("Muslim")
        case "Hindu":
            print("Hindu")
        case "Christian":
            print("Christian")
        case "Buddhist":
            print("Buddhist")
        case "Jain":
            print("Jain")
        case _:
            print("Unknown")

Religion("Islam")