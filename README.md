# Automatic Door Lock 🔒
It is a IOT and AWS cloud based door lock system

<h3>Introduction 🚪</h3><br>
The Automatic Door Lock System is a security system that allows authorized personnel to enter a restricted area while keeping unauthorized personnel out. The system works by using a combination of hardware and software to detect the presence of an authorized person and unlock the door for them.<br><br>
The system uses a facial authoriztion to identify authorized personnel once the howseowner authorises the guest the door will unlocked by owner 🔓.

<h3>User Story</h3>
When a guest comes to your door and press the push button, Raspberry Pi performs three tasks:

- It takes a picture of the guest and upload it to AWS S3 Bucket and S3 Bucket trigger a SNS notification to a specific topic.
- It sends an email with presigned url of photo to the house owner.

After Getting the email owner have to decide that wether to unlock the door or not. If owner reckognise the guest, owner pushed the push button and that button will be connected to the Arduino UNO and the Arduino controls the servo motor and servo motor will rotate Anti clockwise 180 for unlocking the door

# Refrences 
<b>Project Defination</b>: https://www.hackster.io/taifur/intelligent-door-lock-f9b7c3<br>
<b>Raspberry PI OS and All Instalation Process</b>: https://www.raspberrypi.com/software/

# For any queries Contact me
- 📫Linked IN : https://www.linkedin.com/in/raj-beladiya/<br>
<br>
<img src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" title="AWS" alt="AWS" width="40"        height="40"/>&nbsp;
