facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

while True:
    new_fact = False

    for conditions, result in rules:
        if conditions.issubset(facts) and result not in facts:
            facts.add(result)
            new_fact = True

    if not new_fact:
        break

print("Final facts:", facts)