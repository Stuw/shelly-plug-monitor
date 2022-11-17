# Overview

Deploy Shelly Plug S dashboard in Docker with minimal efforts.

Monitoring consists of 4 main components:
* Shlly Plug S configured with login and password;
* Monitoring container collects data from Shelly Plug S for Prometheus (https://github.com/geerlingguy/shelly-plug-prometheus);
* Prometheus container aggregates data from the monitoring container;
* Grafana displays data from the prometheus container.

![Grafana dashboard example](images/shelly-plug-s-grafana-dashboard.jpg)

# Usage

NOTE: there is an issue with permissions after first run (1)

* Clone repo: `git clone https://github.com/Stuw/shelly-plug-monitor.git --recursive`
* Change dir `cd shelly-plug-monitor`
* Copy `shelly-plug-config.env.sample` to `shelly-plug-config.env` and modify it to fit you shelly plug configuration
* Run `docker compose up`
* Go to Grafana at `https://<your_server_ip>:3000` and login with username `admin` with password `admin`
* Change Grafana admin password
* Interrupt docker compose
* Fix permissions: `sudo chown -R $(id -u):$(id -g) .` (1)
* Run `docker compose up`
* Find shelly plug dashboard
* Enjoy
