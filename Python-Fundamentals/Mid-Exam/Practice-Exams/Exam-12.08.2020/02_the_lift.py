people = int(input())
current_state_lift = [int(i) for i in input().split()]

index = 0
while people > 0:
    if current_state_lift[index] > 4:
        people += current_state_lift[index] - 4
        current_state_lift[index] = 4

    if current_state_lift[index] == 4:
        index += 1
        if index > len(current_state_lift) - 1:
            break
    current_state_lift[index] += 1
    people -= 1

if people == 0 and current_state_lift.count(4) != len(current_state_lift):
    print("The lift has empty spots!")
    print(' '.join(str(i) for i in current_state_lift))

elif people > 0 and current_state_lift.count(4) == len(current_state_lift):
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(str(i) for i in current_state_lift))

else:
    print(' '.join(str(i) for i in current_state_lift))
