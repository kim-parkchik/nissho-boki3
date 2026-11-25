#!/usr/bin/env python3
"""仕訳表の貸借一致を確認するスクリプト。

Markdown 内の「| 借方科目 | 金額 | 貸方科目 | 金額 |」で始まる表を探し、
借方金額の合計と貸方金額の合計が一致しているかを確認します。
先頭に「番号」の列がある表(| 番号 | 借方 | 金額 | 貸方 | 金額 |)は、
番号の欄が書かれている行から次の番号の行の前までを、1つの仕訳として確認します。

使い方:
    python tools/check_entries.py docs/chapters/*.md

不一致があれば終了コード 1 を返します(GitHub Actions でも使えます)。
"""
import re
import sys
from pathlib import Path

HEADER = re.compile(r"^\|\s*借方科目\s*\|\s*金額\s*\|\s*貸方科目\s*\|\s*金額\s*\|\s*$")
NUMBERED_HEADER = re.compile(
    r"^\|\s*番号\s*\|\s*借方(?:科目)?\s*\|\s*金額\s*\|\s*貸方(?:科目)?\s*\|\s*金額\s*\|\s*$"
)
SEPARATOR = re.compile(r"^\|[\s:\-|]+\|\s*$")
HEADING = re.compile(r"^#{1,6}\s+(.*)$")


def parse_amount(text: str, path: Path, lineno: int) -> int:
    text = text.strip().replace(",", "").replace("円", "")
    if text == "":
        return 0
    if not re.fullmatch(r"\d+", text):
        raise ValueError(f"{path}:{lineno}: 金額を読み取れません: {text!r}")
    return int(text)


def check_file(path: Path) -> tuple[int, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    count = 0
    heading = "(見出しなし)"
    i = 0
    while i < len(lines):
        m = HEADING.match(lines[i])
        if m:
            heading = m.group(1).strip()
        if HEADER.match(lines[i]):
            start = i + 1
            i += 1
            if i < len(lines) and SEPARATOR.match(lines[i]):
                i += 1
            debit = credit = 0
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if len(cells) != 4:
                    errors.append(f"{path}:{i + 1}: 列の数が4ではありません")
                else:
                    try:
                        debit += parse_amount(cells[1], path, i + 1)
                        credit += parse_amount(cells[3], path, i + 1)
                    except ValueError as e:
                        errors.append(str(e))
                i += 1
            count += 1
            if debit != credit:
                errors.append(
                    f"{path}:{start}: [{heading}] 貸借不一致 借方 {debit:,} / 貸方 {credit:,}"
                )
            if debit == 0 and credit == 0:
                errors.append(f"{path}:{start}: [{heading}] 金額が入っていません")
            continue
        if NUMBERED_HEADER.match(lines[i]):
            i += 1
            if i < len(lines) and SEPARATOR.match(lines[i]):
                i += 1
            entries: list[list[int]] = []  # [開始行, 借方, 貸方, 番号]
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if len(cells) != 5:
                    errors.append(f"{path}:{i + 1}: 列の数が5ではありません")
                else:
                    if cells[0] or not entries:
                        entries.append([i + 1, 0, 0, cells[0]])
                    try:
                        entries[-1][1] += parse_amount(cells[2], path, i + 1)
                        entries[-1][2] += parse_amount(cells[4], path, i + 1)
                    except ValueError as e:
                        errors.append(str(e))
                i += 1
            for start, debit, credit, no in entries:
                count += 1
                if debit != credit:
                    errors.append(
                        f"{path}:{start}: [{heading} {no}] 貸借不一致 借方 {debit:,} / 貸方 {credit:,}"
                    )
            continue
        i += 1
    return count, errors


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    total = 0
    all_errors: list[str] = []
    for arg in argv:
        n, errs = check_file(Path(arg))
        total += n
        all_errors.extend(errs)
    for e in all_errors:
        print("NG", e)
    print(f"仕訳 {total} 件を確認しました。不一致 {len(all_errors)} 件。")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
