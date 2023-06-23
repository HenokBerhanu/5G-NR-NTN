version: '3.8'
services:
    oai-nrf:
        container_name: "rfsim5g-oai-nrf"
        image: oaisoftwarealliance/oai-nrf:v1.5.0
        environment:
            - NRF_INTERFACE_NAME_FOR_SBI=eth0
            - TZ=Europe/Paris
        networks:
            public_net:
                ipv4_address: 192.168.71.130
    mysql:
        container_name: "rfsim5g-mysql"
        image: mysql:8.0
        volumes:
            - ./oai_db.sql:/docker-entrypoint-initdb.d/oai_db.sql
            - ./mysql-healthcheck.sh:/tmp/mysql-healthcheck.sh
        environment:
            - TZ=Europe/Paris
            - MYSQL_DATABASE=oai_db
            - MYSQL_USER=test
            - MYSQL_PASSWORD=test
            - MYSQL_ROOT_PASSWORD=linux
        healthcheck:
            test: /bin/bash -c "/tmp/mysql-healthcheck.sh"
            interval: 10s
            timeout: 5s
            retries: 30
        networks:
            public_net:
                ipv4_address: 192.168.71.131
networks:
    public_net:
        driver: bridge
        name: rfsim5g-oai-public-net
        ipam:
            config:
                - subnet: 192.168.71.128/26
        driver_opts:
            com.docker.network.bridge.name: "rfsim5g-public"
    traffic_net:
        driver: bridge
        name: rfsim5g-oai-traffic_net-net
        ipam:
            config:
                - subnet: 192.168.72.128/26
        driver_opts:
            com.docker.network.bridge.name: "rfsim5g-traffic"