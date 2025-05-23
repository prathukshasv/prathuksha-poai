
class Blockworld:
    def __init__(self, num_blocks):
        self.state = [[i] for i in range(num_blocks)]

    def display(self):
        for stack in self.state:
            print(f"Block(s) on stack: {stack}")

    def find(self, block):
        for stack in self.state:
            if block in stack:
                return stack
        return None

    def move(self, block, dest):
        s = self.find(block)
        d = self.find(dest)
        if s and d and block in s:
            s.remove(block)
            d.append(block)
            self.display()

    def set_goal(self, goal):
        self.state = goal
        print("Goal state set!")
        self.display()


def main():
    bw = Blockworld(3)
    print("Initial state:")
    bw.display()

    goal = [[0], [1], [2]]
    bw.set_goal(goal)

    print("Performing Moves:")
    bw.move(0, 1)
    bw.move(1, 2)
    bw.move(2, 0)


if __name__ == "__main__":
    main()
