<img src='https://i.ibb.co/HpYSnXb/IMG-5169.jpg'></img>
<h1><font color="pink">Sakura: template engineer</font></h1>
<h3>The templating tool is designed for training purposes. Performance was not the main goal of the author. <p>The substrings for the beginning and end of the pattern can be set in the "bounds" variable in sakura.py. The default bounds are: start - {% code %} - stop</p><p>An example of a template: {% ;for;(works, 1, 10, 1) {
                                                ;print;(works, work)
                                           } %}</p></h3>

<h2><font color='pink'> Functions and cycles</font></h2>
<h3>There are two kinds of commands in the templating tool: "functions" and "cycles". 
<p>The command begins with boundary characters, e.g. ;command; - ";" boundary character (i.e. the name of the command must be framed by boundary characters). You can set boundary characters for commands in the OPERATOR_FRAME variable in the parse.py file</p> <p>Each command has a header, e.g. ;command;;(1,3,4) - "(1,3,4)" - header, "1" "3" "4" - header arguments. Custom functions can be added in the functions.py file.  Signature of loops: (iter_var, start, stop, step).</p></h3>
