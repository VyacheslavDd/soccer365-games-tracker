# soccer365-games-tracker
Простое приложение на фреймворке Python Flet, использующее сайт soccer365.ru для отслеживания футбольных матчей: событий, счёта; так же имеет систему уведомлений при изменении статуса матча, счёта или появлении нового события (Гол, пенальти и т.п.).
Предназначено для Windows 10

# Как запустить?
Клонировать репозиторий в выбранную папку, запустить файл main.py

# Как пользоваться?
Приложение предполагает вставку ссылки на матч с сайта soccer365.ru, нажатие кнопки "Добавить матч", после чего данный матч добавляется в таблицу, и будет отслеживаться приложением до тех пор, пока его статус не изменится на "Завершен".
Так же можно воспользоваться кнопкой "Добавить матчи за сегодня": приложение спарсит главную страницу сайта и выберет все матчи, расположенные на ней, не имеющие статус "Завершен".
Нельзя добавить один и тот же матч дважды!

# Дополнительный функционал
Каждый матч можно удалить из таблицы, что приведёт к прекращению его отслеживания; у каждого матча можно посмотреть список событий — он расположен в самом низу страницы.
Каждый раз при изменении статуса матча, счёта, либо при новом событии будет появляться уведомление на 3 секунды, отображающее афишу матча, счёт, и сообщение, что же именно произошло.
Данные с таблицы можно сохранить в .txt-файл с помощью кнопки "Сохранить сет матчей", а впоследствии спокойно загрузить с помощью кнопки "Загрузить сет матчей" (так же доступны только файлы формата .txt).
Таким образом, можно, например, добавить для отслеживания матчи какого-нибудь дня Лиги Чемпионов, сохранить данные, а перед самими играми загрузить данные и отслеживать события игр, не заходя на сам сайт.  
