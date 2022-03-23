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
<pre><span class="s0">import </span><span class="s1">smtplib</span>
<span class="s0">import </span><span class="s1">random</span>
<span class="s0">import </span><span class="s1">datetime </span><span class="s0">as </span><span class="s1">dt</span>
<span class="s0">import </span><span class="s1">pandas</span>

<span class="s2"># Letter Picker and Placeholder</span>
<span class="s1">letter_number = random.randint(</span><span class="s3">1</span><span class="s0">, </span><span class="s3">3</span><span class="s1">)</span>
<span class="s1">placeholder = </span><span class="s4">&quot;[NAME]&quot;</span>

<span class="s2"># Mail login and password</span>
<span class="s1">my_email = </span><span class="s4">&quot;ogprime8623@gmail.com&quot;</span>
<span class="s1">password = </span><span class="s4">&quot;Spidey8623&quot;</span>

<span class="s2"># CSV reader and date checker</span>
<span class="s1">csv_data = pandas.read_csv(</span><span class="s4">&quot;birthdays.csv&quot;</span><span class="s1">)</span>
<span class="s1">today = dt.datetime.now()</span>

<span class="s0">for </span><span class="s1">num </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">0</span><span class="s0">, </span><span class="s1">len(csv_data)):  </span><span class="s2"># Go through all rows in CSV</span>
    <span class="s0">if </span><span class="s1">csv_data.month[num] == today.month </span><span class="s0">and </span><span class="s1">csv_data.day[num] == today.day:  </span><span class="s2"># Check for matching date</span>
        <span class="s1">name = csv_data.name[num]  </span><span class="s2"># Set name variable if found</span>
        <span class="s0">with </span><span class="s1">open(</span><span class="s4">f&quot;../emailHappyBirthday/letter_templates/letter_</span><span class="s0">{</span><span class="s1">letter_number</span><span class="s0">}</span><span class="s4">.txt&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s4">'r'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">file:</span>
            <span class="s1">content = file.read()</span>
            <span class="s1">new_content = content.replace(placeholder</span><span class="s0">, </span><span class="s1">name)  </span><span class="s2"># Replace placeholder name with actual</span>
            <span class="s0">with </span><span class="s1">open(</span><span class="s4">f&quot;../emailHappyBirthday/final_letters/letter-</span><span class="s0">{</span><span class="s1">letter_number</span><span class="s0">}</span><span class="s4">.txt&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s4">'w'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">new_file:</span>
                <span class="s1">new_file.write(new_content)  </span><span class="s2"># Create a new txt file with changed name</span>
        <span class="s0">with </span><span class="s1">open(</span><span class="s4">f&quot;../emailHappyBirthday/final_letters/letter-</span><span class="s0">{</span><span class="s1">letter_number</span><span class="s0">}</span><span class="s4">.txt&quot;</span><span class="s0">, </span><span class="s1">mode=</span><span class="s4">'r'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">mail_file:</span>
            <span class="s1">letter = mail_file.read()</span>
            <span class="s1">letter = str(letter)</span>
            <span class="s0">with </span><span class="s1">smtplib.SMTP(</span><span class="s4">&quot;smtp.gmail.com&quot;</span><span class="s0">, </span><span class="s1">port=</span><span class="s3">587</span><span class="s1">) </span><span class="s0">as </span><span class="s1">connection:  </span><span class="s2"># Connecting to gmail smtp</span>
                <span class="s1">connection.starttls()  </span><span class="s2"># Transport Layer Security</span>
                <span class="s1">connection.login(user=my_email</span><span class="s0">, </span><span class="s1">password=password)  </span><span class="s2"># Login to your mail</span>
                <span class="s1">connection.sendmail(from_addr=my_email</span><span class="s0">, </span><span class="s1">to_addrs=</span><span class="s4">&quot;ogprime8623@gmail.com&quot;</span><span class="s0">,</span>
                                    <span class="s1">msg=</span><span class="s4">f&quot;Subject: Birthday Wishes</span><span class="s0">\n\n{</span><span class="s1">letter</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)  </span><span class="s2"># Send the mail</span>
</pre>
</body>
</html>