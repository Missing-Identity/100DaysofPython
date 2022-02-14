<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #6897bb;}
.s4 { color: #808080;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">tkinter </span><span class="s0">import </span><span class="s1">*</span>
<span class="s1">font = (</span><span class="s2">&quot;Avenir&quot;</span><span class="s0">, </span><span class="s3">18</span><span class="s0">, </span><span class="s2">&quot;normal&quot;</span><span class="s1">)</span>

<span class="s4"># Window setup</span>
<span class="s1">window = Tk()</span>
<span class="s1">window.title(</span><span class="s2">&quot;Miles to Kilometers convertor&quot;</span><span class="s1">)</span>

<span class="s4"># Text-Field</span>
<span class="s1">input_field = Entry(width=</span><span class="s3">10</span><span class="s1">)</span>
<span class="s1">input_field.grid(column=</span><span class="s3">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s3">0</span><span class="s1">)</span>


<span class="s4"># Button Click Action</span>
<span class="s0">def </span><span class="s1">button_click():</span>
    <span class="s1">miles_input = float(input_field.get())</span>
    <span class="s1">kilometers = miles_input*</span><span class="s3">1.609</span>
    <span class="s1">km_calc_label.config(text=</span><span class="s2">f&quot;</span><span class="s0">{</span><span class="s1">kilometers</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s1">)</span>


<span class="s4"># Labels</span>
<span class="s1">miles_label = Label(text=</span><span class="s2">&quot;Miles&quot;</span><span class="s0">, </span><span class="s1">font=font)</span>
<span class="s1">miles_label.grid(row=</span><span class="s3">0</span><span class="s0">, </span><span class="s1">column=</span><span class="s3">2</span><span class="s1">)</span>
<span class="s1">is_equal_to_label = Label(text=</span><span class="s2">&quot;is equal to&quot;</span><span class="s0">, </span><span class="s1">font=font)</span>
<span class="s1">is_equal_to_label.grid(column=</span><span class="s3">0</span><span class="s0">, </span><span class="s1">row=</span><span class="s3">1</span><span class="s1">)</span>
<span class="s1">km_label = Label(text=</span><span class="s2">&quot;kms&quot;</span><span class="s0">, </span><span class="s1">font=font)</span>
<span class="s1">km_label.grid(column=</span><span class="s3">2</span><span class="s0">, </span><span class="s1">row=</span><span class="s3">1</span><span class="s1">)</span>

<span class="s4"># Variable Label</span>
<span class="s1">km_calc_label = Label(text=</span><span class="s2">&quot; &quot;</span><span class="s1">)</span>
<span class="s1">km_calc_label.grid(column=</span><span class="s3">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s3">1</span><span class="s1">)</span>

<span class="s4"># Button</span>
<span class="s1">button = Button(text=</span><span class="s2">&quot;Calculate&quot;</span><span class="s0">, </span><span class="s1">command=button_click)</span>
<span class="s1">button.grid(column=</span><span class="s3">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s3">2</span><span class="s1">)</span>

<span class="s1">window.mainloop()</span>
</pre>
</body>
</html>