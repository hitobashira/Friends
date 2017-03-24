# Friends :: Easy Find Tool with Perl Regular Expressions.

now, Testing use only.

Friends v.x.x.x-2017-03-24 with Perl RE ::

alternative find , easy to find files with perl regular expression.
easy exclude dir/path. no prune.

探しだして何かするのが得意なフレンズ(仮)

Friends Usage::

friends "PCRE" -E(-exclude) "ディレクトリ除外指定"
-E,-exclude exclude_arguments

-I,-include include_arguments

  friends "*png"        | xargs mpv       {}
  
  friends "png|jpg"     | xargs mpv       {}
  
  friends '.*pcre.mkv\z' | xargs -i  mpv   {}
  
  friends '.*pcre.py$'   | xargs -n1 head  {}
 

 friends ".*Dream.*flac" -exclude "SOUND|Sound|Comes|HITS|♡|Various|./.*?/.*?/(羽|Emerge)" 
 
 friends '.*pcre.mkv\z|.*pcre.png\z|.*pcre.ogg\z' | xargs -i  mpv {} 
 
 friends "PCRE for Files" -E "PCRE for Path"

 friends "PCRE for Files" -I "PCRE for Path"

-E -exclude
-I -include

./aaa/zzz/ccc/aaa.flac
./aaa/bbb/ccc/aaa.flac

tree ./aaa
./aaa<br>
├── bbb<br>
│   └── ccc<br>
│       └── aaa.flac (1)<br>
└── zzz<br>
    └── ccc<br>
        └── aaa.flac (2)<br>

$ friends "aaa.flac" -E "./.*?/bbb/"

"./aaa/zzz/ccc/aaa.flac" <---only (2)

$ friends "aaa.flac" -E "./.*?/zzz/"

"./aaa/bbb/ccc/aaa.flac" <---only (1)

$ friends "aaa.flac" -I "./.*?/zzz/"

"./aaa/zzz/ccc/aaa.flac"  <---only (2)

locale ja_JP.UTF-8
mulitibytes language support (japanese and maybe chinese )
