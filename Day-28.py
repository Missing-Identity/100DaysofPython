<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #808080;}
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
<pre><span class="s0">from </span><span class="s1">tkinter </span><span class="s0">import </span><span class="s1">*</span>
<span class="s0">import </span><span class="s1">math</span>
<span class="s2"># ---------------------------- CONSTANTS ------------------------------- #</span>
<span class="s1">PINK = </span><span class="s3">&quot;#e2979c&quot;</span>
<span class="s1">RED = </span><span class="s3">&quot;#e7305b&quot;</span>
<span class="s1">GREEN = </span><span class="s3">&quot;#9bdeac&quot;</span>
<span class="s1">YELLOW = </span><span class="s3">&quot;#f7f5dd&quot;</span>
<span class="s1">FONT_NAME = </span><span class="s3">&quot;Courier&quot;</span>
<span class="s1">WORK_MIN = </span><span class="s4">25</span>
<span class="s1">SHORT_BREAK_MIN = </span><span class="s4">5</span>
<span class="s1">LONG_BREAK_MIN = </span><span class="s4">20</span>
<span class="s1">reps = </span><span class="s4">0</span>
<span class="s1">timer = </span><span class="s3">&quot;&quot;</span>

<span class="s2"># ---------------------------- TIMER RESET ------------------------------- #</span>


<span class="s0">def </span><span class="s1">reset_timer():</span>
    <span class="s1">window.after_cancel(timer)</span>
    <span class="s0">global </span><span class="s1">reps</span>
    <span class="s1">canvas.itemconfig(timer_countdown</span><span class="s0">, </span><span class="s1">text=</span><span class="s3">&quot;00:00&quot;</span><span class="s1">)</span>
    <span class="s1">reps = </span><span class="s4">0</span>
    <span class="s1">timer_text.config(text=</span><span class="s3">&quot;Timer&quot;</span><span class="s0">, </span><span class="s1">fg=GREEN)</span>
    <span class="s1">tick_mark.config(text=</span><span class="s3">&quot;&quot;</span><span class="s1">)</span>

<span class="s2"># ---------------------------- TIMER MECHANISM ------------------------------- #</span>


<span class="s0">def </span><span class="s1">start_timer():</span>
    <span class="s0">global </span><span class="s1">reps</span>
    <span class="s1">reps += </span><span class="s4">1</span>
    <span class="s1">work_seconds = WORK_MIN*</span><span class="s4">60</span>
    <span class="s1">short_break_seconds = SHORT_BREAK_MIN*</span><span class="s4">60</span>
    <span class="s1">long_break_seconds = LONG_BREAK_MIN*</span><span class="s4">60</span>
    <span class="s0">if </span><span class="s1">reps % </span><span class="s4">8 </span><span class="s1">== </span><span class="s4">0</span><span class="s1">:</span>
        <span class="s1">count_down(long_break_seconds)</span>
        <span class="s1">timer_text.config(text=</span><span class="s3">&quot;Long Break&quot;</span><span class="s0">, </span><span class="s1">fg=RED)</span>
    <span class="s0">elif </span><span class="s1">reps % </span><span class="s4">2 </span><span class="s1">== </span><span class="s4">0</span><span class="s1">:</span>
        <span class="s1">count_down(short_break_seconds)</span>
        <span class="s1">timer_text.config(text=</span><span class="s3">&quot;Short Break&quot;</span><span class="s0">, </span><span class="s1">fg=PINK)</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">count_down(work_seconds)</span>
        <span class="s1">timer_text.config(text=</span><span class="s3">&quot;Work Time!&quot;</span><span class="s0">, </span><span class="s1">fg=GREEN)</span>

<span class="s2"># ---------------------------- COUNTDOWN MECHANISM ------------------------------- #</span>


<span class="s0">def </span><span class="s1">count_down(count):</span>
    <span class="s0">global </span><span class="s1">reps</span>
    <span class="s0">global </span><span class="s1">timer</span>
    <span class="s1">count_min = math.floor(count/</span><span class="s4">60</span><span class="s1">)    </span><span class="s2"># Removing floats</span>
    <span class="s1">count_seconds = count % </span><span class="s4">60</span>
    <span class="s0">if </span><span class="s1">count_seconds &lt; </span><span class="s4">10</span><span class="s1">:</span>
        <span class="s1">count_seconds = </span><span class="s3">f&quot;0</span><span class="s0">{</span><span class="s1">count_seconds</span><span class="s0">}</span><span class="s3">&quot;</span>
    <span class="s1">canvas.itemconfig(timer_countdown</span><span class="s0">, </span><span class="s1">text=</span><span class="s3">f&quot;</span><span class="s0">{</span><span class="s1">count_min</span><span class="s0">}</span><span class="s3">:</span><span class="s0">{</span><span class="s1">count_seconds</span><span class="s0">}</span><span class="s3">&quot;</span><span class="s1">)</span>
    <span class="s0">if </span><span class="s1">count &gt; </span><span class="s4">0</span><span class="s1">:</span>
        <span class="s1">timer = window.after(</span><span class="s4">1000</span><span class="s0">, </span><span class="s1">count_down</span><span class="s0">, </span><span class="s1">count-</span><span class="s4">1</span><span class="s1">)</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">start_timer()</span>
        <span class="s1">tick = </span><span class="s3">&quot;&quot;</span>
        <span class="s1">work_sessions = math.floor(reps/</span><span class="s4">2</span><span class="s1">)</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(work_sessions):</span>
            <span class="s1">tick += </span><span class="s3">&quot;✔&quot;</span>
        <span class="s1">tick_mark.config(text=tick)</span>

<span class="s2"># ---------------------------- UI SETUP ------------------------------- #</span>


<span class="s1">window = Tk()</span>
<span class="s1">window.title(</span><span class="s3">&quot;Pomodoro GUI&quot;</span><span class="s1">)</span>
<span class="s1">window.config(padx=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">pady=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">bg=YELLOW)</span>


<span class="s2"># Canvas setup</span>
<span class="s1">canvas = Canvas(width=</span><span class="s4">200</span><span class="s0">, </span><span class="s1">height=</span><span class="s4">224</span><span class="s0">, </span><span class="s1">bg=YELLOW</span><span class="s0">, </span><span class="s1">highlightthickness=</span><span class="s4">0</span><span class="s1">)</span>
<span class="s1">tomato_img = PhotoImage(file=</span><span class="s3">&quot;tomato.png&quot;</span><span class="s1">)</span>
<span class="s1">canvas.create_image(</span><span class="s4">100</span><span class="s0">, </span><span class="s4">112</span><span class="s0">, </span><span class="s1">image=tomato_img)  </span><span class="s2"># Putting half the values of size of image so that it is in the center.</span>
<span class="s1">timer_countdown = canvas.create_text(</span><span class="s4">100</span><span class="s0">, </span><span class="s4">130</span><span class="s0">, </span><span class="s1">text=</span><span class="s3">&quot;00:00&quot;</span><span class="s0">, </span><span class="s1">fill=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">font=(FONT_NAME</span><span class="s0">, </span><span class="s4">35</span><span class="s0">, </span><span class="s3">&quot;bold&quot;</span><span class="s1">))</span>
<span class="s1">canvas.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">1</span><span class="s1">)</span>


<span class="s2"># Button setup</span>
<span class="s1">start_button = Button(text=</span><span class="s3">&quot;Start&quot;</span><span class="s0">, </span><span class="s1">bg=YELLOW</span><span class="s0">, </span><span class="s1">highlightbackground=YELLOW</span><span class="s0">, </span><span class="s1">command=start_timer)</span>
<span class="s1">reset_button = Button(text=</span><span class="s3">&quot;Reset&quot;</span><span class="s0">, </span><span class="s1">bg=YELLOW</span><span class="s0">, </span><span class="s1">highlightbackground=YELLOW</span><span class="s0">, </span><span class="s1">command=reset_timer)</span>
<span class="s1">start_button.grid(column=</span><span class="s4">0</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">2</span><span class="s1">)</span>
<span class="s1">reset_button.grid(column=</span><span class="s4">2</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">2</span><span class="s1">)</span>

<span class="s2"># Label setup</span>
<span class="s1">timer_text = Label(text=</span><span class="s3">&quot;Timer&quot;</span><span class="s0">, </span><span class="s1">font=(FONT_NAME</span><span class="s0">, </span><span class="s4">34</span><span class="s0">, </span><span class="s3">&quot;bold&quot;</span><span class="s1">)</span><span class="s0">, </span><span class="s1">bg=YELLOW</span><span class="s0">, </span><span class="s1">fg=GREEN)</span>
<span class="s1">tick_mark = Label(text=</span><span class="s3">&quot;&quot;</span><span class="s0">, </span><span class="s1">font=(FONT_NAME</span><span class="s0">, </span><span class="s4">24</span><span class="s0">, </span><span class="s3">&quot;bold&quot;</span><span class="s1">)</span><span class="s0">, </span><span class="s1">bg=YELLOW</span><span class="s0">, </span><span class="s1">fg=GREEN)</span>
<span class="s1">timer_text.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">0</span><span class="s1">)</span>
<span class="s1">tick_mark.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">3</span><span class="s1">)</span>

<span class="s1">window.mainloop()</span>
</pre>
</body>
</html>