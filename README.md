# HomeLEDController

This is a full-stack microservice-based project meant to control 256 individually addressable LEDs across 4 locations in the home.

## Details

This project supports both a dev and prod environment (prod is not yet live).

Development Environment: [development.home-led-controller.rrjamal.ca](https://development.home-led-controller.rrjamal.ca/)  
Production Environment: [home-led-controller.rrjamal.ca](https://home-led-controller.rrjamal.ca/)

The [front-end](https://github.com/RaymanRJ/HomeLEDController/tree/development/src/front-end/home-led-controller) is a simple React project that sends requests to a private AWS API Gateway.  
The API Gateway then communicates with a local [web server](https://github.com/RaymanRJ/HomeLEDController/tree/development/src/webserver) running Flask and TinyDB, which has the ability to control the [microcontrollers](https://github.com/RaymanRJ/HomeLEDController/tree/development/src/microcontroller) that the LED strips are on.

## Components

Front-End: React  
Back-End: Flask (Python), TinyDB (Database), [ESP8266 Microcontrollers](https://www.sparkfun.com/products/17146), [LED Strips](https://www.amazon.ca/BTF-LIGHTING-Flexible-Individually-Addressable-Non-waterproof/dp/B01CDTEJBG)  
Infrastructure (AWS): CloudFormation, S3, ECR, CloudFront, Route53, API Gateway
