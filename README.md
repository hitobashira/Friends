# Friends :: Easy Find Tool with Perl Regular Expressions.

Friends v.x.x.x-2017-03-24 with Perl RE ::

alternative find , easy to find files with perl regular expression.
easy exclude dir/path. no prune.

Friends who are good at finding out and doing something. (Provisional)
探しだして何かするのが得意なフレンズ(仮)

Friends Usage::

GNU find = Full match<br>
friends  = Partial match

friends "PCRE"<br>
friends "PCRE" -E(-exclude) "PCRE exclude exp."

  -E,-exclude exclude_arguments<br>
  -I,-include include_arguments<br>


  friends "*png"        | xargs mpv       {}
  
  friends "png|jpg"     | xargs mpv       {}
  
  friends '.*pcre.mkv\z' | xargs -i  mpv   {}
  
  friends '.*pcre.py$'   | xargs -n1 head  {}
 

 friends ".*Dream.*flac" -exclude "SOUND|Sound|Comes|HITS|♡|Various|./.*?/.*?/(羽|Emerge)" 
 
 friends '.*pcre.mkv\z|.*pcre.png\z|.*pcre.ogg\z' | xargs -i  mpv {} 
 
 friends "PCRE for Files" -E "PCRE for Path"
<br>
 friends "PCRE for Files" -I "PCRE for Path"

-E -exclude<br>
-I -include<br>

./aaa/zzz/ccc/aaa.flac<br>
./aaa/bbb/ccc/aaa.flac

tree .<br>
├── 1.sh<br>
├── aaa<br>
│   ├── bbb<br>
│   │   └── ccc<br>
│   │       └── aaa.flac<br>
│   └── zzz<br>
│       └── ccc<br>
│           └── aaa.flac<br>
├── data<br>

$ friends "aaa.flac" -E "./.*?/bbb/"

"./aaa/zzz/ccc/aaa.flac" <---only (2)

$ friends "aaa.flac" -E "./.*?/zzz/"

"./aaa/bbb/ccc/aaa.flac" <---only (1)

$ friends "aaa.flac" -I "./.*?/zzz/"

"./aaa/zzz/ccc/aaa.flac"  <---only (2)

locale ja_JP.UTF-8<br>
mulitibytes language support (japanese and maybe chinese )

フレンズ=Friends。http://www.crunchyroll.com/kemono-friends
