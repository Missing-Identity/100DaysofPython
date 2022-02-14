<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">pandas</span>

<span class="s1">nato_alphabet_list = pandas.read_csv(</span><span class="s2">&quot;nato_phonetic_alphabet.csv&quot;</span><span class="s1">)</span>
<span class="s1">nato_alphabet_dataFrame = pandas.DataFrame(nato_alphabet_list)</span>
<span class="s1">nato_alphabet_dict = {row.letter: row.code </span><span class="s0">for </span><span class="s1">(index</span><span class="s0">, </span><span class="s1">row) </span><span class="s0">in </span><span class="s1">nato_alphabet_dataFrame.iterrows()}</span>

<span class="s1">word = input(</span><span class="s2">&quot;Enter a word you want to convert into NATO:</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">)</span>
<span class="s1">word_letters = [letter </span><span class="s0">for </span><span class="s1">letter </span><span class="s0">in </span><span class="s1">word.upper()]</span>

<span class="s1">nato_code = [nato_alphabet_dict[</span><span class="s2">f&quot;</span><span class="s0">{</span><span class="s1">letter</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s1">] </span><span class="s0">for </span><span class="s1">letter </span><span class="s0">in </span><span class="s1">word_letters]</span>
<span class="s1">print(nato_code)</span>
</pre>
</body>
</html>