from js import document, window

# Game constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30  # pixels

def main():
    """Main function to setup and run the game."""
    # Get canvas and context
    canvas = document.getElementById("game-canvas")
    ctx = canvas.getContext("2d")

    # Set canvas dimensions
    canvas.width = GRID_WIDTH * BLOCK_SIZE
    canvas.height = GRID_HEIGHT * BLOCK_SIZE

    def game_loop(timestamp):
        """The main game loop, called for each animation frame."""
        # Clear the canvas
        ctx.fillStyle = "#000"
        ctx.fillRect(0, 0, canvas.width, canvas.height)
        
        # Draw a test rectangle
        ctx.fillStyle = "#F00" # Red
        ctx.fillRect(0, 0, BLOCK_SIZE, BLOCK_SIZE)

        # Request the next frame
        window.requestAnimationFrame(game_loop)

    # Start the game loop
    window.requestAnimationFrame(game_loop)

# Run the main function
main() 