# 無料で学べる 日商簿記3級

日商簿記3級を独学で合格したい人のための、**無料の教科書と問題集**です。
高校生・大学生から、働きながら勉強する社会人まで、予備知識ゼロで読めることを目指しています。

**サイトで読む**:<https://kim-parkchik.github.io/nissho-boki3/>

- 費用は一切かかりません。印刷・コピー・授業での利用も自由です(ライセンスは下記)。
- 解説 → 例題 → 練習問題 → 解答・解説 の順に、1章ずつ進められます。
- 間違いを見つけたら、[Issue](../../issues/new/choose) で教えてください。すぐに直します。

## 対象とする試験範囲

**2027年度(2027年4月1日以降に実施される試験)の出題区分表**に合わせて作っています。

2027年度から、紙の手形・小切手に関する論点が削除され、普通預金の明記や、
売上原価対立法・定率法・固定資産の除却が2級から3級へ移るなどの変更があります。
2026年度中(2027年3月31日まで)に受験する人は、範囲が一部異なるので注意してください。

> 出題範囲の正式な情報は、日本商工会議所の「商工会議所の検定試験」サイト(<https://www.kentei.ne.jp/>)で必ず確認してください。

## 目次

| 章 | 内容 | 状態 |
|---|---|---|
| [第1章](docs/chapters/01-basics.md) | 簿記の基本と仕訳 | 初版 |
| [第2章](docs/chapters/02-merchandise.md) | 商品売買 | 初版 |
| [第3章](docs/chapters/03-cash-deposits.md) | 現金・預金 | 初版 |
| [第4章](docs/chapters/04-receivables-payables.md) | 売掛金・買掛金と電子記録債権・債務 | 初版 |
| [第5章](docs/chapters/05-other-receivables-payables.md) | その他の債権・債務 | 初版 |
| [第6章](docs/chapters/06-fixed-assets.md) | 有形固定資産 | 初版 |
| [第7章](docs/chapters/07-equity.md) | 株式会社の純資産 | 初版 |
| [第8章](docs/chapters/08-taxes.md) | 税金 | 初版 |
| [第9章](docs/chapters/09-accruals-corrections.md) | 収益・費用と訂正仕訳 | 初版 |
| [第10章](docs/chapters/10-books-slips.md) | 帳簿と伝票 | 初版 |
| [第11章](docs/chapters/11-trial-balance.md) | 試算表 | 初版 |
| [第12章](docs/chapters/12-adjustments.md) | 決算整理 | 初版 |
| [第13章](docs/chapters/13-worksheet-statements.md) | 精算表と財務諸表 | 初版 |
| [第14章](docs/chapters/14-mock-exam.md) | 総合問題(模擬試験 5回分) | 初版 |

精算表・財務諸表・商品有高帳などの問題には、印刷して使える[答案用紙](docs/sheets/index.md)があります。

章立ての詳しい方針は [docs/syllabus.md](docs/syllabus.md) にあります。

## サイトとして読む

`docs/` の中身は [MkDocs](https://www.mkdocs.org/) でWebサイトにでき、GitHub Pages(<https://kim-parkchik.github.io/nissho-boki3/>)で公開されます。
手元で確認する場合:

```bash
pip install -r requirements.txt
mkdocs serve
```

## 仕訳の検算

解答の仕訳が貸借一致しているかを、スクリプトで確認できます。

```bash
python tools/check_entries.py docs/chapters/*.md
```

## 協力のお願い

誤字・計算ミス・わかりにくい説明の報告を歓迎します。詳しくは [CONTRIBUTING.md](CONTRIBUTING.md) を見てください。

## ライセンス

本文・問題・解説は [クリエイティブ・コモンズ 表示 - 継承 4.0 国際 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) で公開しています。
`tools/` 内のプログラムは MIT License です。詳しくは [LICENSE.md](LICENSE.md) を見てください。

本教材は日本商工会議所とは関係のない、有志による非公式の教材です。
問題はすべてオリジナルで、過去の検定試験問題や市販教材からの転載はしていません。
