from js import document, window
import random
from tetriminos import SHAPES, COLORS

# Game constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30  # pixels
DROP_INTERVAL = 500  # milliseconds

class Piece:
    """Represents a Tetris piece."""
    def __init__(self, shape_name, shape, color):
        self.shape_name = shape_name
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

def spawn_piece():
    """Spawns a new random piece."""
    shape_name = random.choice(list(SHAPES.keys()))
    shape = SHAPES[shape_name]
    color = COLORS[shape_name]
    return Piece(shape_name, shape, color)

def draw_piece(ctx, piece):
    """Draws a piece on the canvas."""
    ctx.fillStyle = piece.color
    for r, row in enumerate(piece.shape):
        for c, block in enumerate(row):
            if block:
                ctx.fillRect(
                    (piece.x + c) * BLOCK_SIZE,
                    (piece.y + r) * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )

def is_valid_position(piece):
    """Checks if a piece is in a valid position."""
    for r, row in enumerate(piece.shape):
        for c, block in enumerate(row):
            if block:
                if not (0 <= piece.x + c < GRID_WIDTH and 0 <= piece.y + r < GRID_HEIGHT):
                    return False
    return True

def main():
    """Main function to setup and run the game."""
    canvas = document.getElementById("game-canvas")
    ctx = canvas.getContext("2d")
    canvas.width = GRID_WIDTH * BLOCK_SIZE
    canvas.height = GRID_HEIGHT * BLOCK_SIZE

    # Game state
    current_piece = spawn_piece()
    last_drop_time = 0

    def game_loop(timestamp):
        nonlocal last_drop_time, current_piece
        
        # Automatic drop
        if timestamp - last_drop_time > DROP_INTERVAL:
            last_drop_time = timestamp
            current_piece.y += 1
            if not is_valid_position(current_piece):
                current_piece.y -= 1
                current_piece = spawn_piece() # For now, just spawn a new piece

        # Drawing
        ctx.fillStyle = "#000"
        ctx.fillRect(0, 0, canvas.width, canvas.height)
        draw_piece(ctx, current_piece)
        window.requestAnimationFrame(game_loop)

    def handle_keydown(event):
        nonlocal current_piece
        original_x = current_piece.x
        if event.key == "ArrowLeft":
            current_piece.x -= 1
        elif event.key == "ArrowRight":
            current_piece.x += 1
        
        if not is_valid_position(current_piece):
            current_piece.x = original_x

    document.addEventListener("keydown", handle_keydown)
    window.requestAnimationFrame(game_loop)

main() 