# Friends :: Easy Find Tool with Perl Regular Expressions.

now, Testing use only.

Friends v.x.x.x-2017-03-24 with Perl RE ::

alternative find , easy to find files with perl regular expression.
easy exlude dir/path. no prune.

  friends "*png"        | xargs mpv       {}
  friends "png|jpg"     | xargs mpv       {}
  friends '.*pcre.mkv\z' | xargs -i  mpv   {}
  friends '.*pcre.py$'   | xargs -n1 head  {}
 

 friends ".*Dream.*flac" -exclude "SOUND|Sound|Comes|HITS|♡|Various|./.*?/.*?/(羽|Emerge)" 
 friends '.*pcre.mkv\z|.*pcre.png\z|.*pcre.ogg\z' | xargs -i  mpv {} 
 
 
