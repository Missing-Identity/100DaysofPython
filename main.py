<html>
<head>
<title>main.py</title>
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
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">smtplib</span>
<span class="s0">import </span><span class="s1">time</span>
<span class="s0">import </span><span class="s1">requests</span>
<span class="s0">from </span><span class="s1">datetime </span><span class="s0">import </span><span class="s1">datetime</span>

<span class="s1">MY_LAT = </span><span class="s2">17.385044  </span><span class="s3"># Your latitude</span>
<span class="s1">MY_LONG = </span><span class="s2">78.486671  </span><span class="s3"># Your longitude</span>

<span class="s3"># Mail login and password</span>
<span class="s1">my_email = </span><span class="s4">&quot;ogprime8623@gmail.com&quot;</span>
<span class="s1">password = </span><span class="s4">&quot;Spidey8623&quot;</span>


<span class="s1">parameters = {</span>
    <span class="s4">&quot;lat&quot;</span><span class="s1">: MY_LAT</span><span class="s0">,</span>
    <span class="s4">&quot;lng&quot;</span><span class="s1">: MY_LONG</span><span class="s0">,</span>
    <span class="s4">&quot;formatted&quot;</span><span class="s1">: </span><span class="s2">0</span><span class="s0">,</span>
<span class="s1">}</span>

<span class="s1">response = requests.get(</span><span class="s4">&quot;https://api.sunrise-sunset.org/json&quot;</span><span class="s0">, </span><span class="s1">params=parameters)</span>
<span class="s1">response.raise_for_status()</span>
<span class="s1">data = response.json()</span>
<span class="s1">sunrise = int(data[</span><span class="s4">&quot;results&quot;</span><span class="s1">][</span><span class="s4">&quot;sunrise&quot;</span><span class="s1">].split(</span><span class="s4">&quot;T&quot;</span><span class="s1">)[</span><span class="s2">1</span><span class="s1">].split(</span><span class="s4">&quot;:&quot;</span><span class="s1">)[</span><span class="s2">0</span><span class="s1">])</span>
<span class="s1">sunset = int(data[</span><span class="s4">&quot;results&quot;</span><span class="s1">][</span><span class="s4">&quot;sunset&quot;</span><span class="s1">].split(</span><span class="s4">&quot;T&quot;</span><span class="s1">)[</span><span class="s2">1</span><span class="s1">].split(</span><span class="s4">&quot;:&quot;</span><span class="s1">)[</span><span class="s2">0</span><span class="s1">])</span>

<span class="s1">loop_reset = </span><span class="s0">True</span>


<span class="s0">def </span><span class="s1">send_email(subject</span><span class="s0">, </span><span class="s1">message):</span>
    <span class="s0">with </span><span class="s1">smtplib.SMTP(</span><span class="s4">&quot;smtp.gmail.com&quot;</span><span class="s0">, </span><span class="s1">port=</span><span class="s2">587</span><span class="s1">) </span><span class="s0">as </span><span class="s1">connection:  </span><span class="s3"># Connecting to gmail smtp</span>
        <span class="s1">connection.starttls()  </span><span class="s3"># Transport Layer Security</span>
        <span class="s1">connection.login(user=my_email</span><span class="s0">, </span><span class="s1">password=password)  </span><span class="s3"># Login to your mail</span>
        <span class="s1">connection.sendmail(from_addr=my_email</span><span class="s0">, </span><span class="s1">to_addrs=</span><span class="s4">&quot;unmilan.mukherjee@rocketmail.com&quot;</span><span class="s0">,</span>
                            <span class="s1">msg=</span><span class="s4">f&quot;Subject: </span><span class="s0">{</span><span class="s1">subject</span><span class="s0">}\n\n{</span><span class="s1">message</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)  </span><span class="s3"># Send the mail</span>


<span class="s0">while </span><span class="s1">loop_reset:</span>
    <span class="s3"># Get current time</span>
    <span class="s1">time_now = datetime.now()</span>

    <span class="s3"># Get ISS Data</span>
    <span class="s1">response = requests.get(url=</span><span class="s4">&quot;http://api.open-notify.org/iss-now.json&quot;</span><span class="s1">)</span>
    <span class="s1">response.raise_for_status()</span>
    <span class="s1">data = response.json()</span>

    <span class="s3"># Get ISS Lat&amp;Lng</span>
    <span class="s1">iss_latitude = float(data[</span><span class="s4">&quot;iss_position&quot;</span><span class="s1">][</span><span class="s4">&quot;latitude&quot;</span><span class="s1">])</span>
    <span class="s1">iss_longitude = float(data[</span><span class="s4">&quot;iss_position&quot;</span><span class="s1">][</span><span class="s4">&quot;longitude&quot;</span><span class="s1">])</span>

    <span class="s0">if </span><span class="s1">MY_LAT - </span><span class="s2">5 </span><span class="s1">&lt;= iss_latitude &lt;= MY_LAT + </span><span class="s2">5 </span><span class="s0">and </span><span class="s1">MY_LONG - </span><span class="s2">5 </span><span class="s1">&lt;= iss_longitude &lt;= MY_LONG + </span><span class="s2">5</span><span class="s1">:</span>
        <span class="s0">if </span><span class="s1">sunset &gt; time_now.hour &gt;= sunrise:</span>
            <span class="s1">send_email(subject=</span><span class="s4">&quot;You missed it!&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s4">&quot;The ISS is above you but you can't see it in daytime!&quot;</span><span class="s1">)</span>
            <span class="s1">print(</span><span class="s4">f&quot;ISS-Long: </span><span class="s0">{</span><span class="s1">iss_longitude</span><span class="s0">} </span><span class="s4">and ISS-Lat: </span><span class="s0">{</span><span class="s1">iss_latitude</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
            <span class="s1">print(</span><span class="s4">f&quot;My-Long: </span><span class="s0">{</span><span class="s1">MY_LONG</span><span class="s0">} </span><span class="s4">and My-Lat: </span><span class="s0">{</span><span class="s1">MY_LAT</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
            <span class="s1">loop_reset = </span><span class="s0">False</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">send_email(subject=</span><span class="s4">&quot;Look Up!&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s4">&quot;There is the ISS in the night sky above!&quot;</span><span class="s1">)</span>
            <span class="s1">print(</span><span class="s4">f&quot;ISS-Long: </span><span class="s0">{</span><span class="s1">iss_longitude</span><span class="s0">} </span><span class="s4">and ISS-Lat: </span><span class="s0">{</span><span class="s1">iss_latitude</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
            <span class="s1">print(</span><span class="s4">f&quot;My-Long: </span><span class="s0">{</span><span class="s1">MY_LONG</span><span class="s0">} </span><span class="s4">and My-Lat: </span><span class="s0">{</span><span class="s1">MY_LAT</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
            <span class="s1">loop_reset = </span><span class="s0">False</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">send_email(subject=</span><span class="s4">&quot;Nothing to look up to!&quot;</span><span class="s0">, </span><span class="s1">message=</span><span class="s4">&quot;Nothing is above your head! Sorry!&quot;</span><span class="s1">)</span>
        <span class="s1">print(</span><span class="s4">f&quot;ISS-Long: </span><span class="s0">{</span><span class="s1">iss_longitude</span><span class="s0">} </span><span class="s4">and ISS-Lat: </span><span class="s0">{</span><span class="s1">iss_latitude</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
        <span class="s1">print(</span><span class="s4">f&quot;My-Long: </span><span class="s0">{</span><span class="s1">MY_LONG</span><span class="s0">} </span><span class="s4">and My-Lat: </span><span class="s0">{</span><span class="s1">MY_LAT</span><span class="s0">}</span><span class="s4">&quot;</span><span class="s1">)</span>
    <span class="s1">time.sleep(</span><span class="s2">60</span><span class="s1">)</span>
</pre>
</body>
</html>