<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #808080;}
.s3 { color: #6897bb;}
.s4 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span><span class="s0">, </span><span class="s1">Screen</span>
<span class="s0">from </span><span class="s1">random </span><span class="s0">import </span><span class="s1">randint</span>

<span class="s2"># Initial setup</span>
<span class="s1">race_on = </span><span class="s0">False</span>
<span class="s1">condition = </span><span class="s0">False</span>
<span class="s1">screen = Screen()</span>
<span class="s1">screen.setup(width=</span><span class="s3">500</span><span class="s0">, </span><span class="s1">height=</span><span class="s3">400</span><span class="s1">)</span>
<span class="s1">colours = [</span><span class="s4">&quot;red&quot;</span><span class="s0">, </span><span class="s4">&quot;orange&quot;</span><span class="s0">, </span><span class="s4">&quot;green&quot;</span><span class="s0">, </span><span class="s4">&quot;blue&quot;</span><span class="s0">, </span><span class="s4">&quot;black&quot;</span><span class="s0">, </span><span class="s4">&quot;brown&quot;</span><span class="s1">]</span>
<span class="s1">turtles = {</span><span class="s3">0</span><span class="s1">: []</span><span class="s0">, </span><span class="s3">1</span><span class="s1">: []</span><span class="s0">, </span><span class="s3">2</span><span class="s1">: []</span><span class="s0">, </span><span class="s3">3</span><span class="s1">: []</span><span class="s0">, </span><span class="s3">4</span><span class="s1">: []</span><span class="s0">, </span><span class="s3">5</span><span class="s1">: []}</span>
<span class="s1">winner = </span><span class="s4">&quot;&quot;</span>
<span class="s1">bet = </span><span class="s4">&quot;&quot;</span>
<span class="s1">x = -</span><span class="s3">230</span>
<span class="s1">y = -</span><span class="s3">150</span>


<span class="s0">def </span><span class="s1">random_number():</span>
    <span class="s0">return </span><span class="s1">randint(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">10</span><span class="s1">)</span>


<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">6</span><span class="s1">):</span>
    <span class="s1">turtles[i] = Turtle(shape=</span><span class="s4">&quot;turtle&quot;</span><span class="s1">)</span>
    <span class="s1">turtles[i].penup()</span>
    <span class="s1">turtles[i].color(colours[i])</span>
    <span class="s1">turtles[i].goto(x=x</span><span class="s0">, </span><span class="s1">y=y)</span>
    <span class="s1">y += </span><span class="s3">60</span>

<span class="s0">while not </span><span class="s1">condition:</span>
    <span class="s1">bet = screen.textinput(title=</span><span class="s4">&quot;Make your bet&quot;</span><span class="s0">, </span><span class="s1">prompt=</span><span class="s4">&quot;Which turtle will win the race? Enter a colour: &quot;</span><span class="s1">)</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">colours:</span>
        <span class="s0">if </span><span class="s1">i == bet:</span>
            <span class="s1">condition = </span><span class="s0">True</span>
    <span class="s0">if </span><span class="s1">condition:</span>
        <span class="s1">race_on = </span><span class="s0">True</span>

<span class="s0">while </span><span class="s1">race_on:</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">6</span><span class="s1">):</span>
        <span class="s1">turtles[i].forward(random_number())</span>
        <span class="s0">if </span><span class="s1">turtles[i].position()[</span><span class="s3">0</span><span class="s1">] &gt;= </span><span class="s3">230</span><span class="s1">:</span>
            <span class="s1">race_on = </span><span class="s0">False</span>
            <span class="s1">print(</span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">str(turtles[i].color()[</span><span class="s3">0</span><span class="s1">]).title()</span><span class="s0">} </span><span class="s4">won!&quot;</span><span class="s1">)</span>
            <span class="s1">winner = turtles[i].color()[</span><span class="s3">0</span><span class="s1">]</span>
            <span class="s0">break</span>

<span class="s0">if </span><span class="s1">str(winner) == bet:</span>
    <span class="s1">print(</span><span class="s4">&quot;Your bet won!&quot;</span><span class="s1">)</span>
<span class="s0">else</span><span class="s1">:</span>
    <span class="s1">print(</span><span class="s4">&quot;Oops! Looks like you lost!&quot;</span><span class="s1">)</span>

<span class="s1">screen.exitonclick()</span>
</pre>
</body>
</html>