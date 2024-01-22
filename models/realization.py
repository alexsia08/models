# Результаты реализации недопустимых событий
class Realization: 
    
    # SQL-инъекция в форму авторизации в личном кабинете
    Implemented_event = "После компрометации личного кабинета (чтение данных пользователей, исполнение произвольного кода) может привести к потери работоспособности кабинета из-за действий злоумышленника."
    Tools = "Sqlmap, собственные скрипты на Python"
    Attacked_address = "https://portal.test.ru/auth "
    Triggered_protection = "WAF, была блокировка"
    Period = "10.10.2023 – 20.10.2023"
    Description = "SQL-инъекция подразумевает добавление к пользовательским данным управляющих конструкция языка SQL для чтения, изменения данных. В зависимости от типа уязвимости может дойти до исполнения произвольного кода"
    Results_attack = "За время проверки не удалось обойти WAF. Ограничений на количество принимаемых запросов с одного IP-адреса не было замечено. Методов защиты от автоматизированного перебора вредоносных запросов (CAPTCHA, CSRF-токен не были замечены)"
    Recommendations = "Добавить в форму авторизации CAPTCHA, CSRF-токен. Обращать внимание на WAF на аномальные запросы, коррелировать до инцидентов, если это возможно"