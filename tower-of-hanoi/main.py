def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),
        [],
        []
    ]

    steps = []

    def save_step():
        current = " ".join(str(rod) for rod in rods)
        steps.append(current)

    def move_disks(count, start, end, spare):
        if count == 0:
            return

        move_disks(count - 1, start, spare, end)

        disk = rods[start].pop()
        rods[end].append(disk)

        save_step()

        move_disks(count - 1, spare, end, start)

    save_step()
    move_disks(n, 0, 2, 1)

    return "\n".join(steps)
