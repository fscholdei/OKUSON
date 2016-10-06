<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head><link rel="shortcut icon" href="favicon.ico" />
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="OKUSONAdmin.css" type="text/css" rel="StyleSheet" />

    <title>Display/Delete Private Messages</title>
  </head>

  <body>
    <Header />
    <h1>Display/Delete Private Messages</h1>

    <h2>Course: <CourseName />, <Semester />, <Lecturer /></h2>

    <p><LoginStatus /></p>

    <p>Private messages for: <FirstName /> <LastName />, <IdOfPerson /></p>

    <form action="DeleteMessagesDowork" method="post">
    <PrivateMessagesForDeletion />
    <p><input type="submit" name="Action" value="Delete marked" />
       <AdminPasswdField /></p></form>

    <p><a href="AdminMenu">Back to administrator menu</a></p>

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
     $Id: showmessages.tpl,v 1.5 2004/10/06 10:26:44 neunhoef Exp $ -->
