# soccer365-games-tracker
<p>Простое приложение на фреймворке Python Flet, использующее сайт soccer365.ru для отслеживания футбольных матчей: событий, счёта; так же имеет систему уведомлений при изменении статуса матча, счёта или появлении нового события (Гол, пенальти и т.п.).</p>
<p>Предназначено для Windows 10</p>

# Как запустить?
Клонировать репозиторий в выбранную папку, запустить файл main.py

# Как пользоваться?
<p>Приложение предполагает вставку ссылки на матч с сайта soccer365.ru, нажатие кнопки "Добавить матч", после чего данный матч добавляется в таблицу, и будет отслеживаться приложением до тех пор, пока его статус не изменится на "Завершен".</p>
<p>Так же можно воспользоваться кнопкой "Добавить матчи за сегодня": приложение спарсит главную страницу сайта и выберет все матчи, расположенные на ней, не имеющие статус "Завершен".</p>
<p>Нельзя добавить один и тот же матч дважды!</p>

# Дополнительный функционал
<p>Каждый матч можно удалить из таблицы, что приведёт к прекращению его отслеживания; у каждого матча можно посмотреть список событий — он расположен в самом низу страницы.</p>
<p>Каждый раз при изменении статуса матча, счёта, либо при новом событии будет появляться уведомление на 3 секунды, отображающее афишу матча, счёт, и сообщение, что же именно произошло.</p>
<p>Данные с таблицы можно сохранить в .txt-файл с помощью кнопки "Сохранить сет матчей", а впоследствии спокойно загрузить с помощью кнопки "Загрузить сет матчей" (так же доступны только файлы формата .txt).</p>
<p>Таким образом, можно, например, добавить для отслеживания матчи какого-нибудь дня Лиги Чемпионов, сохранить данные, а перед самими играми загрузить данные и отслеживать события игр благодаря уведомлениям, не заходя на сам сайт.</p>
