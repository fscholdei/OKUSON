<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head><link rel="shortcut icon" href="favicon.ico" />
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="OKUSONSheet.css" type="text/css" rel="StyleSheet" />

    <title>Sheet <SheetName /></title>
  </head>

  <body>
    <Header />
    <h1>Sheet <SheetName /></h1>

    <h2>Course: <CourseName />, <Semester />, <Lecturer /></h2>

    <IfIndividualSheets>
    <p>For ID: <IdOfPerson /></p>
    </IfIndividualSheets>

    <p>Due date: <OpenTo /></p>

    <IfIndividualSheets>
    <p>This page was created at: <CurrentTime /></p>

    <p>
     <IfClosed><strong>This sheet is already closed.</strong></IfClosed>
     <IfOpen>This sheet is still open.</IfOpen>
    </p>
    </IfIndividualSheets>

    <form action="SubmitSheet" method="post">
     <IfIndividualSheets>
     <div>
     <HiddenIdOfPerson />
     <HiddenNameOfSheet />
     </div>
     </IfIndividualSheets>
     
     <WebSheetTable />
     
     <IfIndividualSheets>
     <IfOpen>
      <p>Password:
         <input type="password" size="16" maxlength="16" name="passwd"
                value="" />
         <input type="submit" value="Abgeben" name="action" />
      </p>
     </IfOpen>
     <IfClosed>
      <p><strong>This sheet is already closed!</strong></p>
     </IfClosed>
     </IfIndividualSheets>
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
     $Id: sheet.tpl,v 1.6 2004/10/06 10:26:44 neunhoef Exp $ -->
