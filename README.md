## 手順 

* pipenv installで依存関係をインストール
* trend_repo_files_spider.pyにあるURLを修正して言語ごとに分ける
* `sh start.sh` でscrapyを実行
* 出力されてくるoutput.csvを任意の名前に変更
* create_picture.pyにあるLANGを上記ファイル名と同じ名前にする
* create_picture.pyを実行する

Github Trendから学ぶ開発ツール

## 概要

* GitHubのトレンドに上がってくるリポジトリは開発が熱い
* リポジトリのルートディレクトリには開発を楽にするツールの設定ファイルが置かれがちだ
* トレンドに上がっているリポジトリのルートディレクトリのファイル名を集計すれば開発ツールが見えてくるはず

## 方法

* scrapyで[トレンド](https://github.com/trending)のリポジトリのタイトルを集める
    * 言語でフィルタを掛けて月間のトレンドを見る
* 集計して棒グラフとして出力
    * カウントが2以上の単語のみグラフに表示する

## 結果