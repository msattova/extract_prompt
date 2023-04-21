from pathlib import Path
import os

def is_PNG(img_path: Path) -> bool:
    '''
    先頭8バイトのシグネチャからPNG画像かどうかを判定
    '''
    with img_path.open(mode="rb") as fp:
        signature=fp.read(8)
    if signature == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        return True
    else:
        return False


def show_binary(filepath: Path):
    '''
    img_path: バイナリデータを閲覧したいファイルのパス。
    '''
    with filepath.open(mode="rb") as fp:
        print(fp.read(8))
        while True:
            datalen = fp.read(4)
            chunkname = fp.read(4)
            data = fp.read(int.from_bytes(datalen, 'big'))
            crc = fp.read(4)
            print(datalen)
            print(chunkname)
            print(data)
            print(crc)
            if chunkname == b'IEND':
                return None


def convert_charactor(data):
    '''
    複数のutf-8コードからなる文字を似た形の単一のutf-8からなる文字に変換
    (対症療法なのでいつか根本的解決ができるようなコードにするべき)
    '''
    return data.replace(b'\xe2\x80\x94', b'\x2d')



def get_param(img_path: Path, splited=True):
    '''
    img_path: パラメーターを取得したい画像のパス。
    splited: Trueなら戻り値を\nで分割したlist[str]にする。
             Falseなら分割せずにstrにする。
    '''
    with img_path.open(mode="rb") as fp:
        fp.seek(8, os.SEEK_SET)
        while True:
            datalen = fp.read(4)
            chunkname = fp.read(4)
            data = fp.read(int.from_bytes(datalen, 'big'))
            fp.seek(4, os.SEEK_CUR) # crc
            if chunkname == b"tEXt" or chunkname == b"iTXt":
                print('data', data)
                break
            if chunkname == b'IEND':
                return None
    data = convert_charactor(data) # emダッシュをハイフンに変換
    result = ''.join([chr(i) for i in data.split(b'\x00')[-1] if i!=0])
    print('result', result)
    if splited:
        return result.split('\n')
    else:
        return result
