# Build iOS App Skill

Один Codex-скилл для создания portrait-only iPhone-приложения и подготовки его к App Store Review: идея, дизайн, реализация и релизный пакет в одном возобновляемом процессе.

Скилл уменьшает число предсказуемых причин отклонения, но не гарантирует одобрение Apple. Финальное решение принимает App Review, а проверки на физическом iPhone выполняются владельцем приложения вручную.

## Как работает пайплайн

| Этап | Результат | Статус после проверки |
| --- | --- | --- |
| Идея и политика | `AppSpec.md`, `AppPrivacy.yml`, App Review feasibility gate | `policy-approved` |
| Дизайн | Экраны, permission UX, widget, notification UI и иконка | `design-approved` |
| Реализация | Xcode-проект, extensions, AppMetrica, backend и release manifest | `implementation-verified` |
| Релиз | Архив, privacy report, metadata и review notes | `archive-validated`, затем `release-ready` |

Между этапами скилл показывает артефакты, решения и блокеры, затем останавливается. Следующий этап начинается только после нового явного сообщения пользователя, которое утверждает текущий результат и разрешает конкретный следующий этап.

Начальная просьба «сделай всё», молчание, неоднозначная похвала или старое разрешение не считаются аппрувом. При запросе изменений скилл остаётся на текущем этапе и повторно запрашивает подтверждение после обновлённого результата.

Отправка сборки, изменение App Store Connect и отправка на App Review требуют ещё одного отдельного разрешения непосредственно перед внешним действием.

## Обязательный продуктовый brief

Пайплайн рассчитан на UIKit и iOS 15 для основного приложения, iOS 16 для Lock Screen widget, iPhone-only portrait interface и кодовую вёрстку без Storyboard/XIB. Unit- и UI-test targets не создаются; проверка реализации использует сборку, запуск, статическую инспекцию, backend smoke checks и ручной device checklist.

Каждое приложение должно честно и через реальную пользовательскую функцию использовать:

- Bluetooth;
- камеру;
- контакты;
- Face ID;
- геолокацию;
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

Если обязательную возможность нельзя органично встроить в продукт, скилл останавливает feasibility gate, а не создаёт декоративный запрос разрешения.

## Установка в Codex

Codex обнаруживает скиллы в `.agents/skills` текущего репозитория и в `$HOME/.agents/skills` пользователя. Символические ссылки позволяют обновлять этот репозиторий без ручного копирования файлов.

### Для одного проекта

В корне проекта выполните:

```bash
mkdir -p .agents/skills
ln -s /absolute/path/to/skills/build-ios-app .agents/skills/build-ios-app
```

### Для всех проектов пользователя

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /absolute/path/to/skills/build-ios-app "$HOME/.agents/skills/build-ios-app"
```

Замените `/absolute/path/to/skills` на абсолютный путь к клону репозитория. Если скилл не появился автоматически, перезапустите Codex. Подробнее: [официальная документация OpenAI по скиллам](https://learn.chatgpt.com/docs/build-skills).

## Использование

Скилл можно выбрать через `/skills`, упомянуть явно или вызвать естественным запросом.

### Начать с новой идеи

```text
$build-ios-app
Придумай и создай приложение для планирования семейных поездок.
```

### Начать со своей идеи

```text
$build-ios-app
Проверь идею для App Review и начни пайплайн: <описание идеи>.
```

### Продолжить существующий проект

```text
$build-ios-app
Продолжи работу с текущего утверждённого этапа.
```

Скилл читает `AppSpec.md`, `AppPrivacy.yml`, дизайн и `Release/release-manifest.json`, определяет первый незавершённый этап и не повторяет уже утверждённую работу. Если старый проект не содержит журнала аппрувов, скилл покажет последний результат и запросит свежее подтверждение.

## Пример аппрувов

После каждого gate достаточно ответить явно:

```text
Утверждаю идею, переходи к дизайну.
```

```text
Дизайн подходит, начинай реализацию.
```

```text
Реализация принята, готовь релиз.
```

Каждое сообщение разрешает только названный следующий этап. Запрошенные изменения отменяют текущий gate до повторной проверки.

## Статусы

```text
idea-draft
  -> policy-approved
  -> design-approved
  -> implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

Ручные проверки Bluetooth, камеры, Contacts, Face ID, геолокации, микрофона, PhotoKit, ATT, APNs, push и специального оборудования записываются в `Release/manual-device-checks.md`. Они не создают отдельного статуса.

## AppPrivacy.yml

`AppPrivacy.yml` — machine-readable source of truth для:

- разрешений, feature triggers и purpose copy;
- локальных и передаваемых данных;
- AppMetrica и других SDK;
- ATT и tracking behavior;
- backend и публичных доменов;
- privacy policy и App Store Privacy;
- conditional policy modules;
- release blockers;
- журнала явных пользовательских аппрувов.

Файл не должен содержать API keys, токены, сертификаты, пароли и другие секреты.

## Структура

```text
build-ios-app/
├── SKILL.md
├── scripts/
│   └── validate_skill.py
├── references/
│   ├── idea-stage.md
│   ├── design-stage.md
│   ├── build-stage.md
│   ├── release-stage.md
│   ├── app-privacy-contract.md
│   └── AppPrivacy.template.yml
└── version.json
```

`SKILL.md` отвечает за triggers, usage, определение этапа и approval gates. Подробные требования каждого этапа загружаются из `references/` только тогда, когда этот этап разрешён. `version.json` содержит версию, changelog, категорию и автора.

## Проверка скилла

После изменения файлов выполните из корня репозитория:

```bash
python3 build-ios-app/scripts/validate_skill.py
```

Валидатор проверяет единственность устанавливаемого скилла, обязательные файлы, frontmatter, stage routing, approval contract, разрешения, privacy schema, README и `version.json`.

## Что потребуется перед релизом

- актуальные Xcode и iOS SDK;
- Apple Developer Team, signing и provisioning;
- настроенные APNs и AppMetrica;
- доступный production HTTPS backend;
- опубликованные privacy policy и support page;
- данные App Store Connect;
- reviewer account, sample data или инструкции к оборудованию, когда они нужны;
- ручная проверка релизной сборки на физическом iPhone.
