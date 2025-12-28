   
# アクティビティの取得

アクティビティの詳細を返します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
GET

```
## URL

```
/api/v2/activities/:activityId

```
## URL parameters

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| activityId | 数値 | アクティビティのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
  "id": 3153,
  "project": {
    "id": 92,
    "projectKey": "SUB",
    "name": "Subtasking",
    "chartEnabled": true,
    "useResolvedForChart": true,
    "subtaskingEnabled": true,
    "projectLeaderCanEditProjectLeader": false,
    "useWiki": true,
    "useFileSharing": true,
    "useWikiTreeView": true,
    "useOriginalImageSizeAtWiki": false,
    "textFormattingRule": "backlog",
    "archived": false,
    "displayOrder": 3,
    "useDevAttributes": true
  },
  "type": 0,
  "content": {
    "id": 92,
    "key_id": 121,
    "summary": "Comment",
    "description": "string",
    "comment": {
      "id": 7237,
      "content": "Comment"
    },
    "changes": [
      {
        "field": "milestone",
        "new_value": "R2014-07-23",
        "old_value": null,
        "type": "standard"
      }
    ]
  },
  "notifications": [
    {
      "id": 25,
      "alreadyRead": false,
      "reason": 2,
      "user": {
        "id": 25,
        "userId": "admin",
        "name": "admin",
        "roleType": 1,
        "lang": "ja",
        "nulabAccount": {
            "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
            "name": "admin",
            "uniqueId": "admin"
        },
        "mailAddress": "eguchi@nulab.example",
        "lastLoginTime": "2022-09-01T06:35:39Z"
      }
    }
  ],
  "createdUser": {
    "id": 25,
    "userId": "admin",
    "name": "admin",
    "roleType": 1,
    "lang": "ja",
    "nulabAccount": {
        "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
        "name": "admin",
        "uniqueId": "admin"
    },
    "mailAddress": "eguchi@nulab.example",
    "lastLoginTime": "2022-09-01T06:35:39Z"
  },
  "created": "2013-12-27T07:50:44Z"
}

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| type | 数値 | 最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:ユーザーがプロジェクトに参加16:ユーザーがプロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   