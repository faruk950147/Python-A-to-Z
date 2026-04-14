def char_sorted(name):
    parts = name.split()
    # এই ফাংশনটা নামকে স্পেস দিয়ে ভাগ করছে (split())

    # যদি নাম ২ শব্দের হয় → দ্বিতীয় শব্দটা (surname/last name) return করবে
    # যদি ১ শব্দের হয় → সেই নামটাই return করবে
    # উদাহরণ
    # "Tanzid Hasan" → "Hasan"
    # "Emon" → "Emon"
    # "Liton Das" → "Das"
    # "Saif Hasan" → "Hasan"
    # "Tawhid Hridoy" → "Hridoy"
    # "Shamim Hosen" → "Hosen"
    # "Nurul Hasan" → "Hasan"
    # "Rishad Hasan" → "Hasan"
    # এখানে list টা sort হচ্ছে char_sorted() ফাংশনের return value অনুযায়ী (মানে last name অনুযায়ী)
    
    return parts[1] if len(parts) > 1 else parts[0]

bangladesh = ['Tanzid Hasan', 'Emon', 'Liton Das', 'Saif Hasan', 'Tawhid Hridoy', 'Shamim Hosen', 'Nurul Hasan', 'Rishad Hasan']
bangladesh.sort(key=char_sorted)
print(bangladesh)
