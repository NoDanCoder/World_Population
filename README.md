# World Population Predictor

## Introduction

This software is made to provide a perspective about world population quantity within 5 years; its development was part of an *Electronic Engineering* program in *Francisco Jose de Caldas Distrital University*, related to *Physic I* university subject.

## Synopsis

This program plains to keep a track of three days of a web page, [this](https://www.worldometers.info/) page has a record of every born and death in the world, to achieve this objective, we have made a web scrapping program checks every hour between ```12:00 PM``` and ```12:00 AM``` (Time zone is related to GMT-5 according to Coordinated Universal Time - UTC), starting from ```3/06/2020``` the given web page.

We tried to keep scrapping process still running on Amazon Elastic Compute Cloud (Amazon EC2), to automate this process throughout of time, we found some issues and a short time to develop this project, so this topic will be frozen.

After this, data will be cleaned and formatted to be interpreted by a linear regression model, giving a prediction chart at the end.

## Installation

It was made using python 3.8, you can download it [here](https://www.python.org/downloads/release/python-380/).

- Clone the repo:

```bash
git clone https://github.com/Wetgou/World_Population.git
```

- Install the dependences:

```bash
pip install -r requirements.txt
```

- Get into program folder:

```bash
cd World_Population/raw-data/
```

- And run:

```bash
./collect.py
```

## Usage

Every time you run the script, it creates a file called ```dataset.json```, where stores the info, in JSON format.

## Roadmap

- Achieve to make a linear model to interpret the data, and plot it into a chart.
- Complete README files for sub-folders.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
