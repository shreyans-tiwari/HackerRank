if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner = runner_up = -101

    for i in arr:
        if i > winner:
            runner_up, winner = winner, i
        elif i > runner_up and i != winner:
            runner_up = i

    print(runner_up)
