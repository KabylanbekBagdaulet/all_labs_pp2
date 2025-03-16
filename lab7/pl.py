import pygame
import os

pygame.init()

music_folder = r"C:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\Новая папка (2)\music"
playlist = os.listdir(music_folder)


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

index, playing = 0, True

# Загружаем и запускаем первую песню
pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза / продолжить
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:  # Следующий трек
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:  # Предыдущий трек
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
                pygame.mixer.music.play()

    clock.tick(24)
