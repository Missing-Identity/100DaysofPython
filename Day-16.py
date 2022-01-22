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
<pre><span class="s0">from </span><span class="s1">menu </span><span class="s0">import </span><span class="s1">Menu</span><span class="s0">, </span><span class="s1">MenuItem</span>
<span class="s0">from </span><span class="s1">coffee_maker </span><span class="s0">import </span><span class="s1">CoffeeMaker</span>
<span class="s0">from </span><span class="s1">money_machine </span><span class="s0">import </span><span class="s1">MoneyMachine</span>

<span class="s1">menu = Menu()</span>
<span class="s1">make = CoffeeMaker()</span>
<span class="s1">money_manager = MoneyMachine()</span>

<span class="s1">loop_condition = </span><span class="s0">True</span>
<span class="s0">while </span><span class="s1">loop_condition:</span>
    <span class="s1">order = input(</span><span class="s2">f&quot;What would you like to order?: </span><span class="s0">{</span><span class="s1">menu.get_items()</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s1">).lower()</span>
    <span class="s0">if </span><span class="s1">order == </span><span class="s2">&quot;report&quot;</span><span class="s1">:</span>
        <span class="s1">make.report()</span>
    <span class="s0">elif </span><span class="s1">order == </span><span class="s2">&quot;off&quot;</span><span class="s1">:</span>
        <span class="s0">break</span>
    <span class="s0">elif </span><span class="s1">order == </span><span class="s2">&quot;latte&quot; </span><span class="s0">or </span><span class="s1">order == </span><span class="s2">&quot;espresso&quot; </span><span class="s0">or </span><span class="s1">order == </span><span class="s2">&quot;cappuccino&quot;</span><span class="s1">:</span>
        <span class="s1">drink = menu.find_drink(order)</span>
        <span class="s1">item = MenuItem(drink.name</span><span class="s0">, </span><span class="s1">drink.ingredients[</span><span class="s2">'water'</span><span class="s1">]</span><span class="s0">, </span><span class="s1">drink.ingredients[</span><span class="s2">'milk'</span><span class="s1">]</span><span class="s0">, </span><span class="s1">drink.ingredients[</span><span class="s2">'coffee'</span><span class="s1">]</span><span class="s0">,</span>
                        <span class="s1">drink.cost)</span>
        <span class="s0">if </span><span class="s1">make.is_resource_sufficient(item):</span>
            <span class="s0">if </span><span class="s1">money_manager.make_payment(drink.cost):</span>
                <span class="s1">make.make_coffee(item)</span>
    <span class="s0">elif </span><span class="s1">order == </span><span class="s2">&quot;profit&quot;</span><span class="s1">:</span>
        <span class="s1">money_manager.report()</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">print(</span><span class="s2">&quot;Sorry! Wrong order! Please try ordering something else!&quot;</span><span class="s1">)</span>
</pre>
</body>
</html>