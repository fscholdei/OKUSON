<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="/OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>Anzeige der Ergebnisse</title>
  </head>

  <body>
    <h1>Anzeige der Ergebnisse</h1>

    <h2>Vorlesung: <CourseName />, <Semester />, <Lecturer /></h2>

    <p>Sie haben auf den �bungsbl�ttern, deren Abgabefrist
bereits abgelaufen ist, die folgenden Punktzahlen in den
Multiple-Choice-Aufgaben (MC) beziehungsweise in den schriftlichen
Aufgaben (S) erhalten (letztere, soweit diese uns mitgeteilt wurden,
sonst steht da ein `?`. <strong>ACHTUNG</strong>: Die Punkte f�r die
schriftlichen Aufgaben werden nicht regelm��ig erfasst, die wissen Sie
ja von den korrigierten Zetteln.):</p>

    <table>
    <tr><th>�bungsblatt</th><th>Multiple-Choice-Teil</th>
        <th>Schriftlicher Teil</th></tr>

    <Results />

    </table>

    <br />

    <p>Sie haben im Moment insgesamt <Totalscore /> Punkte.</p>

    <GeneralMessages />

    <PrivateMessages />

    <hr />

    <p><a href="/index.html">Zur�ck zur Startseite</a></p>

    <p class="foot">Bei Fragen wenden Sie sich bitte an: <br />
      <Feedback /> 
    </p>

    <p class="foot">
      <ValidatorIcon />
    </p>
  </body>
</html>

<!-- Copyright 2003 Frank L�beck and Max Neunh�ffer
     $Id: results.tpl,v 1.1 2003/09/23 08:14:40 neunhoef Exp $ -->

