   
# 種別の追加

プロジェクトに種別を追加します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/issueTypes

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | 種別の名前 |
| color (必須) | 文字列 | 種別の背景色：以下から指定”#e30000""#990000""#934981""#814fbc""#2779ca""#007e9a""#7ea800""#ff9200""#ff3265""#666665” |
| templateSummary | 文字列 | 課題テンプレートの件名 |
| templateDescription | 文字列 | 課題テンプレートの詳細 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 1,
    "projectId": 1,
    "name": "バグ",
    "color": "#990000",
    "displayOrder": 0,
    "templateSummary": "件名",
    "templateDescription": "詳細"
}

```
   