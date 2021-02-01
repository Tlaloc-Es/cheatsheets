<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Cheatsheets</h3>

  <p align="center">
    An tool  to cheat
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Tlalocan/cheatsheets">View Demo</a>
    ·
    <a href="https://github.com/Tlalocan/cheatsheets/issues">Report Bug</a>
    ·
    <a href="https://github.com/Tlalocan/cheatsheets/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Whit this tool you could create cheatsheets of commands in order to can execute again easely.

Probably you needed some bash command in order to do any task, and you search again any time that you need. Now you can only save as a cheatsheets and use this tool in order to execute again

### Built With

* Python

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need have installed python and pip v3.

  ```sh
  sudo apt install python3 python3-pip
  ```

### Installation


```sh
   pip install cheatsheets
```

<!-- USAGE EXAMPLES -->
## Usage

Each cheatsheets that you want to store, is a json file with the name that you want, in `~/.cheatsheets`

A cheat following the next format:

> cheat.json
>
>```json
>{
>    "name":"List content",
>    "command":"ls",
>    "description":"List content in directory"
>}
>```

If you want to put any argument in order to remplace when execute the cheatsheets, you can do it puting the name of the argument betwen `<name of arg>`

> cheat.json
>
>```json
>{
>    "name":"List content",
>    "command":"ls <ls> <directory>",
>    "description":"List content in directory"
>}
>```

after this you can list your cheatsheets with

```sh
cheatsheets
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Tlalocan/cheatsheets/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Tlalocan/cheatsheets](https://github.com/Tlalocan/cheatsheets)

https://github.com/Tlalocan/cheatsheets
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Tlalocan/cheatsheets.svg?style=for-the-badge
[contributors-url]: https://github.com/Tlalocan/cheatsheets/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Tlalocan/cheatsheets.svg?style=for-the-badge
[forks-url]: https://github.com/Tlalocan/cheatsheets/network/members
[stars-shield]: https://img.shields.io/github/stars/Tlalocan/cheatsheets.svg?style=for-the-badge
[stars-url]: https://github.com/Tlalocan/cheatsheets/stargazers
[issues-shield]: https://img.shields.io/github/issues/Tlalocan/cheatsheets.svg?style=for-the-badge
[issues-url]: https://github.com/Tlalocan/cheatsheets/issues
[license-shield]: https://img.shields.io/github/license/Tlalocan/cheatsheets.svg?style=for-the-badge
[license-url]: https://github.com/Tlalocan/cheatsheets/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[bitcoin-shield]: https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/128px-Bitcoin.svg.png
[bitcoin-donation]: https://www.blockchain.com/btc/address/18p1E49PaampipMXgf7rR5JypGJUHuRVSj
