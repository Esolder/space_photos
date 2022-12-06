# Космический Телеграм

### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Чтобы использовать скрипты, нужно создать файл .env, содержащий следующие переменные:
- `FOLDERPATH`: Путь к папке для загрузки и отправки фото
- `TELEGRAM_TOKEN`: Токен бота Telegram
- `TELEGRAM_CHAT_ID`: ID чата Telegram, в который будут отправляться фото
- `COUNT_NASA_EPIC_PHOTOS` (опционально): Количество "эпичных" Nasa фото для закачки (по умолчанию 5 фото)
- `NASA_API_KEY` (опционально): Токен Nasa API (по умолчанию использует `DEMO_KEY`)
- `DELAY_SECONDS` (опционально): Количество секунд, между отправкой фото (по умолчанию 4 часа)

### fetch_spacex_images.py
Скрипт использует API SpaceX для загрузки фотографий запуска. Запуск выбирается на основе аргументе командной строки `--id`.
Например:
```
python fetch_spacex_images.py --id 5eb87d42ffd86e000604b384
```
Если аргумент останется пустым, скрипт выберет последний запуск.

### fetch_nasa_images.py
Скрипт использует API Nasa для загрузки фотографий со спутников. Количество фотографий выбирается на основе аргументе командной строки `--count`.
Например:
```
python fetch_nasa_images.py --count 5
```
Можно использовать короткую запись:
```
python fetch_nasa_images.py -c 7
```

Если аргумент останется пустым, загрузится 10 фотографий.

### fetch_nasa_epic_images.py
Скрипт использует API Nasa для загрузки "эпичных" фотографий Земли. Количество фото указывается в переменной среды `COUNT_NASA_EPIC_PHOTOS`. Если переменная среды отсутствует, будет установлено значение 5.

### publish_one_photo.py
Скрипт публикует фотографию в Telegram канале, указанном в переменной среды `TELEGRAM_CHAT_ID`, используя идентификатор токена, указанный в переменной среды `TELEGRAM_TOKEN`. Имя файла фотографии может быть указано в аргументе командной строки `--photo`, либо, если аргумент останется пустым, скрипт выберет случайное фото из папки, указанной в переменной среды `FOLDERPATH`.

### publish_in_telegram.py
Скрипт отправляет случайные фотографии из указанной папки в чат Telegram. Фотографии перемешиваются и отправляются с указанным задержкой в секундах между каждой фотографией.
После запуска скрипт будет работать бесконечно, отправляя фотографии в указанный чат.

### support_funcs.py
Содержит вспомогательные функции, использующиеся в других файлах проекта:
- `download_photo` - загружает фотографию в указанную папку
- `get_extension` - получает расширение файла из url 

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).