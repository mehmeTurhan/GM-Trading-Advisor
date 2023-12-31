# GM TradingAdvisor 
Gustavo Sanchez and Mehmet Turhan

An event driven architecture. We would like to execute a financial trade, that would be pulling in data from an API to then execute the trading algorithm. 

The API we are using is from this website:https://site.financialmodelingprep.com/ and it provides the most gainers of the day of the stock market as well as the stock ticker and the price of the top 5

Our module will be even driven architecture with some mix of microservice. 

The languages we will be using will be python. 

The general description of the UI will either be to display the top names to trade for the day based on volatility and option expiration, or to execute the trade and display a profit loss up to the current date. 

## Framework
![image](https://github.com/mehmeTurhan/GM-Trading-Advisor/assets/97054495/ca2f8654-a38d-492b-8f83-1196f7e8a4eb)

## To run the API to get the top 5 gainers on Docker and Kubernets
1.Clone the repository and start the terminal in SymbolsAPI 

2.To build docker container 
```
 docker build -t <your user name>/gainers:1.0 .            
```
3.To run in on your local host using docker. URL:[localhosthttp://localhost:8081/gainers](http://localhost:8081/gainers)
```
docker run -p 8081:8081 <your user name>/gainers:1.0
```
4.To create the kubernetes deployment and services
```
kubectl apply -f gainers-deployment.yaml      
```
5.To see which port the service is running
```
kubectl get all
```
![image](https://github.com/mehmeTurhan/GM-Trading-Advisor/assets/97054495/833eb988-4397-4584-af06-e3722acb7823)


6. In this case, our service is running on 8081:32675,So, URL:http://localhost:32675/gainers

## COMMANDS
Compose to build any images that need to be built before starting the containers, building multiple containers. 
```
Docker-compose up --build
```
(this command let me DELETE products in our database when it was running infinite loops)
``` 
Docker-compose up -d db 
```
command  used to start up all the containers defined in my yml
``` 
Docker-compose up
```

### Update:

Since our presentation we we able to do a connection between admin and main, using POSTMAN we were able to POST in port localhost:8000 which was our admin database connection, and it would add its own ID number plus the information we sent it. Subsequently it would also add the same data with the same ID number to localhost:8001 which was where our main database was located at. 

### Database and Mock UI:
![image](https://github.com/mehmeTurhan/GM-Trading-Advisor/assets/97054495/e38d0e27-9082-45ad-b207-89cb3eb1abaf)

![image](https://github.com/mehmeTurhan/GM-Trading-Advisor/assets/97054495/176bf55b-551e-4b2d-869d-b8e9b6ff8698)

### Working on
We weren't able to POST from our admin code, as it kept getting stuck in an infinite loop and after some lag time it would finally appear in our "main" database, but with many repeating tickers. Our moching_UI file shows what we would've wanted the user interface to be, which was asking how much they would like to deposit and it would calculate the overall win or loss of the day. 

