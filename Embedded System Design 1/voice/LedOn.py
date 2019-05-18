from aiy.board import Board, Led

while True:
    with Board() as board:
        board.led.state = Led.ON

