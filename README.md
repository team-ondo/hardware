<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
<a href="https://github.com/team-ondo/backend">
<img src="docs/images/logo_current.png" alt="Logo" width="350" height="119">
</a>

<h3 align="center">ondo-hardware</h3>

  <p align="center">
    Hardware implementation of ondo
    <br />
    <a href="https://github.com/team-ondo/hardware"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://ondo.onrender.com/">View Demo</a>
    ·
    <a href="https://github.com/team-ondo/hardware/issues">Report Bug</a>
    ·
    <a href="https://github.com/team-ondo/hardware/issues">Request Feature</a>
  </p>
</div>


<details>
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
        <li>
            <a href="#prerequisites">Prerequisites</a>
            <ul>
                <li><a href="#environment">Environment</a></li>
                <li><a href="#set-up-env">Set up .env</a></li>
            </ul>
        </li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

### Built With

[![Python][Python]][Python-url]  
[![Socket.io]][Socket.io-url]  
[![Redis]][Redis-url]  
[![Visual studio code][Visual studio code]][Visual studio code-url]  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

### Prerequisites

#### Environment

- Install poetry

#### Set up .env

- Create a new file named .env at the root of the project.
- Set up the .env file and set the key and values like below.
    ```env
    SERVER_URL="https://ondo-backend-test.onrender.com"
    ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/team-ondo/hardware.git
   ```
2. Install libraries
   ```sh
   poetry install
   ```
3. Run state machine program
   ```sh
   make run-state
   ```
4. Run socket client program
    ```sh
    make run-socket
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Roadmap

See the [open issues](https://github.com/team-ondo/hardware/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


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


## Contact

Project Link: [https://github.com/team-ondo/hardware](https://github.com/team-ondo/hardware)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/team-ondo/hardware.svg?style=for-the-badge
[contributors-url]: https://github.com/team-ondo/hardware/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/team-ondo/hardware.svg?style=for-the-badge
[forks-url]: https://github.com/team-ondo/hardware/network/members
[stars-shield]: https://img.shields.io/github/stars/team-ondo/hardware.svg?style=for-the-badge
[stars-url]: https://github.com/team-ondo/hardware/stargazers
[issues-shield]: https://img.shields.io/github/issues/team-ondo/hardware.svg?style=for-the-badge
[issues-url]: https://github.com/team-ondo/hardware/issues
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Socket.io]: https://img.shields.io/badge/Socket.io-black?style=for-the-badge&logo=socket.io&badgeColor=010101
[Socket.io-url]: https://socket.io/
[Redis]: https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[Visual Studio Code]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Visual Studio Code-url]:https://code.visualstudio.com/
