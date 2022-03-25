<html>
<head>
<title>quiz_brain.py</title>
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
quiz_brain.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">html</span>


<span class="s0">class </span><span class="s1">QuizBrain:</span>

    <span class="s0">def </span><span class="s1">__init__(self</span><span class="s0">, </span><span class="s1">q_list):</span>
        <span class="s1">self.question_number = </span><span class="s2">0</span>
        <span class="s1">self.score = </span><span class="s2">0</span>
        <span class="s1">self.question_list = q_list</span>
        <span class="s1">self.current_question = </span><span class="s0">None</span>

    <span class="s0">def </span><span class="s1">still_has_questions(self):</span>
        <span class="s0">return </span><span class="s1">self.question_number &lt; len(self.question_list)</span>

    <span class="s0">def </span><span class="s1">next_question(self):</span>
        <span class="s1">self.current_question = self.question_list[self.question_number]</span>
        <span class="s1">self.question_number += </span><span class="s2">1</span>
        <span class="s1">q_text = html.unescape(self.current_question.text)</span>
        <span class="s0">return </span><span class="s3">f&quot;Q.</span><span class="s0">{</span><span class="s1">self.question_number</span><span class="s0">}</span><span class="s3">: </span><span class="s0">{</span><span class="s1">q_text</span><span class="s0">} </span><span class="s3">(True/False): &quot;</span>

    <span class="s0">def </span><span class="s1">check_answer(self</span><span class="s0">, </span><span class="s1">user_answer):</span>
        <span class="s1">correct_answer = self.current_question.answer</span>
        <span class="s0">if </span><span class="s1">user_answer.lower() == correct_answer.lower():</span>
            <span class="s0">return True</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s0">return False</span>
</pre>
</body>
</html>