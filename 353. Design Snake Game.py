from collections import deque

class SnakeGame:
    # won't change
    moves = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

    # maybe we could create a Snake class
    class Snake:
        def __init__(self):
            self.pos = (0, 0)
            self.pos_deque = deque({(0, 0)})
            self.pos_set = set({(0, 0)})

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = self.Snake()
        self.borders = (height, width)
        self.food = deque(food)
        self.game_over = False
        

    def move(self, direction: str) -> int:
        if self.game_over: return -1

        self.snake.pos = (self.snake.pos[0] + self.moves[direction][0], self.snake.pos[1] + self.moves[direction][1])

        # if there is food, extend snake tail
        if self.food and self.snake.pos == tuple(self.food[0]):
            self.food.popleft()
        else:
            snake_last_pos = self.snake.pos_deque.popleft()
            self.snake.pos_set.remove(snake_last_pos)
        
        # check if snake is out of the table or 
        if self.snake.pos[0] < 0 or self.snake.pos[1] < 0 or self.snake.pos[0] >= self.borders[0] or self.snake.pos[1] >= self.borders[1] or self.snake.pos in self.snake.pos_set:
            self.game_over = True
            return -1

        # add current pos
        self.snake.pos_set.add(self.snake.pos)
        self.snake.pos_deque.append(self.snake.pos)

        # return snake tail length
        return len(self.snake.pos_set) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)