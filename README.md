# Trains
<h2><u>IBM train technical Assessment</u></h2>

<p>This is a project that calculates the weight of a journey
given entire routes by segmenting individual routes.</p>

I worked under the assumption of a limited defined route
<p>Routes available :</p>
<ol>
    <li>AB - weight - 5</li>
    <li>BC - weight - 4</li>
    <li>CD - weight - 8</li>
    <li>DC - weight - 8</li>
    <li>DE - weight - 6</li>
    <li>AD - weight - 5</li>
    <li>CE - weight - 2</li>
    <li>EB - weight - 3</li>
    <li>AE - weight - 7</li>
</ol>

<h2><u>How it works.</u></h2>
<p>It works by separating routes into the two nodes adjacent 
to each other starting from the left most node.
</p>
<p>
This design focuses on a linear time complexity capable 
of a liner growth rate. Therefore, no matter how big a route or
graph is theoretically it should scale the same way.
</p>
<p>
The user should be aware of the routes but even if you
don't the user worry you can try as many times as you want.
You will be asked after every try to afrim if you wish to
give another try.
</p>

<h2><u>How to run project.</u></h2>

<p>To run the project go after fetching find the shell.sh
and either double click or run in on the cmd
<b><i><u>./shell.sh</u></i></b>

</p>

<p>For linux based system run
<b><i><u>python3 main.py</u></i></b>

</p>


<p>
And on the shell it presumes you have python installed on
your system.
</p>

<p>For testing I have used Pytest as an external library.</p>

<p>Happy Journey! </p>