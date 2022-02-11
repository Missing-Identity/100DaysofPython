<html>
<head>
<title>snake.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #808080;}
.s4 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
snake.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>

<span class="s1">move_distance = </span><span class="s2">20</span>
<span class="s1">starting_positions = [(</span><span class="s2">0</span><span class="s0">, </span><span class="s2">0</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(-</span><span class="s2">20</span><span class="s0">, </span><span class="s2">0</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(-</span><span class="s2">40</span><span class="s0">, </span><span class="s2">0</span><span class="s1">)]</span>
<span class="s1">up = </span><span class="s2">90</span>
<span class="s1">left = </span><span class="s2">180</span>
<span class="s1">right = </span><span class="s2">0</span>
<span class="s1">down = </span><span class="s2">270</span>


<span class="s0">class </span><span class="s1">Snake:</span>
    <span class="s0">def </span><span class="s1">__init__(self):</span>
        <span class="s1">self.snake_segments = []</span>
        <span class="s1">self.initial_snake()</span>
        <span class="s1">self.head = self.snake_segments[</span><span class="s2">0</span><span class="s1">]</span>

    <span class="s0">def </span><span class="s1">initial_snake(self):</span>
        <span class="s0">for </span><span class="s1">position </span><span class="s0">in </span><span class="s1">starting_positions:</span>
            <span class="s1">self.add_segment(position)</span>

    <span class="s0">def </span><span class="s1">move(self):</span>
        <span class="s0">for </span><span class="s1">seg </span><span class="s0">in </span><span class="s1">range((len(self.snake_segments) - </span><span class="s2">1</span><span class="s1">)</span><span class="s0">, </span><span class="s2">0</span><span class="s0">, </span><span class="s1">-</span><span class="s2">1</span><span class="s1">):</span>
            <span class="s1">new_x = self.snake_segments[seg - </span><span class="s2">1</span><span class="s1">].xcor()</span>
            <span class="s1">new_y = self.snake_segments[seg - </span><span class="s2">1</span><span class="s1">].ycor()</span>
            <span class="s1">self.snake_segments[seg].goto(new_x</span><span class="s0">, </span><span class="s1">new_y)</span>
        <span class="s1">self.head.forward(move_distance)</span>

    <span class="s0">def </span><span class="s1">snake_extend(self):</span>
        <span class="s1">self.add_segment(self.snake_segments[-</span><span class="s2">1</span><span class="s1">].position())  </span><span class="s3"># Negative number means starting from the end of list.</span>
        <span class="s3"># Here we are adding to the last position</span>

    <span class="s0">def </span><span class="s1">add_segment(self</span><span class="s0">, </span><span class="s1">position):</span>
        <span class="s1">tim = Turtle(</span><span class="s4">&quot;square&quot;</span><span class="s1">)</span>
        <span class="s1">tim.color(</span><span class="s4">&quot;white&quot;</span><span class="s1">)</span>
        <span class="s1">tim.penup()</span>
        <span class="s1">tim.goto(position)</span>
        <span class="s1">self.snake_segments.append(tim)</span>

    <span class="s0">def </span><span class="s1">reset(self):</span>
        <span class="s0">for </span><span class="s1">seg </span><span class="s0">in </span><span class="s1">self.snake_segments:</span>
            <span class="s1">seg.goto(</span><span class="s2">1000</span><span class="s0">, </span><span class="s2">1000</span><span class="s1">)</span>
        <span class="s1">self.snake_segments.clear()</span>
        <span class="s1">self.initial_snake()</span>
        <span class="s1">self.head = self.snake_segments[</span><span class="s2">0</span><span class="s1">]</span>

    <span class="s0">def </span><span class="s1">up(self):</span>
        <span class="s0">if </span><span class="s1">self.head.heading() != down:</span>
            <span class="s1">self.head.setheading(up)</span>

    <span class="s0">def </span><span class="s1">down(self):</span>
        <span class="s0">if </span><span class="s1">self.head.heading() != up:</span>
            <span class="s1">self.head.setheading(down)</span>

    <span class="s0">def </span><span class="s1">left(self):</span>
        <span class="s0">if </span><span class="s1">self.head.heading() != right:</span>
            <span class="s1">self.head.setheading(left)</span>

    <span class="s0">def </span><span class="s1">right(self):</span>
        <span class="s0">if </span><span class="s1">self.head.heading() != left:</span>
            <span class="s1">self.head.setheading(right)</span>
</pre>
</body>
</html>