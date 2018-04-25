# GBP-StoryCatalog
「バンドリ！ガールズバンドパーティ！」のストーリーのスクリーンショット画像から会話内容を文字列化し、画像を検索出来るプログラム

## 使い方
### インストール
事前にTesseract-OCRをインストールしておいてください。
```sh
git clone https://github.com/chunjb37/gbp-storycatalog.git
cd gbp-storycatalog
pip install -r requirements.txt
```
### 実行
imagesディレクトリにスクリーンショット画像を入れて
```
python img2data.py
```
data.jsonが作成されます。
```
python main.py
```
で動きます
