from urllib.request import urlretrieve
import zipfile
import os


sdl2_url = 'https://www.libsdl.org/release/SDL2-2.0.10-win32-x64.zip'
sdl2_img_url = 'https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5-win32-x64.zip'
sdl2_ttf_url = 'https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15-win32-x64.zip'
sdl2_mixer_url = 'https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4-win32-x64.zip'

urls = [sdl2_url, sdl2_img_url, sdl2_mixer_url, sdl2_ttf_url]

def hook(blocknum, bs, size):
    print(blocknum*bs*100//size, '%')

for url in urls:
    name = url.split('/')[-1]
    print(f'正在下载{name}')
    urlretrieve(url, name, reporthook=hook)
    file = zipfile.ZipFile(name)
    file.extractall(path='./dll')
    file.close()
    os.unlink(name)
