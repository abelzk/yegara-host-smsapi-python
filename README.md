# yegara-host-smsapi-python
This repository contains a Python script that allows you to send free SMS messages using the Yegara Host SMS Gateway. You can use this script to send OTP, notifications, alerts, and other messages from your websites and apps. 
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://ethiosolve.com">
    <img src="images/ethlogo.png" alt="ethiosolve 3d logo" width="120" height="120">
  </a>

  <h3 align="center">Yegara Host SMS API Python Script</h3>

  <p align="center">
    Simple python script to implement SMS API for your sites.
    <br />
    <a href="https://ethiosolve.com"><strong>Visit Ethiosolve»</strong></a>
    <br />
    <br />
    <a href="https://my.yegara.com/index.php?fuse=knowledgebase&controller=articles&view=article&articleId=8">Yegara Documentation</a>
    <a href="https://ethiosolve.com/plagiarism-checker">Plagiarism Checker</a>
    ·
    <a href="https://ethiosolve.com/referrals">Referral Programs</a>
    ·
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://ethiosolve.com)

This repository contains a Python script that allows you to send free SMS messages using the `Yegara Host SMS Gateway`. You can use this script to send OTP, notifications, alerts, and other messages from your websites and apps. The script uses the `Yegara Host API` to communicate with the SMS Gateway and requires a valid API key and sender ID. You can also use the WordPress plugin provided by Yegara Host to integrate the SMS Gateway with your WordPress site. This script is easy to use and customize, and it supports both Unicode and non-Unicode characters.

Create `app.py` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Prerequisites

* [![Python]
To use this script, you need to have Python 3 installed on your system and install the requests library using pip:
`pip install requests`
You also need to have a Yegara Host account and a domain name registered with them. You can sign up for a free account [here](https://yegara.com).
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

First import these libraries

* `import random`
* `import string`
* `import requests`

To use this script, you need to edit the following variables in the code:
* `username:` Your domain name registered with Yegara Host.
* `password:` Your Yegara Host account password.
* `to:` The phone number of the recipient in international format (e.g. +251911234567).
* `message:` The message you want to send. If you are using a template, this will be the variable part of the message (e.g. OTP code).
* `template_id:` The template ID of the message you want to send. You can choose from the predefined templates or create your own custom template in your Yegara Host dashboard.

The script defines two functions: generateOTP() and sendSMS(). The first function generates a random 4-digit OTP code using the random module. The second function sends an SMS message using the requests module and prints the JSON response from the server.

You can run the script from the command line or import it as a module in your own Python program. The script will generate a random OTP code and send it to the specified phone number using the ‘otp’ template. You can change the template ID or the message as per your requirement.

<strong>Template IDs</strong>
    
    * otp
    * otp_1
    * welcome
    * welcome_1
    * reminder
    * reminder_1
    * shopping
    * shopping_1
    * confirmation
    * confirmation_1

_For more examples, please refer to the [Documentation](https://my.yegara.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Reference

 * [(https://yegara.com/sms-gateway/](https://yegara.com/sms-gateway/)
 * [https://yegara.com/sms-api/](https://yegara.com/sms-api/)
 * [https://yegara.com/free-hosting/](https://yegara.com/free-hosting/)
 * [LICENCE](https://github.com/yegara-host-smsapi-python/LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Abel Zecharias - [Instagram](https://instagram.com/_abelzk) - abelzeki24@gmail.com

Project Link: [https://github.com/abelzk/yegara-host-smsapi-python](https://github.com/abelzk/yegara-host-smsapi-python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
