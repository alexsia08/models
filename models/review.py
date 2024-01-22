# Краткий обзор результатов
class Review: 

    # Актуальные атаки
    Attack = "" # Название вектора атаки
    level = "Средний уровень" # Уровень атаки
    Decision = "Могут быть устранены в порядке планового технического обслуживания" # Путь решения
    Connected = "Атаки связаны с подбором учётных и проверкой регистрации пользователя для подбора пароля к учётной записи" # С чем связано

    # Рекомендации
    Disadvantage = "" # Обнаруженный недостаток
    Elimination = "Можно устранить на уровне WAF или исходного кода веб-ресурса. " # Как устранить
    Recommendation = "Рекомендуется проверить, что обнаруженные адреса электронной почты, номера телефонов действительно актуальны и сотрудники не подвергаются лишнему риску стать жертвой социальной инженерии." # Рекомендации

    # Итоговая оценка    
    Safety = "Средний уровень" # Безопасность
    Conditioned = "Не получилось провести обследование поддоменов, так как их много и выделенного времени не хватило на полный охват." # Обусловленный
    Effectiveness = "WAF (Qrator)" # Эффективность
    Action = "Успешно блокировал атаки, направленные на инъекции вредоносного кода" # Действия
    Awareness = "Проводимые атаки в ходе анализа защищённости уже должны быть известны Вашим специалистам"
    Measures = "Приняты меры для предотвращения обнаружения технологического стека и свободного доступа к панели администрирования" # Меры
  
# Итоговая оценка СТОИТ ПОСЛЕ реестра недопустимых событий!!!

