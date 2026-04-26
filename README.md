# VLESS Config Generator Bot

Telegram bot для создания и распространения VLESS конфигов через GitHub Pages.

## 📋 Структура проекта

```
workspace/
├── bot/                    # Код Telegram бота
│   ├── main.py            # Основной файл бота
│   └── __init__.py
├── core/                   # Основная логика
│   ├── vless_generator.py # Генерация VLESS конфигов
│   ├── github_manager.py  # Работа с GitHub API
│   └── __init__.py
├── configs/                # Документация по конфигам
│   └── README.md          # Гайд по настройке единого репозитория
├── .env.example           # Пример переменных окружения
├── .env                   # Ваши настройки (заполните!)
├── requirements.txt       # Зависимости Python
├── README.md              # Главный файл
├── START_HERE.md          # ⭐ НАЧНИТЕ ОТСЮДА!
├── QUICK_START_PAGES.md   # Быстрая настройка за 5 минут
├── ENV_SETUP_GUIDE.md     # Как заполнить .env файл
├── PAGES_CHECKLIST.md     # Чек-лист проверки
├── README_PAGES.md        # Полное оглавление документации
└── GITHUB_PAGES_SETUP.md  # Полное руководство
```

## ✨ Возможности

- ✅ Только для пользователя @Weleredz
- ✅ Две кнопки: "🔑 Get Proxy" и "🔄 Update"
- ✅ Генерация VLESS WebSocket конфигов с TLS
- ✅ **Единый репозиторий** для хранения и GitHub Pages
- ✅ Автоматическое создание `index.html` для страниц
- ✅ Сохранение UUID при обновлении конфига
- ✅ Автоматическая очистка старых конфигов

## 🚀 Быстрый старт

### ⚡ Самый быстрый способ (5 минут)

**ОТКРОЙТЕ [`START_HERE.md`](./START_HERE.md)** - там ваш план действий!

Или следуйте этой инструкции:

### Шаг 1: Создайте репозиторий для конфигов

1. Перейдите на https://github.com/new
2. Название: `vless-configs`
3. **Видимость: Public** (обязательно для бесплатного GitHub Pages)
4. Нажмите **Create repository**

### Шаг 2: Включите GitHub Pages

1. В репозитории перейдите в **Settings** → **Pages**
2. Source: `Deploy from a branch`
3. Branch: `main`, Folder: `/ (root)`
4. Нажмите **Save**

Ваш URL будет: `https://your-username.github.io/vless-configs/`

### Шаг 3: Получите токены

#### Telegram Bot Token
1. Напишите @BotFather в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям

#### GitHub Personal Access Token
1. GitHub Settings → Developer settings → Personal access tokens
2. Create token (classic)
3. Выберите scope: `repo`
4. Скопируйте токен

### Шаг 4: Настройте переменные окружения

```bash
cp .env.example .env
```

Отредактируйте `.env`:

```bash
# Telegram
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# GitHub
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
CONFIG_REPO=your-username/vless-configs
PAGES_REPO=your-username/vless-configs

# VLESS сервер
VLESS_ADDRESS=your-domain.com
VLESS_PORT=443
VLESS_PATH=/vless
VLESS_SNI=your-domain.com
```

⚠️ **Важно:** `CONFIG_REPO` и `PAGES_REPO` указывают на **один и тот же репозиторий**!

### Шаг 5: Установите зависимости

```bash
pip install -r requirements.txt
```

### Шаг 6: Запустите бота

```bash
python bot/main.py
```

## 📖 Использование

1. Отправьте боту `/start`
2. Нажмите **"🔑 Get Proxy"** для генерации нового конфига
3. Нажмите **"🔄 Update"** для обновления существующего

Бот автоматически:
- Сгенерирует уникальный VLESS конфиг
- Загрузит его в репозиторий (`configs/username_timestamp.txt`)
- Обновит `index.html` на GitHub Pages
- Отправит вам ссылку на конфиг

## 🔗 Доступ к конфигам

После генерации конфиг доступен по URL:

```
https://your-username.github.io/vless-configs/configs/Weleredz_20240126_143022.txt
```

Главная страница со списком всех конфигов:

```
https://your-username.github.io/vless-configs/
```

## 🏗 Архитектура

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│  Telegram   │────▶│  VLESS Bot   │────▶│  GitHub Repo     │
│   User      │◀────│  (bot/main)  │◀────│  (vless-configs) │
└─────────────┘     └──────────────┘     └──────────────────┘
                                                │
                                        ┌───────┴────────┐
                                        │                │
                                  configs/          index.html
                                  (конфиги)        (GitHub Pages)
                                        │                │
                                        └───────┬────────┘
                                                ▼
                                    https://username.github.io
```

## 📁 Структура репозитория конфигов

После первого запуска бот создаст:

```
vless-configs/
├── configs/
│   ├── .gitkeep
│   ├── Weleredz_20240126_143022.txt
│   └── Weleredz_20240127_091530.txt
├── index.html          # Автогенерируемая страница
└── README.md
```

## ⚙️ Детальная настройка

Для подробной инструкции по настройке смотрите:

- **[`START_HERE.md`](./START_HERE.md)** - 🌟 НАЧНИТЕ ОТСЮДА! (ваш план действий)
- **[`QUICK_START_PAGES.md`](./QUICK_START_PAGES.md)** - ⚡ Пошаговая настройка за 5 минут
- **[`ENV_SETUP_GUIDE.md`](./ENV_SETUP_GUIDE.md)** - Как заполнить .env файл
- **[`PAGES_CHECKLIST.md`](./PAGES_CHECKLIST.md)** - ✅ Чек-лист проверки
- [`GITHUB_PAGES_SETUP.md`](./GITHUB_PAGES_SETUP.md) - 📖 Полное руководство
- [`configs/README.md`](./configs/README.md) - Управление конфигами

## 🔧 Решение проблем

### GitHub Pages показывает 404
- Подождите 2-3 минуты после первой загрузки
- Проверьте, что репозиторий Public
- Убедитесь, что `index.html` существует

### Ошибка загрузки конфига
- Проверьте токен GitHub (scope `repo`)
- Убедитесь в формате `CONFIG_REPO`: `owner/repo`

### Бот не отвечает
- Проверьте `BOT_TOKEN`
- Убедитесь, что ваш username @Weleredz

## 🔒 Безопасность

⚠️ **Важно:**
- Репозиторий должен быть **Public** для бесплатного GitHub Pages
- Конфиги доступны публично по прямой ссылке
- Не делитесь ссылками с непроверенными людьми
- Регулярно удаляйте старые конфиги

## 📦 Зависимости

- `python-telegram-bot==21.0` - Telegram Bot API
- `PyGithub==2.3.0` - GitHub API клиент
- `python-dotenv==1.0.0` - Загрузка .env файлов

## 📝 Лицензия

Приватный репозиторий для личного использования.
