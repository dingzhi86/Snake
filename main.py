import ctypes
import random
import time
from render import Window, SDL_SetWindowIcon, IMG_Load, Renderer, SpriteFactory, SDL_SetRenderDrawColor, \
    SDL_RenderClear, SDL_SetTextureAlphaMod, SDL_RenderPresent, SDL_Event, SDL_QUIT, SDL_PollEvent, SDL_Delay, \
    SDL_Color, TTF_OpenFont, TTF_RenderUTF8_Blended_Wrapped, SDL_FreeSurface, SDL_BLENDMODE_ADD, \
    SDL_SetTextureBlendMode, SDL_CreateTextureFromSurface, SDL_RenderCopy, SDL_Rect, SDL_QueryTexture, TTF_Init, \
    Mix_OpenAudio, MIX_DEFAULT_FORMAT, Mix_VolumeMusic, Mix_PlayMusic, Mix_LoadMUS, SDL_TEXTINPUT, SDL_TEXTEDITING, \
    SDL_SetTextureColorMod, SDL_RenderDrawLine, SDL_RenderDrawPoint

if __name__ == "__main__":

    window = Window("🐍 贪吃蛇 🐍", size=(960, 640))

    renderer = Renderer(window)
    factory = SpriteFactory(renderer)
    bg = factory.create("./data/block.png")
    body = factory.create("./data/body.png")
    head = factory.create("./data/head.png")

    TTF_Init()
    font = TTF_OpenFont('data/b.ttf'.encode("utf8"), 25)

    Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048)
    Mix_VolumeMusic(20)
    f = Mix_LoadMUS("data/a.mp3".encode("utf-8"))
    Mix_PlayMusic(f, -1)

    SDL_SetRenderDrawColor(renderer.renderer, 4, 4, 4, 255)
    SDL_RenderClear(renderer.renderer)

    for i in range(window.width // 32):
        for j in range(window.height // 32):
            bg.render(i * 32, j * 32)

    for i in range(10):
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        body.render(32 * x, 32 * y)
        head.render(32 * (x - 1), 32 * y)

    SDL_RenderPresent(renderer.renderer)
    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            if event.type == SDL_TEXTINPUT:
                print(event.text.text.decode("utf8"))
            if event.type == SDL_TEXTEDITING:
                print(event.edit.text.decode("utf8"))
        SDL_Delay(10)
