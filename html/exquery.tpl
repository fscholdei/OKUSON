<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="/OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>�bungsblatt abrufen</title>
  </head>

  <body>
    <h1>�bungsblatt abrufen</h1>

    <h2>Vorlesung: <CourseName />, <Semester />, <Lecturer /></h2>

    <p>Bitte geben Sie Ihre Matrikelnummer und Ihr Passwort ein (mit dem
    Sie sich <a href="/registration.html">angemeldet</a> haben).
    </p>

<!--    <p>Auch wenn Sie nicht angemeldet sind, k�nnen Sie sich als Gast
    Beispielbl�tter ansehen. Benutzen Sie die Nummer <GuestId />
    mit beliebigem (auch leerem) Passwort.</p>
-->
    <form action="QuerySheet" method="post">

    <table>
    <tr><td>Ihre Matrikelnummer: </td>
    <td><input size="8"  maxlength="6" name="id" value="" /></td></tr>
    <tr><td>Ihr Passwort: </td>
    <td><input type="password" size="16"
               maxlength="16" name="passwd" value="" /> </td></tr>
    <tr><td>Gew�nschter Dokumenttyp 
            (<a href="/doctypehelp.html">Hilfe</a>):</td>
    <td><select name="format">
        <option selected="selected">HTML</option>
        <option>PDF</option>
    </select></td></tr>
    <tr><td>Aufl�sung:</td>
    <td><select name="resolution">
        <AvailableResolutions />
    </select></td></tr>
    </table>

    <p>Die folgenden �bungsbl�tter sind verf�gbar:</p>
    <p><AvailableSheetsAsButtons /></p>

    </form>

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
     $Id: exquery.tpl,v 1.1 2003/09/23 08:14:40 neunhoef Exp $ -->

