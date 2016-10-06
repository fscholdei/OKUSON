<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head><link rel="shortcut icon" href="favicon.ico" />
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>Query of scores</title>
  </head>

  <body>
    <Header />
    <h1>Query of scores</h1>

    <h2>Course: <CourseName />, <Semester />, <Lecturer /></h2>

<p>Here you can find out about your scores in the past sheets.</p>

<p>Please enter your ID and password (net yet
<a href="registration.html">registered</a>?):</p> 

<form action="QueryResults" method="post">
  <table>
    <tr>
      <td>ID:</td>
      <td> <input size="12" maxlength="12" name="id" value="" /> </td>
    </tr>

    <tr>
      <td>Password:</td>
      <td> <input type="password" size="16" maxlength="16" name="passwd"
        value="" />
      </td>
    </tr>

    <tr>
      <td> </td>
      <td> <input type="submit" name="Action" value="Submit" /> </td>
    </tr>
  </table>
</form>

    <hr />

    <p><a href="index.html">Back to the main menu</a></p>

    <p class="foot">If there is any question please contact: <br />
      <Feedback /> 
    </p>

    <p class="foot">
      <ValidatorIcon /> <a href="http://www.math.rwth-aachen.de/~OKUSON/">
      (OKUSON <Version/>)</a>
    </p>
    <Footer />
  </body>
</html>

<!-- Copyright 2003 Frank L�beck and Max Neunh�ffer
     $Id: resquery.tpl,v 1.4 2004/10/06 10:26:44 neunhoef Exp $ -->
