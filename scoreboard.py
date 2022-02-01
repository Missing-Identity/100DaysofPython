<html>
<head>
<title>scoreboard.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
scoreboard.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>
<span class="s1">alignment = </span><span class="s2">&quot;center&quot;</span>
<span class="s1">font = (</span><span class="s2">&quot;Avenir&quot;</span><span class="s0">, </span><span class="s3">30</span><span class="s0">, </span><span class="s2">&quot;normal&quot;</span><span class="s1">)</span>


<span class="s0">class </span><span class="s1">Score(Turtle):</span>
    <span class="s0">def </span><span class="s1">__init__(self):</span>
        <span class="s1">super().__init__()</span>
        <span class="s1">self.score = </span><span class="s3">0</span>
        <span class="s1">self.clear()</span>
        <span class="s1">self.penup()</span>
        <span class="s1">self.ht()</span>
        <span class="s1">self.color(</span><span class="s2">&quot;white&quot;</span><span class="s1">)</span>
        <span class="s1">self.setposition(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">260</span><span class="s1">)</span>
        <span class="s1">self.write(</span><span class="s2">f&quot;Score: </span><span class="s0">{</span><span class="s1">self.score</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s0">, True, </span><span class="s1">align=alignment</span><span class="s0">, </span><span class="s1">font=font)</span>

    <span class="s0">def </span><span class="s1">increase_score(self):</span>
        <span class="s1">self.score += </span><span class="s3">1</span>
        <span class="s1">self.clear()</span>
        <span class="s1">self.setposition(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">260</span><span class="s1">)</span>
        <span class="s1">self.write(</span><span class="s2">f&quot;Score: </span><span class="s0">{</span><span class="s1">self.score</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s0">, True, </span><span class="s1">align=alignment</span><span class="s0">, </span><span class="s1">font=font)</span>

    <span class="s0">def </span><span class="s1">game_over(self):</span>
        <span class="s1">self.setposition(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">0</span><span class="s1">)</span>
        <span class="s1">self.color(</span><span class="s2">&quot;red&quot;</span><span class="s1">)</span>
        <span class="s1">self.write(</span><span class="s2">&quot;GAME OVER&quot;</span><span class="s0">, True, </span><span class="s1">align=alignment</span><span class="s0">, </span><span class="s1">font=font)</span>
</pre>
</body>
</html>