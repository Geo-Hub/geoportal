# GeoPortal

## The GeoHub Team

### Objectives
1. Demonstrate a land information systems
2. Demonstrate different access levels for land information. This ensures subsets of
   information can be accessible to the public while others by admins only.
4. Demonstrate GIS can be used to assess quality and attributes of land before purchasing.

_To demo different access levels admin can log in and out and not that the names of land owners toggles visibility_

### _Presented at the 2015 Jkuat Tech Expo_

#### _Won most popular award_

The app is up at [https://geoportal.victorngeno.com](https://geoportal.victorngeno.com)

See the [Geo part here](https://geoportal.victorngeno.com/data/)

##### Pre requisites
1. Docker installation. Install from https://docs.docker.com/engine/install/
##### _Setup Instructions_
These assume unix commands ie Ubuntu/Mac. For windows users, might need to substitute with relevant commands.
These are run in the terminal.
1. cd into your projects directory.
2. Clone this repo `git clone https://github.com/Geo-Hub/geoportal.git`
3. cd into the newly created folder `cd geoportal`
4. Copy `.env.sample` file into `.env` with `cp .env.sample .env`
5. Update the values in the `.env` to your specifics.
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
