for i in range(5):
        height = random.randint(10, 50)
        pygame.draw.rect(screen, (0, 100, 100), (5 + i*20, 300-height, 10, height))
        pygame.display.flip()