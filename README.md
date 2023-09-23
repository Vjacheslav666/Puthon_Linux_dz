### Автоматизация тестирования консольных приложений Linux на Python
## Урок 1. Тестирование cli в linux без использования фреймворков

# Задание 1.

Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.

# Задание 2. (повышенной сложности)

Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.



## Урок 2. Создание первых тестов на pytest

# Задание 1.

Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x). 

## Урок 3. Использование фикстур в pytest. Создание отчетов о тестировании

# Задание 1.

Условие:
Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла). 