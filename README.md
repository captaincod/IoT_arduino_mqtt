# Что требовалось сделать

1. Скрипт на Ардуино  

- Делаем машинку по схеме `arduino_scheme.png`  
  -- Важно подобрать правильный резистор.   
     Для этого измеряем сопротивление у фоторезистора:  
	щупами цепляем ножки резистора  
	т.к. головка резистора чувствительна к свету, первое значение получаете   
	закрывая головку пальцем, второе - светя на неё фонариком.  
	запоминаем (у нас было ~ 400 - 20000)  
	далее нужно как-то логарифмически вычислить, какой резистор подойдёт  
	(в нашем случае брать резистор на 4 500. без объяснений.)  

- Запускаем у себя `29.09.ino` с подключенной машинкой  
  -- По Serial Monitor можем проверять напряжение датчиков , вводя 1 или 2  
  -- А так же там рабочий скрипт по предыдущей паре (up/down/blink)  

- С включенным Serial Monitor то закрываем пальцем фоторезистор,  
  то светим на него фонариком.  
  -- При одном состоянии значения будет ближе к 1023,  
     в другом - меньше 400-500  

2. Соединение с MQTT  

- Схема: первый комп читает данные с датчиков, посылает в облако с помощью MQTT,  
  второй комп это читает и как-то этим манипулирует  

- Вспоминаем два скрипта, которые были на лекции - subscribing и publishing  

- Находим второй компьютер, но для начала  

- Настраиваем первый компьютер  
  -- Делаем весь первый пункт и запускаем python  
  -- `read_sensor.py`  
	Подключаем библиотеку serial (и установив pyserial из этой библиотеки). Это позволит видеть ардуино.   
	Запускаем скрипт и проверяем, что данные с машинки точно считываются.  
  -- `publishing.py`  
	Соединяем publishing от mqtt и скрипт для чтения сенсоров  
	Другим скриптом (subscribe с лекции) подписываемся и смотрим, что умеем теперь публиковать  
	значения, принятые с резистора на ардуино  

- Настраиваем второй компьютер  
  -- Запускаем на нём `29.09.ino` и подключаем машинку (без всей схемы - нам нужен только светодиод на ней)  
  -- `subscribing.py`  
	Изменяем скрипт подписки на данные с первого компа  
	Принцип программы: когда приходит значение < 400, значит, резистор на первом компе получает много света -   
	светодиод на машинке нашего второго компа не горит.  
	Значение от 400 до 1023 - у резистора мало света (он закрыт пальцем),  
	сигнализируем об этом включенным светодиодом.  

3. Соединение  

- Включаем отправку и принятие данных   

- Пробуем закрывать и светить на фоторезистор  
 
- Смотрим результат  

*А никто не шутил, что так бомбы можно делать?"* (с) чел на паре  

Дополнение к записям Веснина  
===================================  
Датчик основан на том, что один из резисторов делаем светочувствительным  
С помощью Ардуино измеряем U (напряжениие)  
analogRead (в ардуиновском скрипте) возвращает число от 0 до 1024 - это показатель напряжения  
Микроконтроллер подключаем в точку изменения напряжения (типа левее неё максимум, в точке подключения спад, правее - 0)  

val = 1024 - ( R / (R + R~) ) * 1024   
R >> R~ →  0  
R << R~ →  1023  

От силы резистора меняется уровень падения (5V → 0)  

Принцип фоторезистора:  
Чем сильнее свет → тем больше выбивающихся электронов → тем больше сила тока  
