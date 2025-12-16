def reviewsCount(data):
    if isinstance(data, dict):
        likes = 0
        comments = 0
        dislikes = 0
        for key in data:
            if key == "likes":
                likes += data[key]
            elif key == "comments":
                comments += data[key]
            elif key == "dislikes":
                dislikes += data[key]
        return f"Likes: {float(likes)}, Comments: {float(comments)}, Dislikes: {float(dislikes)}"
    else:
        return "Please provide a dictionary"
    
print(reviewsCount({"image":1, "likes":2, "comments":3, "dislikes":4}))  # Output: Likes: 2.0, Comments: 3.0, Dislikes: 4.0
