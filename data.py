<html>
<head>
<title>data.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
data.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">requests</span>

<span class="s1">amount_of_questions = </span><span class="s2">10</span>
<span class="s1">type_of_questions = </span><span class="s3">&quot;boolean&quot;</span>
<span class="s1">question_data = []</span>

<span class="s1">parameters = {</span>
    <span class="s3">&quot;amount&quot;</span><span class="s1">: amount_of_questions</span><span class="s0">,</span>
    <span class="s3">&quot;type&quot;</span><span class="s1">: type_of_questions</span><span class="s0">,</span>
<span class="s1">}</span>

<span class="s1">response = requests.get(</span><span class="s3">&quot;https://opentdb.com/api.php&quot;</span><span class="s0">, </span><span class="s1">params=parameters)</span>
<span class="s1">api_json_data = response.json()[</span><span class="s3">&quot;results&quot;</span><span class="s1">]</span>

<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s2">0</span><span class="s0">, </span><span class="s2">10</span><span class="s1">):</span>
    <span class="s1">question_dict = api_json_data[i]</span>
    <span class="s1">question_data.append(question_dict)</span>

<span class="s1">print(question_data)</span>
</pre>
</body>
</html>