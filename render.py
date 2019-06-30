"""Simple example for using sdl2 directly."""
import os

os.environ["PATH"] += ";lib"

import sys
import ctypes
from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlmixer import *
from sdl2.sdlttf import *
import random

__all__ = ['Window', 'Person', 'Renderer', 'Sprite', 'SpriteFactory']


class Window:
    def __init__(self, title, size):
        self.title = title
        self.width, self.height = size

        SDL_Init(SDL_INIT_EVERYTHING)
        SDL_EnableScreenSaver()
        SDL_setenv(SDL_HINT_RENDER_SCALE_QUALITY, 'linear'.encode("utf-8"), 1)

        # SDL_StopTextInput()
        self.window = SDL_CreateWindow(title.encode("utf8"),
                                       SDL_WINDOWPOS_CENTERED,
                                       SDL_WINDOWPOS_CENTERED,
                                       self.width, self.height, SDL_WINDOW_SHOWN)
        SDL_SetWindowOpacity(self.window, 1)

        SDL_StartTextInput()
        SDL_SetTextInputRect(SDL_Rect(0, 0, 100, 60))

class Renderer:
    def __init__(self, window: Window):
        self.window = window
        self.renderer = SDL_CreateRenderer(window.window, -1, 0)

    def save(self, file):
        surface = SDL_GetWindowSurface(self.window.window)

        SDL_RenderReadPixels(self.renderer, ctypes.byref(surface.contents.clip_rect), ctypes.c_uint32(0),
                             ctypes.cast(surface.contents.pixels, ctypes.c_void_p),
                             ctypes.c_int(surface.contents.pitch))
        SDL_SaveBMP(surface, file.encode("utf8"))


class Sprite:
    def __init__(self, renderer, texture):
        self.texture = IMG_LoadTexture(renderer.renderer, texture.encode("utf8"))
        self.renderer = renderer
        w = ctypes.c_long()
        h = ctypes.c_long()
        SDL_QueryTexture(self.texture, None, None, ctypes.byref(w), ctypes.byref(h))
        self.w = w
        self.h = h

    def update(self):
        SDL_SetTextureBlendMode(self.texture, SDL_BLENDMODE_BLEND)
        SDL_SetTextureAlphaMod(self.texture, random.randint(170, 200))
        # SDL_SetTextureAlphaMod(self.texture, 50)

    def render(self, x=0, y=0):
        # self.update()
        # SDL_RenderSetViewport(self.renderer.renderer, SDL_Rect(0, 0, 100, 100))
        SDL_RenderCopyEx(self.renderer.renderer, self.texture, SDL_Rect(0, 0, self.w, self.h),
                         SDL_Rect(x, y, self.w, self.h), 0, None, SDL_FLIP_NONE)
        # SDL_RenderSetViewport(self.renderer.renderer, None)
        # SDL_RenderCopyEx(self.renderer.renderer, self.texture, SDL_Rect(0, 0, self.w, self.h),
        #                SDL_Rect(x, y, self.w, self.h), random.randint(1, 90), None, SDL_FLIP_NONE)
        # SDL_RenderPresent(self.renderer.renderer)


class SpriteFactory:
    def __init__(self, renderer):
        self.renderer = renderer

    def create(self, texture):
        return Sprite(self.renderer, texture)


class Person:
    pass
