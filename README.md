# aviata-ticket


## Цель
- Кеш направлений и цен на месяц от текущей даты

## Условия
- Направления определены и являются **константой**
- Функция обновляющая данные каждый день после **00:00**, на месяц вперёд
- Отображение - на своё усмотрение

## Направления

  `ALA`  `Алматы`  
  `TSE`  `Астана`  
  `MOW`  `Москва`  
  `LED`  `С-Петербург`  
  `CIT`  `Шымкент`  


  | Из  | До |
  |:-:  |:-:  |
  | ALA | TSE |
  | TSE | ALA |
  | ALA | MOW |
  | MOW | ALA |
  | ALA | CIT |
  | CIT | ALA |
  | TSE | MOW |
  | MOW | TSE |
  | TSE | LED |
  | LED | TSE |

---------------------

## API
- Документация: [DOC](https://docs.kiwi.com/#flights-flights-get)


### API Process

1. **Поиск:**
- URL: `https://api.skypicker.com/flights`
- Method: `GET`
- Headers: `Content-Type`: `application/json`
- Query:  

  - Направления:  

    | Параметр  | Значение     | Required |
    |:-:        |:-:           |:-:       |  
    | fly_from  | `IATA_code`  | True     |
    | fly_ty    | `IATA_code`  | True     |  

    _Пример:_ `?fly_from=ALA&fly_to=CIT`

  - Дата  

    | Параметр  | Значение     | Required |
    |:-:        |:-:           |:-:       |
    | date_from | `%d/%m/%Y`   | True     |
    | date_to   | `%d/%m/%Y`   | True     |

  - Пассажиры  

    | Параметр  | Значение     | Required |
    |:-:        |:-:           |:-:       |  
    | adults    | `int`        | False    |
    | children  | `int`        | False    |
    | infants   | `int`        | False    |

    _Пример:_ `adults=1&infants=1`

- Result: `json`.  _В нём необходимо найти самый дешёвый перелёт среди всех:_ `"data"` _**( data > price )**_

- Field to use: `booking_token`  `price`
