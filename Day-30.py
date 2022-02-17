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
<span class="s0">from </span><span class="s1">tkinter </span><span class="s0">import </span><span class="s1">messagebox  </span><span class="s2"># For Pop-up</span>
<span class="s0">from </span><span class="s1">random </span><span class="s0">import </span><span class="s1">choice</span><span class="s0">, </span><span class="s1">randint</span><span class="s0">, </span><span class="s1">shuffle</span>
<span class="s0">import </span><span class="s1">pyperclip  </span><span class="s2"># For copy and paste from clipboard</span>
<span class="s0">import </span><span class="s1">json</span>

<span class="s1">FONT = (</span><span class="s3">&quot;Avenir&quot;</span><span class="s0">, </span><span class="s4">18</span><span class="s0">, </span><span class="s3">&quot;normal&quot;</span><span class="s1">)</span>

<span class="s2"># ---------------------------- PASSWORD GENERATOR ------------------------------- #</span>
<span class="s1">letters = [</span><span class="s3">'a'</span><span class="s0">, </span><span class="s3">'b'</span><span class="s0">, </span><span class="s3">'c'</span><span class="s0">, </span><span class="s3">'d'</span><span class="s0">, </span><span class="s3">'e'</span><span class="s0">, </span><span class="s3">'f'</span><span class="s0">, </span><span class="s3">'g'</span><span class="s0">, </span><span class="s3">'h'</span><span class="s0">, </span><span class="s3">'i'</span><span class="s0">, </span><span class="s3">'j'</span><span class="s0">, </span><span class="s3">'k'</span><span class="s0">, </span><span class="s3">'l'</span><span class="s0">, </span><span class="s3">'m'</span><span class="s0">, </span><span class="s3">'n'</span><span class="s0">, </span><span class="s3">'o'</span><span class="s0">, </span><span class="s3">'p'</span><span class="s0">, </span><span class="s3">'q'</span><span class="s0">, </span><span class="s3">'r'</span><span class="s0">, </span><span class="s3">'s'</span><span class="s0">, </span><span class="s3">'t'</span><span class="s0">, </span><span class="s3">'u'</span><span class="s0">, </span><span class="s3">'v'</span><span class="s0">,</span>
           <span class="s3">'w'</span><span class="s0">, </span><span class="s3">'x'</span><span class="s0">, </span><span class="s3">'y'</span><span class="s0">, </span><span class="s3">'z'</span><span class="s0">, </span><span class="s3">'A'</span><span class="s0">, </span><span class="s3">'B'</span><span class="s0">, </span><span class="s3">'C'</span><span class="s0">, </span><span class="s3">'D'</span><span class="s0">, </span><span class="s3">'E'</span><span class="s0">, </span><span class="s3">'F'</span><span class="s0">, </span><span class="s3">'G'</span><span class="s0">, </span><span class="s3">'H'</span><span class="s0">, </span><span class="s3">'I'</span><span class="s0">, </span><span class="s3">'J'</span><span class="s0">, </span><span class="s3">'K'</span><span class="s0">, </span><span class="s3">'L'</span><span class="s0">, </span><span class="s3">'M'</span><span class="s0">, </span><span class="s3">'N'</span><span class="s0">, </span><span class="s3">'O'</span><span class="s0">, </span><span class="s3">'P'</span><span class="s0">, </span><span class="s3">'Q'</span><span class="s0">, </span><span class="s3">'R'</span><span class="s0">,</span>
           <span class="s3">'S'</span><span class="s0">, </span><span class="s3">'T'</span><span class="s0">, </span><span class="s3">'U'</span><span class="s0">, </span><span class="s3">'V'</span><span class="s0">, </span><span class="s3">'W'</span><span class="s0">, </span><span class="s3">'X'</span><span class="s0">, </span><span class="s3">'Y'</span><span class="s0">, </span><span class="s3">'Z'</span><span class="s1">]</span>
<span class="s1">numbers = [</span><span class="s3">'0'</span><span class="s0">, </span><span class="s3">'1'</span><span class="s0">, </span><span class="s3">'2'</span><span class="s0">, </span><span class="s3">'3'</span><span class="s0">, </span><span class="s3">'4'</span><span class="s0">, </span><span class="s3">'5'</span><span class="s0">, </span><span class="s3">'6'</span><span class="s0">, </span><span class="s3">'7'</span><span class="s0">, </span><span class="s3">'8'</span><span class="s0">, </span><span class="s3">'9'</span><span class="s1">]</span>
<span class="s1">symbols = [</span><span class="s3">'!'</span><span class="s0">, </span><span class="s3">'#'</span><span class="s0">, </span><span class="s3">'$'</span><span class="s0">, </span><span class="s3">'%'</span><span class="s0">, </span><span class="s3">'&amp;'</span><span class="s0">, </span><span class="s3">'('</span><span class="s0">, </span><span class="s3">')'</span><span class="s0">, </span><span class="s3">'*'</span><span class="s0">, </span><span class="s3">'+'</span><span class="s1">]</span>


<span class="s0">def </span><span class="s1">generate_password():</span>
    <span class="s1">password_entry.delete(</span><span class="s4">0</span><span class="s0">, </span><span class="s1">END)</span>
    <span class="s1">password_list = [choice(letters) </span><span class="s0">for </span><span class="s1">_ </span><span class="s0">in </span><span class="s1">range(randint(</span><span class="s4">8</span><span class="s0">, </span><span class="s4">10</span><span class="s1">))]</span>
    <span class="s1">password_list += ([choice(symbols) </span><span class="s0">for </span><span class="s1">_ </span><span class="s0">in </span><span class="s1">range(randint(</span><span class="s4">2</span><span class="s0">, </span><span class="s4">4</span><span class="s1">))])</span>
    <span class="s1">password_list += ([choice(numbers) </span><span class="s0">for </span><span class="s1">_ </span><span class="s0">in </span><span class="s1">range(randint(</span><span class="s4">2</span><span class="s0">, </span><span class="s4">4</span><span class="s1">))])</span>

    <span class="s1">shuffle(password_list)</span>

    <span class="s1">password = </span><span class="s3">&quot;&quot;</span><span class="s1">.join(password_list)  </span><span class="s2"># join basically goes through every item in the list/dict passed and</span>
    <span class="s2"># joins them with the str in between each iteration provided in the &quot;&quot;</span>
    <span class="s1">password_entry.insert(</span><span class="s4">0</span><span class="s0">, </span><span class="s3">f&quot;</span><span class="s0">{</span><span class="s1">password</span><span class="s0">}</span><span class="s3">&quot;</span><span class="s1">)</span>
    <span class="s1">pyperclip.copy(password)</span>


<span class="s2"># ---------------------------- SAVE PASSWORD ------------------------------- #</span>


<span class="s0">def </span><span class="s1">save():</span>
    <span class="s1">website = website_entry.get()</span>
    <span class="s1">username = username_entry.get()</span>
    <span class="s1">password = password_entry.get()</span>
    <span class="s1">new_data = {website: {</span>
        <span class="s3">&quot;Username&quot;</span><span class="s1">: username</span><span class="s0">,</span>
        <span class="s3">&quot;Password&quot;</span><span class="s1">: password</span>
    <span class="s1">}</span>
    <span class="s1">}</span>

    <span class="s0">if </span><span class="s1">len(website) == </span><span class="s4">0 </span><span class="s0">or </span><span class="s1">len(username) == </span><span class="s4">0 </span><span class="s0">or </span><span class="s1">len(password) == </span><span class="s4">0</span><span class="s1">:</span>
        <span class="s1">messagebox.showinfo(title=</span><span class="s3">&quot;Warning!&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s3">&quot;One or more of the fields is empty, please fill all the fields!&quot;</span><span class="s1">)</span>

    <span class="s0">else</span><span class="s1">:</span>
        <span class="s0">try</span><span class="s1">:</span>
            <span class="s0">with </span><span class="s1">open(</span><span class="s3">&quot;data.json&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s3">&quot;r&quot;</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
                <span class="s1">data = json.load(file)</span>
        <span class="s0">except </span><span class="s1">FileNotFoundError:</span>
            <span class="s0">with </span><span class="s1">open(</span><span class="s3">&quot;data.json&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s3">&quot;w&quot;</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
                <span class="s1">json.dump(new_data</span><span class="s0">, </span><span class="s1">file</span><span class="s0">, </span><span class="s1">indent=</span><span class="s4">4</span><span class="s1">)</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s0">with </span><span class="s1">open(</span><span class="s3">&quot;data.json&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s3">&quot;w&quot;</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
                <span class="s1">data.update(new_data)</span>
                <span class="s1">json.dump(data</span><span class="s0">, </span><span class="s1">file</span><span class="s0">, </span><span class="s1">indent=</span><span class="s4">4</span><span class="s1">)</span>
        <span class="s0">finally</span><span class="s1">:</span>
            <span class="s1">website_entry.delete(</span><span class="s4">0</span><span class="s0">, </span><span class="s1">END)</span>
            <span class="s1">username_entry.delete(</span><span class="s4">0</span><span class="s0">, </span><span class="s1">END)</span>
            <span class="s1">password_entry.delete(</span><span class="s4">0</span><span class="s0">, </span><span class="s1">END)</span>


<span class="s2"># ---------------------------- SEARCH ------------------------------- #</span>
<span class="s0">def </span><span class="s1">search():</span>
    <span class="s1">search_text = website_entry.get()</span>
    <span class="s0">try</span><span class="s1">:</span>
        <span class="s0">with </span><span class="s1">open(</span><span class="s3">&quot;data.json&quot;</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
            <span class="s1">data = json.load(file)</span>
    <span class="s0">except </span><span class="s1">FileNotFoundError:</span>
        <span class="s1">messagebox.showinfo(title=</span><span class="s3">&quot;Error&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s3">&quot;No Data File Found&quot;</span><span class="s1">)</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s0">if </span><span class="s1">search_text </span><span class="s0">in </span><span class="s1">data:</span>
            <span class="s1">username = data[search_text][</span><span class="s3">&quot;Username&quot;</span><span class="s1">]</span>
            <span class="s1">password = data[search_text][</span><span class="s3">&quot;Password&quot;</span><span class="s1">]</span>
            <span class="s1">messagebox.showinfo(title=</span><span class="s3">f&quot;</span><span class="s0">{</span><span class="s1">search_text</span><span class="s0">}</span><span class="s3">&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s3">f&quot;Username: </span><span class="s0">{</span><span class="s1">username</span><span class="s0">}\n</span><span class="s3">&quot;</span>
                                                                <span class="s3">f&quot;Password: </span><span class="s0">{</span><span class="s1">password</span><span class="s0">}</span><span class="s3">&quot;</span><span class="s1">)</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">messagebox.showinfo(title=</span><span class="s3">&quot;Error&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s3">&quot;Username not found&quot;</span><span class="s1">)</span>


<span class="s2"># ---------------------------- UI SETUP ------------------------------- #</span>
<span class="s1">window = Tk()</span>
<span class="s1">window.title(</span><span class="s3">&quot;Password Manager&quot;</span><span class="s1">)</span>
<span class="s1">window.config(padx=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">pady=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s1">)</span>

<span class="s2"># Canvas Image</span>
<span class="s1">canvas = Canvas(width=</span><span class="s4">200</span><span class="s0">, </span><span class="s1">height=</span><span class="s4">200</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">highlightthickness=</span><span class="s4">0</span><span class="s1">)</span>
<span class="s1">logo_img = PhotoImage(file=</span><span class="s3">&quot;logo.png&quot;</span><span class="s1">)</span>
<span class="s1">canvas.create_image(</span><span class="s4">100</span><span class="s0">, </span><span class="s4">100</span><span class="s0">, </span><span class="s1">image=logo_img)</span>
<span class="s1">canvas.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">0</span><span class="s1">)</span>

<span class="s2"># Labels</span>
<span class="s1">website_label = Label(text=</span><span class="s3">&quot;Website: &quot;</span><span class="s0">, </span><span class="s1">font=FONT</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">fg=</span><span class="s3">&quot;black&quot;</span><span class="s1">)</span>
<span class="s1">username_label = Label(text=</span><span class="s3">&quot;Email/Username: &quot;</span><span class="s0">, </span><span class="s1">font=FONT</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">fg=</span><span class="s3">&quot;black&quot;</span><span class="s1">)</span>
<span class="s1">password_label = Label(text=</span><span class="s3">&quot;Password: &quot;</span><span class="s0">, </span><span class="s1">font=FONT</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">fg=</span><span class="s3">&quot;black&quot;</span><span class="s1">)</span>

<span class="s2"># Entries</span>
<span class="s1">website_entry = Entry(width=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;#e32636&quot;</span><span class="s1">)</span>
<span class="s1">website_entry.focus()</span>
<span class="s1">username_entry = Entry(width=</span><span class="s4">35</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;#e32636&quot;</span><span class="s1">)</span>
<span class="s1">username_entry.insert(</span><span class="s4">0</span><span class="s0">, </span><span class="s3">&quot;dummy@mail.com&quot;</span><span class="s1">)</span>
<span class="s1">password_entry = Entry(width=</span><span class="s4">20</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;#e32636&quot;</span><span class="s1">)</span>

<span class="s2"># Buttons</span>
<span class="s1">generate_button = Button(text=</span><span class="s3">&quot;Generate Password&quot;</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">width=</span><span class="s4">11</span><span class="s0">,</span>
                         <span class="s1">command=generate_password)</span>
<span class="s1">add_button = Button(text=</span><span class="s3">&quot;Add&quot;</span><span class="s0">, </span><span class="s1">width=</span><span class="s4">34</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">command=save)</span>
<span class="s1">search_button = Button(text=</span><span class="s3">&quot;Search&quot;</span><span class="s0">, </span><span class="s1">width=</span><span class="s4">11</span><span class="s0">, </span><span class="s1">bg=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">highlightbackground=</span><span class="s3">&quot;white&quot;</span><span class="s0">, </span><span class="s1">command=search)</span>

<span class="s2"># Grids</span>
<span class="s1">website_label.grid(column=</span><span class="s4">0</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">1</span><span class="s1">)</span>
<span class="s1">website_entry.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">1</span><span class="s1">)</span>
<span class="s1">username_label.grid(column=</span><span class="s4">0</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">2</span><span class="s1">)</span>
<span class="s1">username_entry.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">2</span><span class="s0">, </span><span class="s1">columnspan=</span><span class="s4">2</span><span class="s1">)</span>
<span class="s1">password_label.grid(column=</span><span class="s4">0</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">3</span><span class="s1">)</span>
<span class="s1">password_entry.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">3</span><span class="s1">)</span>
<span class="s1">generate_button.grid(column=</span><span class="s4">2</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">3</span><span class="s1">)</span>
<span class="s1">add_button.grid(column=</span><span class="s4">1</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">4</span><span class="s0">, </span><span class="s1">columnspan=</span><span class="s4">2</span><span class="s1">)</span>
<span class="s1">search_button.grid(column=</span><span class="s4">2</span><span class="s0">, </span><span class="s1">row=</span><span class="s4">1</span><span class="s1">)</span>

<span class="s1">window.mainloop()</span>
</pre>
</body>
</html>