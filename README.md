# Пятнашки

### Инструкция:

Для игры необходим python3 версии 3.8 или выше. 

Чтобы запустить игру необходимо в папке с игрой питоном запустить файл game.py:
```
python3 game.py
```
### Правила:
Игровое поле 4x4 состоит из клеток с номерами от 1 до 15 и пустой клетки "x". 

Задача игрока - перемещая пустую клетку упорядочить все клетки по возрастанию номера в них,
одновременно переместив пустую клетку в правый нижний угол. А именно чтобы игрок победил
игровое поле после его хода должно выглядить так:
```
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
| 13| 14| 15|  x|
—————————————————
```
Управление пустой клеткой происходит при помощи клавиш 'w', 's', 'a', 'd'.
Чтобы поменять пустую клетку с клеткой выше, ниже, левее и правее соответственно необходимо в свой ход ввести ровно одну команду.
Выходить за пределы игрового поля нельзя.
Прервать игру можно при помощи команды 'ctrl+C'.

Гарантируется, что для любой стартовой расстановки существует алгоритм действий игрока который приведет его к победной позиции.
### Пример работы программы:
```
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9|  x| 11| 12|
—————————————————
| 13| 10| 14| 15|
—————————————————

I'am sure you know the rules. Use 'w', 's', 'a', or 'd' to move 'x'.

Perform your next move: ss
Incorrect input. Please use only commands 'w', 's', 'a', or 'd'.
Perform your next move: s
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
| 13|  x| 14| 15|
—————————————————

Perform your next move: s
Incorrect move. You are trying to go outside the boundary of the playing field.
Perform your next move: a
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
|  x| 13| 14| 15|
—————————————————

Perform your next move: ad
Incorrect input. Please use only commands 'w', 's', 'a', or 'd'.
Perform your next move: a
Incorrect move. You are trying to go outside the boundary of the playing field.
Perform your next move: d
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
| 13|  x| 14| 15|
—————————————————

Perform your next move: d
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
| 13| 14|  x| 15|
—————————————————

Perform your next move: d
—————————————————
|  1|  2|  3|  4|
—————————————————
|  5|  6|  7|  8|
—————————————————
|  9| 10| 11| 12|
—————————————————
| 13| 14| 15|  x|
—————————————————

Congratulations! You won!. You solved this puzzle in 5 steps. Not bad.
```

### Планы на будущее:
1) Добавить уровни сложности.
2) Добавить графический интерфейс. 
