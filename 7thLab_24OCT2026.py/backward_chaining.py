facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

def prove(goal):
    if goal in facts:
        return True

    for conditions, result in rules:
        if result == goal:
            if all(prove(condition) for condition in conditions):
                return True

    return False

goal = "E"
print("Can prove", goal, ":", prove(goal))