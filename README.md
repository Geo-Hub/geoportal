# GeoPortal

## The GeoHub Team

### _Presented at the 2015 Jkuat Tech Expo_

#### _Won most popular award_

The app is up at [https://geohub-geoportal.herokuapp.com](https://geohub-geoportal.herokuapp.com)

See the [Geo part here](https://geohub-geoportal.herokuapp.com/data/)

##### Pre requisites
1. Docker installation. Install from https://docs.docker.com/engine/install/
##### _Setup Instructions_
These assume unix commands ie Ubuntu/Mac. For windows users, might need to substitute with relevant commands.
These are run in the terminal.
1. cd into your projects directory.
2. Clone this repo `git clone https://github.com/Geo-Hub/geoportal.git`
3. cd into the newly created folder `cd geoportal`
4. Copy `.env.sample` file into `.env` with `cp .env.sample .env`
5. Update the values in the `.env` to your liking. 
6. Run `docker compose up --build`
7. Load the webserver from [http://localhost:8002](http://localhost:8002)

#### Contributors (Team GeoHub)

1. [Ng'eno Victor](https://github.com/ngenovictor)
2. [Nombu Murage](https://github.com/nombumurage)
3. Sophia Njeri
4. [Thomas Muteti](https://github.com/Thom03)
5. James Mwangi

#### Screen Shots

1. Kiambu County loaded on the data page
    ![Kiambu County](screenshots/kiambu_county.png)
2. Kiambu constituency loaded on the data page
    ![Constituency View](screenshots/constituency_view.png)
3. Farms (Shambas) loaded on the data page
    ![Shamba View Example](screenshots/shamba_view_rates_paid.png)
