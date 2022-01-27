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
<pre><span class="s0">import </span><span class="s1">turtle</span>
<span class="s0">from </span><span class="s1">random </span><span class="s0">import </span><span class="s1">randint</span>
<span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span><span class="s0">, </span><span class="s1">Screen</span>
<span class="s2"># Extracting colours from a picture</span>

<span class="s2"># import colorgram</span>

<span class="s2"># colors = colorgram.extract('hirst.jpeg', 30)</span>

<span class="s2"># for i in range(0, 30):</span>
<span class="s2">#     rgb = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)</span>
<span class="s2">#     color_list.append(rgb)</span>

<span class="s1">color_list = [(</span><span class="s3">188</span><span class="s0">, </span><span class="s3">18</span><span class="s0">, </span><span class="s3">44</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">243</span><span class="s0">, </span><span class="s3">231</span><span class="s0">, </span><span class="s3">66</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">210</span><span class="s0">, </span><span class="s3">236</span><span class="s0">, </span><span class="s3">242</span><span class="s1">)</span><span class="s0">,</span>
              <span class="s1">(</span><span class="s3">196</span><span class="s0">, </span><span class="s3">74</span><span class="s0">, </span><span class="s3">33</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">218</span><span class="s0">, </span><span class="s3">66</span><span class="s0">, </span><span class="s3">107</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">17</span><span class="s0">, </span><span class="s3">125</span><span class="s0">, </span><span class="s3">173</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">196</span><span class="s0">, </span><span class="s3">175</span><span class="s0">, </span><span class="s3">17</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">107</span><span class="s0">, </span><span class="s3">182</span><span class="s0">, </span><span class="s3">209</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">12</span><span class="s0">, </span><span class="s3">142</span><span class="s0">, </span><span class="s3">88</span><span class="s1">)</span><span class="s0">,</span>
              <span class="s1">(</span><span class="s3">12</span><span class="s0">, </span><span class="s3">167</span><span class="s0">, </span><span class="s3">214</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">241</span><span class="s0">, </span><span class="s3">231</span><span class="s0">, </span><span class="s3">2</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">210</span><span class="s0">, </span><span class="s3">152</span><span class="s0">, </span><span class="s3">94</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">186</span><span class="s0">, </span><span class="s3">41</span><span class="s0">, </span><span class="s3">61</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">24</span><span class="s0">, </span><span class="s3">39</span><span class="s0">, </span><span class="s3">76</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">77</span><span class="s0">, </span><span class="s3">174</span><span class="s0">, </span><span class="s3">95</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">35</span><span class="s0">, </span><span class="s3">44</span><span class="s0">, </span><span class="s3">111</span><span class="s1">)</span><span class="s0">,</span>
              <span class="s1">(</span><span class="s3">214</span><span class="s0">, </span><span class="s3">68</span><span class="s0">, </span><span class="s3">50</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">219</span><span class="s0">, </span><span class="s3">129</span><span class="s0">, </span><span class="s3">156</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">124</span><span class="s0">, </span><span class="s3">185</span><span class="s0">, </span><span class="s3">119</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">236</span><span class="s0">, </span><span class="s3">164</span><span class="s0">, </span><span class="s3">184</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">6</span><span class="s0">, </span><span class="s3">59</span><span class="s0">, </span><span class="s3">39</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">147</span><span class="s0">, </span><span class="s3">208</span><span class="s0">, </span><span class="s3">221</span><span class="s1">)</span><span class="s0">,</span>
              <span class="s1">(</span><span class="s3">7</span><span class="s0">, </span><span class="s3">94</span><span class="s0">, </span><span class="s3">54</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">4</span><span class="s0">, </span><span class="s3">85</span><span class="s0">, </span><span class="s3">110</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">160</span><span class="s0">, </span><span class="s3">29</span><span class="s0">, </span><span class="s3">28</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">236</span><span class="s0">, </span><span class="s3">171</span><span class="s0">, </span><span class="s3">164</span><span class="s1">)</span><span class="s0">, </span><span class="s1">(</span><span class="s3">162</span><span class="s0">, </span><span class="s3">212</span><span class="s0">, </span><span class="s3">178</span><span class="s1">)]</span>

<span class="s1">tim = Turtle()</span>

<span class="s2">#Setup Turtle initial</span>
<span class="s1">tim.hideturtle()</span>
<span class="s1">tim.speed(</span><span class="s4">&quot;fastest&quot;</span><span class="s1">)</span>
<span class="s1">turtle.colormode(</span><span class="s3">255</span><span class="s1">)</span>
<span class="s1">tim.penup()</span>
<span class="s1">tim.setposition(-</span><span class="s3">335.00</span><span class="s0">, </span><span class="s1">-</span><span class="s3">300.00</span><span class="s1">)</span>
<span class="s1">start_position = tim.position()</span>

<span class="s1">width = int(input(</span><span class="s4">&quot;Enter the width: &quot;</span><span class="s1">))</span>

<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">1</span><span class="s0">, </span><span class="s1">width + </span><span class="s3">1</span><span class="s1">):</span>
    <span class="s1">tim.dot(</span><span class="s3">20</span><span class="s0">, </span><span class="s1">color_list[randint(</span><span class="s3">0</span><span class="s0">, </span><span class="s1">len(color_list) - </span><span class="s3">1</span><span class="s1">)])</span>
    <span class="s1">tim.forward(</span><span class="s3">75</span><span class="s1">)</span>

<span class="s0">for </span><span class="s1">j </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">1</span><span class="s0">, </span><span class="s1">width):</span>
    <span class="s1">tim.setposition(start_position[</span><span class="s3">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">(start_position[</span><span class="s3">1</span><span class="s1">]+</span><span class="s3">50.0</span><span class="s1">))</span>
    <span class="s1">print(tim.position())</span>
    <span class="s1">start_position = tim.position()</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">1</span><span class="s0">, </span><span class="s1">width+</span><span class="s3">1</span><span class="s1">):</span>
        <span class="s1">tim.dot(</span><span class="s3">20</span><span class="s0">, </span><span class="s1">color_list[randint(</span><span class="s3">0</span><span class="s0">, </span><span class="s1">len(color_list)-</span><span class="s3">1</span><span class="s1">)])</span>
        <span class="s1">tim.forward(</span><span class="s3">75</span><span class="s1">)</span>


<span class="s1">print(tim.position())</span>
<span class="s1">screen = Screen()</span>
<span class="s1">screen.exitonclick()</span>
</pre>
</body>
</html>