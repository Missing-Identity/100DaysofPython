<html>
<head>
<title>food.py</title>
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
food.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>
<span class="s0">import </span><span class="s1">random</span>


<span class="s0">class </span><span class="s1">Food(Turtle):</span>
    <span class="s0">def </span><span class="s1">__init__(self):</span>
        <span class="s1">super().__init__()</span>
        <span class="s1">self.shape(</span><span class="s2">&quot;circle&quot;</span><span class="s1">)</span>
        <span class="s1">self.penup()</span>
        <span class="s1">self.shapesize(stretch_len=</span><span class="s3">0.5</span><span class="s0">, </span><span class="s1">stretch_wid=</span><span class="s3">0.5</span><span class="s1">)</span>
        <span class="s1">self.color(</span><span class="s2">&quot;yellow&quot;</span><span class="s1">)</span>
        <span class="s1">self.speed(</span><span class="s2">&quot;fastest&quot;</span><span class="s1">)</span>
        <span class="s1">self.respawn()</span>

    <span class="s0">def </span><span class="s1">respawn(self):</span>
        <span class="s1">x = random.randint(-</span><span class="s3">260</span><span class="s0">, </span><span class="s3">260</span><span class="s1">)</span>
        <span class="s1">y = random.randint(-</span><span class="s3">260</span><span class="s0">, </span><span class="s3">260</span><span class="s1">)</span>
        <span class="s1">self.goto(x</span><span class="s0">, </span><span class="s1">y)</span>
</pre>
</body>
</html>