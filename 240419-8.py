def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'c'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

scores = [88, 92, 78, 60, 75, 95]
newlist=list(map(grade, scores))
print(newlist)