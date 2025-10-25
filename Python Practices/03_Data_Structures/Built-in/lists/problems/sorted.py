def char_sorted(name):
    parts = name.split()
    return parts[1] if len(parts) > 1 else parts[0]

bangladesh = ['Tanzid Hasan', 'Emon', 'Liton Das', 'Saif Hasan', 'Tawhid Hridoy', 'Shamim Hosen', 'Nurul Hasan', 'Rishad Hasan']
bangladesh.sort(key=char_sorted)
print(bangladesh)
