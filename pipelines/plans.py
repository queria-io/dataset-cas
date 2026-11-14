"""行政事業レビューのシートが「関係する計画・通知等」に挙げる、内閣官房のサイトの PDF をページごとの本文にする。

首相官邸のサイトの会議のページ（/jp/singi/）は内閣官房のサイト（/jp/seisakukaigi/）に移転したので、
シートの URL が官邸のものでも移転先から取得する。

取得と Parquet 化は shared/review_plans.py。

出典: 行政事業レビュー見える化サイト https://rssystem.go.jp 、内閣官房ウェブサイトの各資料
"""

from pathlib import Path

from shared import review_plans

USER_AGENT = "queria-dataset-cas (+https://queria.io/)"
HOSTS = {"www.cas.go.jp"}
MOVED = {"https://www.kantei.go.jp/jp/singi/": "https://www.cas.go.jp/jp/seisakukaigi/"}
PDF_DIR = Path("data/plans")
PARQUET_DIR = Path("data/parquet")


def download_plans() -> None:
    review_plans.download_plans(
        HOSTS, user_agent=USER_AGENT, pdf_dir=PDF_DIR, moved=MOVED
    )


def build_plans_parquet() -> None:
    review_plans.build_plans_parquet(
        user_agent=USER_AGENT, pdf_dir=PDF_DIR, parquet_dir=PARQUET_DIR
    )
