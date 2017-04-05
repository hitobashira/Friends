#!/usr/bin/env python3
#@ 大文字小文字区別。部分一致、ファイルのみ対象検索。with QW

import os
import sys
import argparse
import re

parser = argparse.ArgumentParser( description='正規表現ファイル検索 by Python RE' )

parser.add_argument( "RERE" ,help='\"正規表現をQW付きで入力\" need quote') # 引数追加
parser.add_argument( 'ignore', help='re.IGNORECASE, type any chars.' ,nargs="*")
# parser.add_argument( 'ignore', choices=['ignore', '-ignore', '-I', '-IG',  'IG'],
#                         help='insensible case' , nargs="*") # オプション追加 拡張用
parser.add_argument( '--version', action='version', version='%(prog)s 0.0.3') # version


args = parser.parse_args() # 引数を解釈Namespace(RERE='RERE', ignore=None)
# print(args)


素通し正規表現   =              args.RERE  #= sys.argv[1] #大小文字区別あり
素通し正規表現IG =  re.compile( args.RERE , re.IGNORECASE) # 大小文字区別なし re.Iでも可

f = open( sys.argv[0] + "_results_.txt" ,"w")

def 正規表現でファイル検索 (): #部分マッチ型があれば先頭マッチ型は不要\A|^
    for dirpath, dirs, files in os.walk('.'):
        for 尋ね人 in files:
            if re.search( 素通し正規表現 , 尋ね人 ):#部分マッチ型
                print("\""+os.path.join(dirpath, 尋ね人)+"\"")
                f.write("\""+os.path.join(dirpath, 尋ね人)+"\"\n")

def 正規表現でファイル検索ケース無視 (): #部分マッチ型があれば先頭マッチ型は不要\A|^
    for dirpath, dirs, files in os.walk('.'):
        for 尋ね人 in files:
            if re.search( 素通し正規表現IG , 尋ね人 ):#部分マッチ型
                print("\""+os.path.join(dirpath, 尋ね人)+"\"")
                f.write("\""+os.path.join(dirpath, 尋ね人)+"\"\n")


def 何もしない ():
    print("何もしないは嘘だが、不要なブロック")
    print(args)
    #print(args.RERE)

def Print_Write_File ():
    print("\""+os.path.join(dirpath, 尋ね人)+"\"")
    f.write("\""+os.path.join(dirpath, 尋ね人)+"\"\n")


"""
ここから具体処理の分岐
"""

if args.ignore : #とにかくなんか文字があれば無視モードになる。
    print("re.IGNORECASE turned on")
    正規表現でファイル検索ケース無視 ()
elif args.RERE :
    正規表現でファイル検索 ()
else:
    何もしない () #何もしない (嘘)



sys.exit()
exit()
exit()
exit()
