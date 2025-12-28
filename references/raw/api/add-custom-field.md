   
# カスタム属性の追加

プロジェクトに新しいカスタム属性を追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields

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
| typeId (必須) | 数値 | カスタム属性の形式1: 文字列2: 文章3: 数値4: 日付5: 単一リスト6: 複数リスト7: チェックボックス8: ラジオ |
| name (必須) | 文字列 | カスタム属性の名前 |
| applicableIssueTypes[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 |
| description | 文字列 | カスタム属性の説明 |
| required | 真偽値 | 必須な属性とする場合はtrue |

## 追加パラメーター (数値属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 数値 | 最小値 |
| max | 数値 | 最大値 |
| initialValue | 数値 | 初期値 |
| unit | 文字列 | 単位 |

## 追加パラメーター (日付属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 文字列 | 最小値 (yyyy-MM-dd) |
| max | 文字列 | 最大値 (yyyy-MM-dd) |
| initialValueType | 数値 | 1:当日 2: 当日 + initialShift 3:指定日 |
| initialDate | 文字列 | 初期値 (yyyy-MM-dd) |
| initialShift | 数値 | 差分日数 |

## 追加パラメーター (リスト属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| items[][(複数指定可)](/ja/docs/backlog/tips) | 文字列 | リスト項目 |
| allowInput | 真偽値 | その他直接入力を許可 |
| allowAddItem | 真偽値 | 項目の追加を許可 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "projectId": 5,
    "typeId": 1,
    "name": "バグ専用属性",
    "description": "",
    "required": false,
    "applicableIssueTypes": [1]
}

```
   