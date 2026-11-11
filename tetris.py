import pygame
import random

# Initialize Pygame
pygame.init()

# Visual Constants
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE + 200  # Space for grid + sidebar
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE

# Color Definitions (RGB)
BLACK = (10, 10, 15)
GRAY = (40, 40, 50)
WHITE = (240, 240, 240)
CYAN = (0, 240, 240)    # I
YELLOW = (240, 240, 0)  # O
PURPLE = (160, 0, 240)  # T
GREEN = (0, 240, 0)     # S
RED = (240, 0, 0)       # Z
BLUE = (0, 0, 240)      # J
ORANGE = (240, 160, 0)  # L

# Tetromino Shapes & Colors
SHAPES = [
    [[1, 1, 1, 1]],                              # I
    [[1, 1], [1, 1]],                            # O
    [[0, 1, 0], [1, 1, 1]],                      # T
    [[0, 1, 1], [1, 1, 0]],                      # S
    [[1, 1, 0], [0, 1, 1]],                      # Z
    [[1, 0, 0], [1, 1, 1]],                      # J
    [[0, 0, 1], [1, 1, 1]]                       # L
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE]

class Piece:
    def __init__(self, x, y, shape_idx):
        self.x = x
        self.y = y
        self.shape = SHAPES[shape_idx]
        self.color = SHAPE_COLORS[shape_idx]

    def rotate(self):
        # Matrix transpose + reverse row = 90-degree clock-wise rotation
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        idx = random.randint(0, len(SHAPES) - 1)
        return Piece(GRID_WIDTH // 2 - 1, 0, idx)

    def valid_move(self, piece, x_offset=0, y_offset=0):
        for r, row in enumerate(piece.shape):
            for c, val in enumerate(row):
                if val:
                    new_x = piece.x + c + x_offset
                    new_y = piece.y + r + y_offset
                    
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x] != BLACK:
                        return False
        return True

    def lock_piece(self):
        for r, row in enumerate(self.current_piece.shape):
            for c, val in enumerate(row):
                if val:
                    self.grid[self.current_piece.y + r][self.current_piece.x + c] = self.current_piece.color
        
        self.clear_lines()
        self.current_piece = self.new_piece()
        
        # If new piece collides immediately, game is over
        if not self.valid_move(self.current_piece):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        
        for _ in range(lines_cleared):
            new_grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
        
        self.grid = new_grid
        self.score += lines_cleared * 100

    def move(self, dx):
        if self.valid_move(self.current_piece, x_offset=dx):
            self.current_piece.x += dx

    def drop(self):
        if self.valid_move(self.current_piece, y_offset=1):
            self.current_piece.y += 1
        else:
            self.lock_piece()

    def rotate_piece(self):
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if not self.valid_move(self.current_piece):
            self.current_piece.shape = old_shape  # Revert if illegal

def draw(screen, game, font):
    screen.fill(BLACK)

    # Draw grid background and locked blocks
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, game.grid[y][x], rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Grid border

    # Draw current falling piece
    if game.current_piece:
        for r, row in enumerate(game.current_piece.shape):
            for c, val in enumerate(row):
                if val:
                    rect = pygame.Rect(
                        (game.current_piece.x + c) * BLOCK_SIZE,
                        (game.current_piece.y + r) * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE
                    )
                    pygame.draw.rect(screen, game.current_piece.color, rect)
                    pygame.draw.rect(screen, WHITE, rect, 1)

    # Sidebar: Display Score and Controls
    sidebar_x = GRID_WIDTH * BLOCK_SIZE + 20
    score_text = font.render(f"Score: {game.score}", True, WHITE)
    screen.blit(score_text, (sidebar_x, 30))

    controls = ["Controls:", "← / → : Move", "↑ : Rotate", "↓ : Soft Drop", "SPACE : Hard Drop"]
    for i, line in enumerate(controls):
        ctrl_text = font.render(line, True, WHITE)
        screen.blit(ctrl_text, (sidebar_x, 100 + i * 25))

    if game.game_over:
        over_text = font.render("GAME OVER", True, RED)
        screen.blit(over_text, (sidebar_x, 260))

    pygame.display.flip()

def main():
    screen = pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    game = Tetris()
    fall_time = 0
    fall_speed = 500  # Drop delay in milliseconds

    while True:
        delta_time = clock.tick(60)
        fall_time += delta_time

        # Automatic downward gravity
        if fall_time >= fall_speed and not game.game_over:
            game.drop()
            fall_time = 0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN and not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move(-1)
                elif event.key == pygame.K_RIGHT:
                    game.move(1)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP:
                    game.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, y_offset=1):
                        game.current_piece.y += 1
                    game.lock_piece()

        draw(screen, game, font)

if __name__ == "__main__":
    main()