# Monster Catching Pygame
<br>


## :book: About the project
This is my first solo project using Python. This PyGame has two modes, single player and multi player. This monster catching game has five levels, the higher the level, the more monsters. Score is shown of the top left corner and level on the top right corner.
<br>


## :hammer_and_wrench: Used Technologies
Python
<br>


## :clipboard: Preview
#### :point_down: Single player game
![multiplay](https://user-images.githubusercontent.com/69357145/98470387-3bbc7080-21b3-11eb-8d71-f0e31d184245.gif)
<br /> 
#### :point_down: Multi player game
![singleplay](https://user-images.githubusercontent.com/69357145/98470583-a7eba400-21b4-11eb-9d60-22f644d26c5d.gif)

<br /> 



## 🕹 How to run
1. Fork this respository<br>
Click the Fork button on the upper right-hand side of this repository's page.
2. Clone the repository<br>
Under the repository name, click on the code button and copy the clone URL for the repository.
3. Run the file <br>
``` shell
python -m pip install pygame
```
Open the file on Visual Studio Code and run
<br>


## 💻Usage
```js
class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self, height, width): # boundary for monsters
        if self.rect.x > width or self.rect.x < 0 or self.rect.y > height or self.rect.y < 0:
            self.rect.x = random.randint(0, 490)
            self.rect.y = random.randint(0, 490)
```
<br>


## 📔 License
This project is under MIT license. See the [license](https://opensource.org/licenses/MIT) for more information.
<br /> 
<br /> 








