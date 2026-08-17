# iOS App Store Skills

Набор из четырёх связанных Codex-скиллов для быстрого создания portrait-only iPhone-приложения и подготовки его к App Review: от проверки идеи до релизного пакета.

Скиллы уменьшают число предсказуемых причин отклонения, но не гарантируют одобрение Apple. Финальное решение всегда принимает App Review, а проверки на реальном устройстве выполняются вручную.

## Что входит

| Этап | Скилл | Результат | Финальный статус |
| --- | --- | --- | --- |
| 1. Идея и политика | `generate-ios-app-ideas` | `AppSpec.md` и `AppPrivacy.yml` | `policy-approved` |
| 2. Дизайн | `design-ios-app-concept` | Полный дизайн экранов и иконка | `design-approved` |
| 3. Реализация | `build-ios-app-concept` | Xcode-проект, расширения, backend и release manifest | `implementation-verified` |
| 4. Релиз | `prepare-ios-app-store-release` | Архив, privacy-проверки, метаданные и review notes | `release-ready` |

Пайплайн рассчитан на UIKit и iOS 15 для основного приложения, iOS 16 для Lock Screen widget, portrait-only интерфейс и кодовую вёрстку без Storyboard/XIB. Unit- и UI-test targets намеренно не создаются ради скорости; это не отменяет сборку, статические проверки и ручную проверку релизной сборки.

Во всех приложениях обязательны:

- Bluetooth;
- камера;
- контакты;
- Face ID;
- геолокация;
- микрофон;
- чтение Фото;
- добавление в Фото;
- App Tracking Transparency;
- push-уведомления;
- AppMetrica;
- минимальный HTTPS backend;
- Lock Screen widget;
- Notification Service Extension;
- Notification Content Extension.

Каждое разрешение должно быть связано с реальной пользовательской функцией и запрашиваться только после понятного действия пользователя. Если обязательную возможность нельзя честно встроить в продукт, первый этап должен остановить пайплайн, а не маскировать риск для App Review.

## Установка в Codex

Codex ищет скиллы в `.agents/skills` текущего репозитория и в `$HOME/.agents/skills` пользователя. Символические ссылки поддерживаются, поэтому этот репозиторий можно обновлять независимо, не копируя папки вручную.

### Только для одного проекта

В корне проекта выполните:

```bash
mkdir -p .agents/skills
ln -s /absolute/path/to/skills/generate-ios-app-ideas .agents/skills/generate-ios-app-ideas
ln -s /absolute/path/to/skills/design-ios-app-concept .agents/skills/design-ios-app-concept
ln -s /absolute/path/to/skills/build-ios-app-concept .agents/skills/build-ios-app-concept
ln -s /absolute/path/to/skills/prepare-ios-app-store-release .agents/skills/prepare-ios-app-store-release
```

Замените `/absolute/path/to/skills` на абсолютный путь к клону этого репозитория.

### Для всех проектов пользователя

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /absolute/path/to/skills/generate-ios-app-ideas "$HOME/.agents/skills/generate-ios-app-ideas"
ln -s /absolute/path/to/skills/design-ios-app-concept "$HOME/.agents/skills/design-ios-app-concept"
ln -s /absolute/path/to/skills/build-ios-app-concept "$HOME/.agents/skills/build-ios-app-concept"
ln -s /absolute/path/to/skills/prepare-ios-app-store-release "$HOME/.agents/skills/prepare-ios-app-store-release"
```

Codex обычно обнаруживает изменения автоматически. Если новый скилл не появился, перезапустите Codex. Подробнее: [официальная документация OpenAI по созданию и подключению скиллов](https://learn.chatgpt.com/docs/build-skills).

## Быстрый старт

Откройте в Codex репозиторий будущего приложения. Скилл можно выбрать через `/skills`, явно упомянуть с `$` или позволить Codex выбрать его автоматически по описанию задачи.

### 1. Проверить или придумать идею

```text
$generate-ios-app-ideas
Придумай iPhone-приложение для планирования семейных поездок. Подготовь AppSpec.md и AppPrivacy.yml и проведи App Review feasibility gate.
```

Если идея уже есть:

```text
$generate-ios-app-ideas
Проверь эту идею для App Review и оформи спецификацию: <описание идеи>.
```

Не переходите дальше, пока `AppSpec.md` и `AppPrivacy.yml` не согласованы и статус не равен `policy-approved`.

### 2. Подготовить дизайн

```text
$design-ios-app-concept
Используй согласованные AppSpec.md и AppPrivacy.yml. Подготовь полный дизайн приложения и иконку.
```

Этап должен закончиться статусом `design-approved`. Дизайн обязан показывать честные сценарии запроса всех разрешений, privacy policy и состояния conditional policy modules, которые относятся к приложению.

### 3. Собрать приложение

```text
$build-ios-app-concept
Реализуй согласованные AppSpec.md, AppPrivacy.yml и дизайн. Собери приложение в <папка назначения>, bundle id: <bundle id>.
```

Скилл создаёт основной Xcode-проект, обязательные расширения, минимальный backend и release manifest. Этап завершается только после проверки реализации со статусом `implementation-verified`.

### 4. Подготовить релиз

```text
$prepare-ios-app-store-release
Подготовь реализацию к App Store Review. Проверь архив, privacy manifests, App Store metadata и review notes. Не отправляй сборку без моего явного подтверждения.
```

Релизный скилл сверяется с актуальными первичными источниками Apple во время запуска. Он готовит артефакты, но не загружает сборку и не отправляет её на ревью без отдельного явного разрешения пользователя.

Ожидаемые релизные файлы:

- `Release/release-manifest.json`;
- `Release/compliance-sources.json`;
- `Release/archive-validation.json`;
- `Release/app-store-privacy.json`;
- `Release/app-store-metadata/`;
- `Release/review-notes.md`;
- `Release/manual-device-checks.md`.

После успешной валидации статус меняется на `archive-validated`, затем на `release-ready`. Статус `submitted` допустим только после фактической отправки с явного разрешения пользователя.

## Статусы пайплайна

```text
idea-draft
  -> policy-approved
  -> design-approved
  -> implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

Статуса `device-tested` нет. Проверки на физическом iPhone фиксируются вручную в `Release/manual-device-checks.md` и остаются обязательной ответственностью владельца приложения перед отправкой.

## AppPrivacy.yml

`AppPrivacy.yml` — общий machine-readable source of truth для всех четырёх этапов. В нём фиксируются:

- причины и точки запроса разрешений;
- собираемые данные и их назначение;
- AppMetrica и другие сторонние SDK;
- tracking и ATT;
- backend-домены;
- privacy policy и support URL;
- ответы для App Store Privacy;
- conditional policy modules;
- блокеры релиза.

Файл должен описывать поведение приложения, но не содержать API keys, токены, сертификаты и другие секреты.

## Что потребуется перед релизом

- актуальные Xcode и iOS SDK;
- Apple Developer Team, signing и provisioning;
- настроенные APNs и AppMetrica;
- доступный production HTTPS backend;
- опубликованные privacy policy и support page;
- данные App Store Connect;
- тестовый аккаунт, инструкции, демоданные или оборудование для ревьюера, если они нужны приложению;
- ручная проверка разрешений, push, расширений, backend и основных сценариев на физическом iPhone.

## Проверка репозитория скиллов

После изменений запустите:

```bash
python3 evals/validate_pipeline.py
```

Проверка контролирует связи между четырьмя этапами, обязательные разрешения, статусы, privacy contract и ключевые разделы этой инструкции.

## Структура репозитория

```text
skills/
├── generate-ios-app-ideas/
│   ├── SKILL.md
│   ├── assets/AppPrivacy.template.yml
│   └── references/app-privacy-contract.md
├── design-ios-app-concept/SKILL.md
├── build-ios-app-concept/SKILL.md
├── prepare-ios-app-store-release/SKILL.md
├── evals/
└── README.md
```

При изменении пайплайна работайте в отдельной ветке, обновляйте общий privacy contract вместе с затронутыми скиллами и запускайте валидатор перед pull request. Изменчивые требования Apple не следует жёстко фиксировать в старой версии документации: релизный этап обязан заново проверить актуальные официальные источники.
