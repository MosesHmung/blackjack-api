from fastapi import FastAPI
from game import Game

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


game = None

@app.post("/start")
def start_game():
    global game
    game = Game()
    game.start_round()
    return game.get_public_state()

@app.post("/hit")
def hit():
    global game
    if not game:
        return {"error": "Game not started"}

    game.player_hit()
    if game.is_over:
        return game.get_full_state()
    return game.get_public_state()


@app.post("/stand")
def stand():
    global game
    if not game:
        return {"error": "Game not found"}

    game.player_stand()
    return game.get_full_state()

@app.get("/state")
def state():
    global game
    if not game:
        return {"error": "Game not found"}

    if game.is_over:
        return game.get_full_state()
        pass
    return game.get_public_state()
    pass



