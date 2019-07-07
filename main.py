import ctypes
import random
import time
from render import Window, SDL_SetWindowIcon, IMG_Load, Renderer, SpriteFactory, SDL_SetRenderDrawColor, \
    SDL_RenderClear, SDL_SetTextureAlphaMod, SDL_RenderPresent, SDL_Event, SDL_QUIT, SDL_PollEvent, SDL_Delay, \
    SDL_Color, TTF_OpenFont, TTF_RenderUTF8_Blended_Wrapped, SDL_FreeSurface, SDL_BLENDMODE_ADD, \
    SDL_SetTextureBlendMode, SDL_CreateTextureFromSurface, SDL_RenderCopy, SDL_Rect, SDL_QueryTexture, TTF_Init, \
    Mix_OpenAudio, MIX_DEFAULT_FORMAT, Mix_VolumeMusic, Mix_PlayMusic, Mix_LoadMUS, SDL_TEXTINPUT, SDL_TEXTEDITING, \
    SDL_SetTextureColorMod, SDL_RenderDrawLine, SDL_RenderDrawPoint, SDL_KEYUP, SDL_GetKeyName

if __name__ == "__main__":

    window = Window("🐍 贪吃蛇 🐍 🐕 🐱 🐻 🐏", size=(960, 640))

    renderer = Renderer(window)
    factory = SpriteFactory(renderer)
    bg = factory.create("./data/block.png")
    body = factory.create("./data/body.png")
    head = factory.create("./data/head.png")
    h1 = factory.create("./data/1.png")
    tri = factory.create("./data/tri.png")
    water_drop = factory.create("./data/water_drop.png")
    circle = factory.create("./data/circle.png")

    TTF_Init()
    font = TTF_OpenFont('data/b.ttf'.encode("utf8"), 30)
    text = "贪吃蛇"
    text_surface = TTF_RenderUTF8_Blended_Wrapped(font, text.replace(" ", "\n").encode("utf8"), SDL_Color(255, 0, 0, 255), 255)
    text_texture = SDL_CreateTextureFromSurface(renderer.renderer, text_surface)
    w = ctypes.c_long()
    h = ctypes.c_long()
    SDL_QueryTexture(text_texture, None, None, ctypes.byref(w), ctypes.byref(h))
    SDL_FreeSurface(text_surface)

    Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048)
    Mix_VolumeMusic(20)
    f = Mix_LoadMUS("data/a.mp3".encode("utf-8"))
    Mix_PlayMusic(f, -1)

    SDL_SetRenderDrawColor(renderer.renderer, 4, 4, 4, 255)
    SDL_RenderClear(renderer.renderer)


    running = True
    event = SDL_Event()
    x = 0
    y = 0
    flip = False
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            if event.type == SDL_TEXTINPUT:
                print(event.text.text.decode("utf8"))
            if event.type == SDL_TEXTEDITING:
                print(event.edit.text.decode("utf8"))
            if event.type == SDL_KEYUP:
                a = SDL_GetKeyName(event.key.keysym.sym).decode("utf8")
                if a == "Up":
                    y -= 1
                elif a == "Right":
                    x += 1
                    flip = False
                elif a == "Left":
                    x -= 1
                    flip = True
                elif a == "Down":
                    y += 1

        for i in range(window.width // 32):
            for j in range(window.height // 32):
                bg.render(i * 32, j * 32)

        # for i in range(10):
        #     x1 = random.randint(1, 40)
        #     y1 = random.randint(1, 20)
        #     body.render(32 * x1, 32 * y1)
        #     h1.render(32 * x1, 32 * y1)
        #     head.render(32 * (x1 - 1), 32 * y1)
        #     h1.render(32 * x1 - 32, 32 * y1)
        # circle.render(32 * 12, 32 * 5)
        water_drop.render(32 * 12, 32 * 5)
        tri.render(32 * x, 32 * y, flip)

        SDL_RenderCopy(renderer.renderer, text_texture, SDL_Rect(w=w, h=h), SDL_Rect(x=500, y=400, w=w, h=h))

        SDL_RenderPresent(renderer.renderer)
        SDL_Delay(10)
