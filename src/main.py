from js import document, window
import random
from tetriminos import SHAPES, COLORS

# Game constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30  # pixels

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

def main():
    """Main function to setup and run the game."""
    # Get canvas and context
    canvas = document.getElementById("game-canvas")
    ctx = canvas.getContext("2d")

    # Set canvas dimensions
    canvas.width = GRID_WIDTH * BLOCK_SIZE
    canvas.height = GRID_HEIGHT * BLOCK_SIZE

    # Game state
    current_piece = spawn_piece()

    def game_loop(timestamp):
        """The main game loop, called for each animation frame."""
        # Clear the canvas
        ctx.fillStyle = "#000"
        ctx.fillRect(0, 0, canvas.width, canvas.height)
        
        # Draw the current piece
        draw_piece(ctx, current_piece)

        # Request the next frame
        window.requestAnimationFrame(game_loop)

    # Start the game loop
    window.requestAnimationFrame(game_loop)

# Run the main function
main() 