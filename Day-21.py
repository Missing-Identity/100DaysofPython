<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #6a8759;}
.s4 { color: #808080;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">time</span>
<span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Screen</span>
<span class="s0">from </span><span class="s1">snake </span><span class="s0">import </span><span class="s1">Snake</span>
<span class="s0">from </span><span class="s1">food </span><span class="s0">import </span><span class="s1">Food</span>
<span class="s0">from </span><span class="s1">scoreboard </span><span class="s0">import </span><span class="s1">Score</span>

<span class="s1">screen = Screen()</span>
<span class="s1">screen.setup(width=</span><span class="s2">600</span><span class="s0">, </span><span class="s1">height=</span><span class="s2">600</span><span class="s1">)</span>
<span class="s1">screen.bgcolor(</span><span class="s3">&quot;black&quot;</span><span class="s1">)</span>
<span class="s1">screen.title(</span><span class="s3">&quot;Prime's Snake Game&quot;</span><span class="s1">)</span>
<span class="s1">screen.tracer(</span><span class="s2">0</span><span class="s1">)</span>

<span class="s1">naagin = Snake()</span>
<span class="s1">food = Food()</span>
<span class="s1">score = Score()</span>
<span class="s1">snake_length = len(naagin.snake_segments)</span>

<span class="s1">screen.listen()</span>
<span class="s1">screen.onkey(naagin.up</span><span class="s0">, </span><span class="s3">&quot;Up&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(naagin.down</span><span class="s0">, </span><span class="s3">&quot;Down&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(naagin.right</span><span class="s0">, </span><span class="s3">&quot;Right&quot;</span><span class="s1">)</span>
<span class="s1">screen.onkey(naagin.left</span><span class="s0">, </span><span class="s3">&quot;Left&quot;</span><span class="s1">)</span>

<span class="s1">game_is_on = </span><span class="s0">True</span>
<span class="s0">while </span><span class="s1">game_is_on:</span>
    <span class="s1">screen.update()</span>
    <span class="s1">time.sleep(</span><span class="s2">0.12</span><span class="s1">)</span>

    <span class="s4"># Snake Move Code</span>
    <span class="s1">naagin.move()</span>

    <span class="s4"># Detect Collision with Food</span>
    <span class="s0">if </span><span class="s1">naagin.head.distance(food) &lt;= </span><span class="s2">15</span><span class="s1">:</span>
        <span class="s1">score.clear()</span>
        <span class="s1">food.respawn()</span>
        <span class="s1">score.increase_score()</span>
        <span class="s1">naagin.snake_extend()</span>

    <span class="s4"># Wall Collision Detection</span>
    <span class="s0">if </span><span class="s1">naagin.head.xcor() &gt; </span><span class="s2">280 </span><span class="s0">or </span><span class="s1">naagin.head.xcor() &lt; -</span><span class="s2">280 </span><span class="s0">or </span><span class="s1">naagin.head.ycor() &gt; </span><span class="s2">280 </span><span class="s0">or </span><span class="s1">naagin.head.ycor() &lt; -</span><span class="s2">280</span><span class="s1">:</span>
        <span class="s1">score.game_over()</span>
        <span class="s1">game_is_on = </span><span class="s0">False</span>

    <span class="s4"># Tail Collision Detection</span>
    <span class="s0">for </span><span class="s1">segment </span><span class="s0">in </span><span class="s1">naagin.snake_segments[</span><span class="s2">1</span><span class="s1">::]:</span>
        <span class="s0">if </span><span class="s1">naagin.head.distance(segment) &lt; </span><span class="s2">10</span><span class="s1">:</span>
            <span class="s1">score.game_over()</span>
            <span class="s1">game_is_on = </span><span class="s0">False</span>

<span class="s1">screen.exitonclick()</span>
</pre>
</body>
</html>