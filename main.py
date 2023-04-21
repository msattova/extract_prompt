import argparse
from pathlib import Path

from img2param import get_param, is_PNG, show_binary


def out_md(img_path: Path, param: list[str]):
    negativeprompt = ' '.join(param[1].split(' ')[2:])
    params = '\n'.join([f"* {i}" for i in param[2].split(', ')])
    writein = f"""
# {img_path.name}

**prompt**
```
{param[0]}
```

**negative prompt**
```
{negativeprompt}
```

**paramaters**
{params}
"""
    output_path = img_path.parent / Path(f"{img_path.stem}.md")
    with output_path.open(mode='w', encoding='utf-8') as f:
        f.write(writein)

if __name__=='__main__':
    parser = argparse.ArgumentParser(prog='img2param',
                                     description='Stable Diffusionで生成した画像からプロンプトなどの情報を抜き出す')
    parser.add_argument('imgpaths',
                        nargs='+',
                        action='store',
                        type=Path)
    args = parser.parse_args()
    paths = args.imgpaths
    for p in paths:
        if Path.is_dir(p):
            tmp = {i: get_param(i)
                       for i in p.glob('**/*.png')
                       if is_PNG(i)}
            results = {i: j for i, j in tmp.items() if j is not None}
            for k, v in results.items():
                out_md(k, v)
        elif Path.is_file(p):
            if not is_PNG(p):
                continue
            result = get_param(p)
            print(result)
            if result is None:
                continue
            out_md(p, result)
        else: # ファイルでもディレクトリでもない場合はスキップ
            continue


