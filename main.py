<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #808080;}
.s1 { color: #a9b7c6;}
.s2 { color: #cc7832;}
.s3 { color: #6a8759;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0"># Importing libraries</span>
<span class="s2">import </span><span class="s1">pandas</span>
<span class="s2">import </span><span class="s1">turtle</span>
<span class="s2">from </span><span class="s1">turtle </span><span class="s2">import </span><span class="s1">Turtle</span>

<span class="s0"># Screen Setup</span>
<span class="s1">screen = turtle.Screen()</span>
<span class="s1">screen.title(</span><span class="s3">&quot;US States Game&quot;</span><span class="s1">)</span>
<span class="s1">image = </span><span class="s3">&quot;blank_states_img.gif&quot;</span>
<span class="s1">screen.addshape(image)  </span><span class="s0"># Adding custom shape to turtle</span>
<span class="s1">turtle.shape(image)</span>

<span class="s0"># Game setup</span>
<span class="s1">game_is_on = </span><span class="s2">True</span>
<span class="s1">state_data = pandas.read_csv(</span><span class="s3">&quot;50_states.csv&quot;</span><span class="s1">)</span>
<span class="s1">state_name = []</span>
<span class="s1">missed_states = []</span>
<span class="s1">name = Turtle()</span>
<span class="s1">name.ht()</span>
<span class="s1">score = </span><span class="s4">0</span>


<span class="s2">while </span><span class="s1">game_is_on:</span>
    <span class="s1">answer = screen.textinput(title=</span><span class="s3">f&quot;</span><span class="s2">{</span><span class="s1">score</span><span class="s2">}</span><span class="s3">/50 States Correct&quot;</span><span class="s2">, </span><span class="s1">prompt=</span><span class="s3">&quot;What's another state's name?&quot;</span><span class="s1">)</span>
    <span class="s2">if </span><span class="s1">answer.title() == </span><span class="s3">&quot;Exit&quot;</span><span class="s1">:</span>
        <span class="s2">break</span>
    <span class="s2">for </span><span class="s1">i </span><span class="s2">in </span><span class="s1">range(</span><span class="s4">0</span><span class="s2">, </span><span class="s1">len(state_data)):</span>
        <span class="s2">if </span><span class="s1">len(state_name) == len(state_data):</span>
            <span class="s1">game_is_on = </span><span class="s2">False</span>
            <span class="s1">print(</span><span class="s3">&quot;You win! Congratulations!&quot;</span><span class="s1">)</span>
            <span class="s2">break</span>
        <span class="s2">if </span><span class="s1">answer.title() == state_data.state[i]:</span>
            <span class="s2">if </span><span class="s1">answer.title() </span><span class="s2">in </span><span class="s1">state_name:</span>
                <span class="s2">break</span>
            <span class="s1">name.penup()</span>
            <span class="s1">name.goto(state_data.x[i]</span><span class="s2">, </span><span class="s1">state_data.y[i])</span>
            <span class="s1">name.write(</span><span class="s3">f&quot;</span><span class="s2">{</span><span class="s1">state_data.state[i]</span><span class="s2">}</span><span class="s3">&quot;</span><span class="s2">, </span><span class="s1">move=</span><span class="s2">True</span><span class="s1">)</span>
            <span class="s1">state_name.append(answer.title())</span>
            <span class="s1">score += </span><span class="s4">1</span>

<span class="s0"># Missed states</span>
<span class="s2">for </span><span class="s1">i </span><span class="s2">in </span><span class="s1">range(len(state_data)):</span>
    <span class="s2">if </span><span class="s1">state_data.state[i] </span><span class="s2">in </span><span class="s1">state_name:</span>
        <span class="s2">pass</span>
    <span class="s2">else</span><span class="s1">:</span>
        <span class="s1">missed_states.append(state_data.state[i])</span>
        <span class="s1">missed_csv = pandas.DataFrame(missed_states)</span>
        <span class="s1">missed_csv.to_csv(</span><span class="s3">&quot;Missed_States.csv&quot;</span><span class="s1">)</span>


<span class="s1">turtle.mainloop()</span>
</pre>
</body>
</html>