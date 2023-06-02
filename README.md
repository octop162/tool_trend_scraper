## 手順 

* pipenv installで依存関係をインストール
* trend_repo_files_spider.pyにあるURLを修正して言語ごとに分ける
* `sh start.sh` でscrapyを実行
* 出力されてくるoutput.csvを任意の名前に変更
* create_picture.pyにあるLANGを上記ファイル名と同じ名前にする
* create_picture.pyを実行する