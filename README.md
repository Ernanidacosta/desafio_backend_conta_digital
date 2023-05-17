# Desafio Backend

O desafio consiste em criar uma API REST para uma Conta Digital, onde o usuário poderá realizar pagamentos para seus amigos e adicionar cartões de crétido, que será consumida por um aplicativo (Android e iOS). Onde o usuário irá cadastrar/listar/editar/apagar um cartão quando desejar e transferir e listar o extrato de pagamentos.


### POST `/account/person`
Esse método deve receber um novo usuário e inseri-lo em um banco de dados para ser consumido pela própria API.
```json
{
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "password": "*****",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce"
}
```
| Campo       | Tipo   |
|-------------|--------|
| first_name  | String |
| last_name   | String |
| birthday    | String |
| password    | String |
| username    | String |

### GET `/account/friends`
Esse método da API deve retornar o seguinte JSON com os amigos do usuário
```json
[
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce"
  },
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce"
  },
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce"
  }
]
```

| Campo       | Tipo   |
|-------------|--------|
| first_name  | String |
| last_name   | String |
| birthday    | String |
| username    | String |

### POST `/account/card`
Esse método deve receber um cartão novo e inseri-lo em um banco de dados para ser consumido pela própria API.
```json
{
   "card_id": "70c881d4a26984ddce"
   "title": "Cartão 1",
   "pan": "5527952393064634",
   "expiry_mm": "03",
   "expiry_yyyy": "2022",
   "security_code": "656",
   "date":"26/11/2015"
}
```
| Campo       | Tipo   |
|-------------|--------|
| title       | String |
| pan         | String |
| expiry_mm   | String |
| expiry_yyy  | String |
| security_code | String |
| date        | String |


### GET `/account/cards`
Esse método da API deve retornar o seguinte JSON com os cartões cadastrados pelo usuário
```json
[
  {
    "title":"Cartão 1",
    "pan": "5527952393064634",
    "expiry_mm": "03",
    "expiry_yyyy": "2022",
    "security_code": "656",
    "date":"26/11/2015"
  },
  {
     "title":"Cartão 2",
     "pan": "5527952393064634",
     "expiry_mm": "03",
     "expiry_yyyy": "2022",
     "security_code": "656",
     "date":"26/11/2015"
  },
  {
     "title":"Cartão 2",
     "pan": "5527952393064634",
     "expiry_mm": "03",
     "expiry_yyyy": "2022",
     "security_code": "656",
     "date":"26/11/2015"
  }
]
```

| Campo       | Tipo   |
|-------------|--------|
| title       | String |
| pan         | String |
| expiry_mm   | String |
| expiry_yyy  | String |
| security_code | String |
| date        | String |



Após o usuário adicionar todos os cartões e localizar seus amigos, ele poderá realizar uma transferência.
Para isso, você precisará fazer o método `transfer` na sua API.

### POST `/account/transfer`
Esse método irá receber os dados da compra, junto com os dados do usuário.
```json
{
   "friend_id": "70c881d4a26984ddce",
   "total_to_transfer": 100,
   "billing_card": {
      "card_id": "70c881d4a26984ddce"
   }
}

```

+ Transfer

| Campo        | Tipo       |
|--------------|------------|
| friend_id    | String     |
| total_to_pay | int (in cents)|
| billing_card  | CreditCard |

+ BillingCard

| Campo            | Tipo   |
|------------------|--------|
| card_id          | String |


### GET `/account/bank-statement`
Esse método deve retornar todas as transferencias realizadas entre os amigos na API
```json
[
   {
      "user_id":"70c881d4a26984ddce",
      "friend_id":"70c881d4a26984ddce",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce"
   },
   {
      "user_id":"70c881d4a26984ddce",
      "friend_id":"70c881d4a26984ddce",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce"
   },
   {
      "user_id":"70c881d4a26984ddce",
      "friend_id":"70c881d4a26984ddce",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce"
   },
]
```
| Campo            | Tipo   |
|------------------|--------|
| user_id          | String |
| friend_id        | String |
| value            | int (in cents)    |
| date             | String |
| from_card        | String |

### GET `/account/bank-statement/{usertId}`
Esse método deve retornar todos as transferencias realizadas na API por um usuário específico
```json
[
   {
      "user_id":"70c881d4a26984ddce",
      "friend_id":"70c881d4a26984ddce",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce"
   },
   {
      "user_id":"70c881d4a26984ddce",
      "friend_id":"70c881d4a26984ddce",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce"
   },
]
```
