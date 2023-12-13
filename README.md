
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<img src='https://i.ibb.co/HpYSnXb/IMG-5169.jpg'></img>
<h1><font color="pink">Sakura: Template Engineer</font></h1>
<h3>The templating tool is designed for training purposes. Performance was not the main goal of the author.</h3>
<p>The substrings for the beginning and end of the pattern can be set in the "bounds" variable in sakura.py. The default bounds are: start - <code>{% code %}</code> - stop</p>
<p>An example of a template:</p>
<pre><code>{% ;for;(works, 1, 10, 1) {
    ;print;(works, work)
}%}</code></pre>

<h2><font color="pink">Functions and Cycles</font></h2>
<h3>There are two kinds of commands in the templating tool: "functions" and "cycles".</h3>
<p>The command begins with boundary characters, e.g. <code>;command;</code> - ";" boundary character (i.e. the name of the command must be framed by boundary characters). You can set boundary characters for commands in the <code>OPERATOR_FRAME</code> variable in the parse.py file.</p>
<p>Each command has a header, e.g. <code>;command;;(1,3,4)</code> - "(1,3,4)" - header, "1" "3" "4" - header arguments. Custom functions can be added in the functions.py file. Signature of loops: <code>(iter_var, start, stop, step)</code>.</p>

<h2><font color="pink">License</font></h2>
<p>This templating tool is provided under the MIT License. See the <a href="https://github.com/ermantraun/sakura/blob/main/LICENSE">LICENSE</a> file for details.</p>

</body>
</html>

