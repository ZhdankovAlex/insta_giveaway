console.log('%cПАРСЕР АКТИВНОЙ АУДИТОРИИ (ЛАЙКИ) INSTAGRAM', 'color: #1d6ba3; font-size:24px;');
console.log('%cЛеонид Залюбовский 2019 | http://www.leoneed.pro | http://Instagram.com/leoneed.pro', 'color: #1d6ba3; font-size:14px;');
try {
    // ----------------------------------------------------------------------------------
    // ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
    // ----------------------------------------------------------------------------------
    var accounts = [];
    var div_accounts = document.getElementsByClassName('RnEpo Yx5HN')[0];
	var height_scrolling = []; // массив размеров (высот) скроллинга
    // ----------------------------------------------------------------------------------
    var scrollTag = div_accounts.getElementsByTagName('div');
    for (var i = 0; i < scrollTag.length; i++) {
        if (scrollTag[i].style.height == '356px') {
            var div_scroll = scrollTag[i];
            console.log(div_scroll);
        }
    }
	// ----------------------------------------------------------------------------------
    var div_full_scroll = div_scroll.getElementsByTagName('div');
    // ----------------------------------------------------------------------------------
    // СКОРОСТЬ ПРОКРУТКИ
    // Задаётся в миллисекундах
    // ----------------------------------------------------------------------------------
    var speed_scrolling = 300;
    // ----------------------------------------------------------------------------------
    // УКАЖИТЕ ТРЕБУЕМОЕ КОЛ-ВО АККАУНТОВ ДЛЯ СБОРА
    // Если указать 0 (ноль) - соберет все аккаунты, по умолчанию стоит 700, свыше возможны
    // ограничения - лимиты самого Instagram (ошибка 429)
    // ----------------------------------------------------------------------------------
    var user_count = 700;
    // ----------------------------------------------------------------------------------
    // ФУНКЦИЯ УНИКАЛЬНЫХ ЗНАЧЕНИЙ В МАССИВЕ ДЛЯ СБОРА ДАННЫХ
    // ----------------------------------------------------------------------------------
        Array.prototype.unique = function () {
        var a = [];
        var l = this.length;

        for (var i = 0; i < l; i++) {
            for (var j = i + 1; j < l; j++) {
                if (this[i] === this[j]) {
                    j = ++i;
                }
            }
            a.push(this[i]);
        }
        return a;
    };
    // ----------------------------------------------------------------------------------
    var titleH1 = document.getElementsByClassName("m82CD")[0]; // класс тега h1 заголовка окна
    var title = titleH1.innerHTML;
    // ----------------------------------------------------------------------------------
    // УСЛОВИЕ ВЫБОРА ОТМЕТОК НРАВИТСЯ
    // ----------------------------------------------------------------------------------
    if (title == "Отметки \"Нравится\"" || title == "Likes") {
        var total_count = document.getElementsByClassName("Nm9Fw")[0].innerHTML;
        total_count = total_count.match(/<span>[^]+/g).join('').match(/[^\D+]+/g).join('');
    } else {
        console.log("стоп");
    }
    // ----------------------------------------------------------------------------------
    // Общее кол-во аккаунтов для сбора
    // ----------------------------------------------------------------------------------
    console.log('%cОбщее кол-во аккаунтов для сбора: ' + total_count + ' шт.', 'color: #13a555; font-size:16px;');
    // ----------------------------------------------------------------------------------
    if (user_count != 0) {
        console.log('%cКол-во заданное пользователем: ' + user_count + ' шт.', 'color: #13a555; font-size:16px;');
    }
    // ----------------------------------------------------------------------------------
    console.log('%cНачался сбор данных, дождитесь выполнения...', 'color: #13a555; font-size:16px;');
    // ----------------------------------------------------------------------------------
    // ФУНКЦИЯ СТАРТА СБОРА ДАННЫХ
    // ----------------------------------------------------------------------------------
    function start_parsing() {
        var a_accounts = div_accounts.getElementsByTagName('a');
        for (var i = 0; i < a_accounts.length; i++) {
            if (a_accounts[i].hasAttribute('title') == true) {
                accounts.push(a_accounts[i].getAttribute('title'));
                accounts = accounts.unique();
            }
        }
        accounts.splice(user_count);
    }
    // ----------------------------------------------------------------------------------
    // ФУНКЦИЯ ЗАВЕРШЕНИЯ СБОРА ДАННЫХ
    // ----------------------------------------------------------------------------------
        function end_parsing() {
        result_count = accounts.length;
        accounts = accounts.join('\n');
        console.log(accounts);
        console.log('%cАккаунтов собрано: ' + result_count + ' шт.', 'color: #13a555; font-size:18px;');
        console.log('%cВыделите собранные имена аккаунтов выше и нажмите CTRL-C, чтобы скопировать.', 'color: #13a555; font-size:16px;');
        console.log('%cЗаходите подписывайтесь, ставьте лайки! https://Instagram.com/leoneed.pro | http://www.leoneed.pro ', 'color: #1d6ba3; font-size:14px;');
    }
    // ----------------------------------------------------------------------------------
    // ФУНКЦИЯ СКРОЛЛИНГА
    // ----------------------------------------------------------------------------------
    function run_scrolling() {
		// Определяем размер (высоту) прокрутки div_accounts
        var div_accounts_height = div_full_scroll[0].scrollHeight;
        // Заносим размеры в массив
        height_scrolling.push(div_accounts_height);
        if (user_count >= total_count || user_count == 0) {
            user_count = total_count;
        }
	if ((accounts.length != total_count) && (user_count > accounts.length) && (height_scrolling[0] != height_scrolling[4])) {
            div_scroll.scrollBy(0, 200);
			 //  Если в массиве размеров скроллинга более 5 элементов, обнуляем
            if (height_scrolling.length == 5) {
                height_scrolling = [];
            }
            var timeoutID = setTimeout('run_scrolling()', speed_scrolling);
			start_parsing();
        } else {
            clearTimeout(timeoutID);
            end_parsing();
        }
        return false;
    }
    // ----------------------------------------------------------------------------------
    // СТАРТ РАБОТЫ СКРОЛЛИНГА + СБОР ДАННЫХ
    // ----------------------------------------------------------------------------------
    run_scrolling();
    // ----------------------------------------------------------------------------------
} catch (e) {
    console.log('%cНажмите на странице поста на кол-во отметок "Нравится ... и другим", и запустите заново скрипт', 'color: #a22e1c; font-size:18px;');
}
