<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">question_model </span><span class="s0">import </span><span class="s1">Question</span>
<span class="s0">from </span><span class="s1">data </span><span class="s0">import </span><span class="s1">question_data</span>
<span class="s0">from </span><span class="s1">quiz_brain </span><span class="s0">import </span><span class="s1">QuizBrain</span>
<span class="s0">from </span><span class="s1">ui </span><span class="s0">import </span><span class="s1">QuizInterface</span>

<span class="s1">question_bank = []</span>
<span class="s0">for </span><span class="s1">question </span><span class="s0">in </span><span class="s1">question_data:</span>
    <span class="s1">question_text = question[</span><span class="s2">&quot;question&quot;</span><span class="s1">]</span>
    <span class="s1">question_answer = question[</span><span class="s2">&quot;correct_answer&quot;</span><span class="s1">]</span>
    <span class="s1">new_question = Question(question_text</span><span class="s0">, </span><span class="s1">question_answer)</span>
    <span class="s1">question_bank.append(new_question)</span>


<span class="s1">quiz = QuizBrain(question_bank)</span>
<span class="s1">quiz_ui = QuizInterface(quiz)</span>
</pre>
</body>
</html>