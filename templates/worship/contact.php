<?php

// configure
$from = 'youremail@mail.com';  // the email address that will be in the From field of the email. Important: To avoid being marked as spam, use email on your domain: so if you will be using the form on mygreatsite.com, use 'info@mygreatsite.com' in this variable. 
$sendTo = 'youremail@mail.com'; // the email address that will receive the email with the output of the form. Can be your personal address or can be same as the address as in $from variable. Make sure this email exists
$subject = 'New message from contact form'; // the subject of the email
$fields = array('name' => 'Name', 'email' => 'Email', 'title' => 'Title', 'message' => 'Message'); // array variable name => Text to appear in email
$okMessage = 'Contact form successfully submitted. Thank you, I will get back to you soon!';
$errorMessage = 'There was an error while submitting the form. Please try again later';

// let's do the sending

try
{
    $emailText = "\nYou have new message from contact form\n===============================\n\n";

    foreach ($_POST as $key => $value) {

        if (isset($fields[$key])) {
            $emailText .= "$fields[$key]: \n$value\n\n";
        }
    }

    mail($sendTo, $subject, $emailText, "From: " . $from);

    $responseArray = array('type' => 'success', 'message' => $okMessage);
}
catch (\Exception $e)
{
    $responseArray = array('type' => 'danger', 'message' => $errorMessage);
}

if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    $encoded = json_encode($responseArray);
    
    header('Content-Type: application/json');
    
    echo $encoded;
}
else {
    echo $responseArray['message'];
}
