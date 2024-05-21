[![Actions Status](https://github.com/yuukis/yamanashi-icalendar-updater/workflows/Release%20event.ics/badge.svg)](https://github.com/yuukis/yamanashi-icalendar-updater/actions)

# yamanashi-icalendar-updater

山梨県の IT 勉強会イベントカレンダーを iCalendar 形式で生成するスクリプト

<!-- ABOUT THE PROJECT -->
## このプロジェクトについて

山梨県で開催されているテック系イベントのカレンダーを iCalendar 形式で生成し、公開用リポジトリにアップロードするシンプルなスクリプトです。

このスクリプトでは [Yamanashi Developer Hub](https://hub.yamanashi.dev) に掲載されているイベントデータを API で取得し、iCalendar 形式に変換しています。

iCalendar ファイルは下記の URL から利用できます。

```
https://calendar.yamanashi.dev/event.ics
```

<!-- GETTING STARTED -->
## スタートガイド

### 必要条件

* Python 3.8 以降 

### インストール

1. [GitHub](https://github.com/settings/tokens) で Personal access token を取得します
2. このリポジトリをクローンします
    ```sh
    git clone https://github.com/yuukis/yamanashi-icalendar-updater.git
    ```
3. 依存パッケージをインストールします
    ```sh
    pip install -r requirements.txt
    ```
4. `.env` ファイルを作成し、下記の内容を記述します
    ```ini
    GITHUB_TOKEN=あなたのパーソナルアクセストークン
    GITHUB_OWNER=保存先リポジトリのオーナー名
    GITHUB_REPO=保存先リポジトリ名
    ```

<!-- USAGE EXAMPLES -->
## 使い方

```sh
python main.py
```

<!-- LICENSE -->
## ライセンス

Apache License, Version 2.0

<!-- CONTACT -->
## 連絡先

しみず ゆうき - [@yuuki_maxio](https://x.com/yuuki_maxio) 


<!-- ACKNOWLEDGEMENTS -->
## 謝辞

* [shingen.py](https://shingenpy.connpass.com)
  - 山梨県の python ユーザーコミュニティ