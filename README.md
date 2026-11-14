# 内閣官房

内閣官房のウェブサイト（www.cas.go.jp）が公開する資料を収録した Queria のデータセット（`queria/cas`）です。

## 計画・通知等（plans）


[行政事業レビュー見える化サイト](https://rssystem.go.jp)のレビューシート（政策・施策、法令等、2024 年度から）が「関係する計画・通知等」に挙げる URL のうち、内閣官房のサイト（www.cas.go.jp）の PDF を取得し、ページごとの本文にしています。首相官邸のサイトの会議のページ（www.kantei.go.jp/jp/singi/）は内閣官房のサイト（www.cas.go.jp/jp/seisakukaigi/）に移転したので、シートの URL が官邸のものも移転先から取得します（`plans.documents` の `fetched_url`）。

| テーブル | 内容 |
| --- | --- |
| `plans.documents` | 1 行が 1 つの計画・通知等の PDF の URL。名前・sha256・ページ数・取得日時 |
| `plans.pages` | 1 行が 1 ページ。PDF から取り出して NFKC で正規化した本文 |

- 文字コードの対応表が無いフォントの文字は、Adobe-Japan1 の CID とみなして文字に戻しています（`cid_repaired_chars`）
- ほかのサイトの文書と HTML のページは入っていません。シートの URL のうち、取得できなかったもの（リンク切れなど）と開けない PDF も入っていません
- 全文検索の索引は持っていません。`plans.pages` の `text` を検索してください
- 取得と Parquet 化は dataset-shared の `review_plans.py` で行います。PDF は 1 秒に 1 回の頻度で取得します

## 出典と利用条件

- 行政事業レビュー見える化サイト（https://rssystem.go.jp）のレビューシートの URL を使っています
- 各資料は内閣官房のウェブサイト（https://www.cas.go.jp/）のコンテンツで、ウェブサイトの利用規約（政府標準利用規約）に従います。使うときは出典と加工したことを書いてください
- 図表には内閣官房以外の著作物が含まれることがあります。このデータセットは本文の文字だけを持ち、PDF の原本は保存していません

## ビルド

```bash
git submodule update --init
uv sync
bash scripts/build.sh
```
