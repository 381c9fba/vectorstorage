# Развертывание ChromaDB с помощью Docker Compose

Этот репозиторий содержит конфигурацию Docker Compose для развертывания Векторной базы данных Faiss.

## Предварительные требования

* Docker установлен на вашей системе
* Docker Compose установлен на вашей системе

## Развертывание

1. Клонировать репозиторий: `git clone https://github.com/381c9fba/vectorstorage.git`
2. Перейти в директорию репозитория: `cd vectorstorage`
3. Создать файл Docker Compose: docker-compose up -d
4. Проверить, что Контейнер запущен: docker-compose ps

## Конфигурация

Вы можете настроить развертывание, редактируя файл `compose.yml`.

## Устранение проблем

* Проверить журналы Docker Compose: `docker-compose logs`

## Лицензия

Этот проект распространяется под лицензией [MIT License](https://opensource.org/licenses/MIT).
