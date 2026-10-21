state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

new_state = list(state)

new_state[4], new_state[7] = new_state[7], new_state[4]

new_state = tuple(new_state)

print(new_state)
