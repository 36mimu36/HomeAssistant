# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリのコードを操作する際のガイダンスを提供します。

## 環境

これは Home Assistant OS の設定リポジトリです。作業ディレクトリは `/root/config/` で、Home Assistant の設定ファイルが含まれています。

- **Home Assistant Core**: バージョンは `/root/config/.HA_VERSION` に表示されています
- **プライマリURL**: http://home.local:8123
- **設定ルート**: `/root/config/`

## 設定アーキテクチャ

### 分割設定パターン

このセットアップは Home Assistant の分割設定パターンを使用しており、`configuration.yaml` が各ドメインごとに個別のYAMLファイルをインクルードしています：

```yaml
automation: !include automations.yaml
binary_sensor: !include binary_sensor.yaml
climate: !include climate.yaml
script: !include scripts.yaml
sensor: !include sensor.yaml
# ... など
```

`template:` ドメインは `!include_dir_merge_list templates/` を使用しており、`templates/` ディレクトリ内のすべてのYAMLファイルを単一のリストにマージします。

### カスタムコンポーネント

カスタム統合は `/root/config/custom_components/` にあります：
- `hacs/` - Home Assistant Community Store
- `smartir/` - スマートIRリモコン
- `delete/` - delete-file-home-assistant 統合
- `webrtc/` - WebRTC カメラストリーミング
- `_device_manager/` - デバイス管理ユーティリティ

### 主要な設定機能

- **認証**: 標準の homeassistant 認証と 192.168.1.0/24 用の trusted_networks の両方を使用
- **フロントエンド**: `!include_dir_merge_named` を使用して `themes/` ディレクトリからテーマを読み込み
- **ローカライゼーション**: 多くのオートメーションとスクリプトに日本語のテキスト/コメントが含まれています

## 一般的なコマンド

### 設定の検証
```bash
ha core check --config /root/config
```

### Home Assistant の再起動
```bash
ha core restart
```

### ログの表示
```bash
ha core logs
```

### バックアップ管理
```bash
ha backups list
ha backups new --name "backup-name"
ha backups restore <slug>
```

### アドオン管理
```bash
ha addons list
ha addons info <addon-name>
ha addons start <addon-name>
ha addons stop <addon-name>
```

### コアコマンド
```bash
ha core info        # Core情報の表示
ha core update      # Home Assistant Core の更新
ha core rebuild     # Core コンテナの再構築
```

## ファイルパスと場所

- **設定**: `/root/config/configuration.yaml`
- **オートメーション**: `/root/config/automations.yaml` (多数のオートメーションを含む大きなファイル)
- **スクリプト**: `/root/config/scripts.yaml`
- **テンプレート**: `/root/config/templates/*.yaml`
- **データベース**: `/root/config/home-assistant_v2.db` (SQLiteデータベース、gitignore対象)
- **ログ**: `/root/config/home-assistant.log.1`, `home-assistant.log.old`
- **シークレット**: `/root/config/secrets.yaml` (gitignore対象)
- **ESPHome**: `/root/config/esphome/` (ESPHomeデバイス設定)
- **ブループリント**: `/root/config/blueprints/` (オートメーションブループリント)
- **Zigbee2MQTT**: `/root/config/zigbee2mqtt/` (gitignore対象)

## Git の使用

リポジトリには以下を除外する包括的な `.gitignore` があります：
- 機密ファイル (secrets.yaml、データベースファイル)
- ログと一時ファイル
- 生成されたコンテンツ (tts/、www/、image/)
- 統合固有のデータ (zigbee2mqtt/)

## 開発メモ

- オートメーションやスクリプトを編集する際は、UI を使用するよりも YAML ファイルを直接編集することを推奨します（UI はファイル全体を再フォーマットする可能性があります）
- テンプレートセンサーとエンティティは `templates/` ディレクトリ内の複数のファイルに分割されています
- 設定では多くのエンティティ名と説明に日本語を使用しています
- カスタムコンポーネントは `deps/` ディレクトリに依存関係がある場合があります
- システムには go2rtc がカメラストリーミング用に含まれています（バイナリと設定がルートに存在）
