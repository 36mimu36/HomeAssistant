# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 環境

これは Home Assistant OS の設定リポジトリです。

- **Home Assistant Core**: バージョンは `.HA_VERSION` に表示されています
- **プライマリURL**: http://home.local:8123
- **本番環境パス**: `/root/config/` (HA OS内)

**注意**: このリポジトリはローカルにマウントされて編集され、本番環境（`/root/config/`）にデプロイされます。

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

カスタム統合は `custom_components/` にあります：
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

以下のコマンドは **Home Assistant OS のターミナル（SSH等）** で実行します：

```bash
# 設定の検証
ha core check

# Home Assistant の再起動
ha core restart

# ログの表示
ha core logs

# バックアップ
ha backups list
ha backups new --name "backup-name"

# アドオン管理
ha addons list
ha addons info <addon-name>

# Core情報
ha core info
```

## 主要ファイル

- **automations.yaml**: 約2000行以上のオートメーション定義（大きなファイル）
- **scripts.yaml**: スクリプト定義
- **templates/**: テンプレートエンティティ（sensor, binary_sensor, switch, light, fan, lock, weather）
- **esphome/**: ESPHomeデバイス設定
- **secrets.yaml**: 機密情報（gitignore対象）

## オートメーション記述パターン

このリポジトリのオートメーションは以下の構造に従います：

```yaml
- id: 'タイムスタンプID'
  alias: 日本語のオートメーション名
  description: '動作概要と目的の詳細な説明'
  triggers:
    - trigger: state/numeric_state/time_pattern
      entity_id: [エンティティリスト]
      # トリガー固有の設定
  conditions: []  # または条件リスト
  actions:
    - choose:  # 条件分岐が多い
        - conditions: [...]
          sequence: [...]
    # または直接アクション
  mode: restart/single/queued
```

**特徴的なパターン:**
- `variables:` でテンプレート変数を定義してから使用
- `repeat:` と `while:` で状態監視ループ
- `choose:` で複雑な条件分岐
- トリガーに `id:` を付けて `trigger.id` で判別

## 開発メモ

- オートメーションやスクリプトは **YAML ファイルを直接編集** すること（UIはファイル全体を再フォーマットする）
- エンティティ名と説明は **日本語** を使用
- go2rtc がカメラストリーミング用に含まれています（`go2rtc.yaml`）

## 参照ドキュメント

以下のドキュメントとその下層ページすべてに準拠すること：

### 公式ドキュメント
- https://www.home-assistant.io/docs/
  - 特に https://www.home-assistant.io/docs/automation/ とそのサブページ

### 開発者向けドキュメント
- https://developers.home-assistant.io/

## 開発ルール

1. オートメーション実装前に、該当する公式ドキュメントのページを確認すること
2. トリガー、コンディション、アクションの記述は公式の規約・パターンに従うこと
3. 不明点がある場合は、上記ドキュメントを参照して確認すること
4. ドキュメントに記載のベストプラクティスに従うこと
