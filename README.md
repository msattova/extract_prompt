# extract_prompt

Stable Diffusionで作成したPNG画像のバイナリデータを読んで、その画像作成に用いられたプロンプトやパラメータ等の情報を抜き出すプログラムです。

要するにStable Diffusion web UI(AUTOMATIC1111)のPNG Infoみたいなことができます。

実行方法:

```
python3 main.py image.png
```

もしくは

```
python3 main.py images_directory
```

ディレクトリを指定すると、そのディレクトリ内にあるPNG画像すべてに対して処理を実行します。

また、抽出した情報は抽出元の画像ファイルと同名のMarkdownファイルとして出力されます。
