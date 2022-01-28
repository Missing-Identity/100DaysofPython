<html>
<head>
<title>main.py</title>
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
main.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span><span class="s0">, </span><span class="s1">Screen</span>

<span class="s1">tim = Turtle()</span>
<span class="s1">screen = Screen()</span>

<span class="s1">tim.speed(</span><span class="s2">&quot;fastest&quot;</span><span class="s1">)</span>


<span class="s0">def </span><span class="s1">forwards():</span>
    <span class="s1">tim.forward(</span><span class="s3">5</span><span class="s1">)</span>


<span class="s0">def </span><span class="s1">backwards():</span>
    <span class="s1">tim.back(</span><span class="s3">5</span><span class="s1">)</span>


<span class="s0">def </span><span class="s1">left_turn():</span>
    <span class="s1">new_heading = tim.heading()+</span><span class="s3">10</span>
    <span class="s1">tim.setheading(new_heading)</span>


<span class="s0">def </span><span class="s1">right_turn():</span>
    <span class="s1">new_heading = tim.heading()-</span><span class="s3">10</span>
    <span class="s1">tim.setheading(new_heading)</span>


<span class="s0">def </span><span class="s1">clear():</span>
    <span class="s1">tim.clear()</span>
    <span class="s1">tim.reset()</span>


<span class="s1">screen.listen()</span>
<span class="s1">screen.onkey(forwards</span><span class="s0">, </span><span class="s2">&quot;w&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(backwards</span><span class="s0">, </span><span class="s2">&quot;s&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(left_turn</span><span class="s0">, </span><span class="s2">&quot;a&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(right_turn</span><span class="s0">, </span><span class="s2">&quot;d&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(clear</span><span class="s0">, </span><span class="s2">&quot;c&quot;</span><span class="s1">)</span>
<span class="s1">screen.exitonclick()</span>
</pre>
</body>
</html>